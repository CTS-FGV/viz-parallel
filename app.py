# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import flask
from dash.dependencies import Input, Output
import yaml

import glob
from collections import defaultdict
import imp

from components import components
from methods import wrap_infos

#  CONFIG APP
server = flask.Flask(__name__)
app = dash.Dash(name='app1', sharing=True, server=server, csrf_protect=False)

# CONSTANTS
options_properties = [yaml.load(open(path, 'r')) for path in glob.glob('plots/*/config.yaml')]
options_functions = defaultdict(lambda: dict())

print(options_properties)


def add_functions(path, keyword, opt):
    for base_path in glob.glob(path):
        base_name = base_path.split('/')[1]
        opt[base_name][keyword] = imp.load_source('info', base_path).output[keyword]
    return opt


options_functions = add_functions('plots/*/infos.py', 'infos', options_functions)
options_functions = add_functions('plots/*/plot.py', 'plot', options_functions)
options_functions = add_functions('plots/*/get_raw_data.py', 'raw_data', options_functions)

columns = 2

app.config.supress_callback_exceptions = True

#  ESTRUTURA APP
app.layout = html.Div([
    # title
    html.Div([

        html.H1('Estrutura de tramitações',
                style={'margin-top':    '10',
                       'margin-bottom': '-5',
                       'text-align':    'center'})

    ],
            className='row'
    ),

    html.Div([
        html.Hr()
    ], className='ten columns offset-by-one'),

    # graph selection
    html.Div([

        html.Div([

            html.P('Selecione o gráfico a ser mostrado:'),
            dcc.RadioItems(

                    id='graph-selector',
                    options=[{'label': option['full_name'],
                              'value': option['back_name']}
                             for option in options_properties],
                    value=options_properties[0]['back_name'],
                    labelStyle={'display': 'inline-block'}
            )
        ],
                className='twelve columns offset-by-one'
        ),
    ]
    ),

    # filters
    html.Div(id='menu',
             className='ten columns offset-by-one'
             ),

    html.Div([
        html.Br()
    ], className='twelve columns'),

    # graphs comparisson
    html.Div(
            id='output-container',
            className='twelve columns'

    ),
]
)


# General Functions
def generate_ids(value, col, func):
    return "{value}-{column}-{function}".format(value=value, column=col, function=func)


def get_back_name_properties(back_name):
    return [dic for dic in options_properties if dic['back_name'] == back_name][0]


# Create Menus
@app.callback(Output('menu', 'children'),
              [Input('graph-selector', 'value')])
def update_menu(back_name):
    menus = []

    for opt in options_properties:
        if opt['back_name'] == back_name:
            for column in range(columns):

                container = []

                i = 0
                for variables in opt['variables']:

                    menu_header = html.H3(opt['full_name'] + ' ' + str(column + 1))
                    menu_title = html.P('Selecione um(a) {}'.format(variables['menu_text']))

                    if i == 0:
                        container.append(html.Div([html.Br(), html.Hr(), menu_header, menu_title],
                                                  className='ten columns offset-by-one'))
                    else:
                        container.append(html.Div([html.Br(), menu_title], className='ten columns offset-by-one'))

                    i += 1

                    kwargs = dict(id=generate_ids(variables['data_title'], column, 'menu'),
                                  className='ten columns offset-by-one',
                                  raw_data=options_functions[back_name]['raw_data'],
                                  column_name=variables['column_name'],
                                  back_name=back_name,
                                  data_title=variables['data_title'],
                                  extra_options=variables['options'])

                    container.append(components[variables['type']].component(kwargs=kwargs))

                menus.append(html.Div(container, className='six columns'))

    return menus


# Create Output Containers
@app.callback(
        Output('output-container', 'children'),
        [Input('graph-selector', 'value')])
def display_controls(back_name):
    # Create a unique output container for each pair of dynamic controls
    graphs = html.Div(
            [dcc.Graph(id=generate_ids(back_name, column, 'graph'),
                       className='six columns',
                       style={'text-align': 'center'}) for column in range(columns)])

    space = html.Div([
        html.Br()
    ], className='twelve columns offset-by-one')

    info = html.Div(
            [html.Div(
                    id=generate_ids(back_name, column, 'info'),
                    className='six columns',
                    style={'text-align': 'center'})
                for column in range(columns)])

    return [graphs, space, info, space]



def filter_data(back_name, callback_input):

    options = get_back_name_properties(back_name)['variables']

    filtered_data = options_functions[back_name]['raw_data']

    for variables in options:
        filtered_data = components[variables['type']].filter(callback_input=callback_input,
                                                             extra_options=variables,
                                                             raw_data=filtered_data)
    return filtered_data

# Call Graph Function
def generate_output_callback_graph(back_name):
    def return_graph(*values):

        inp = dict()

        for opt in options_properties:
            if opt['back_name'] == back_name:
                for i, val in enumerate(opt['variables']):
                    inp[val['data_title']] = values[i]

        return options_functions[back_name]['plot'](inp,
                                                    options_functions[back_name]['raw_data'],
                                                    filter_data(back_name, inp))

    return return_graph


# Call Info Function
def generate_output_callback_info(back_name):
    def return_info(*values):

        inp = dict()

        for opt in options_properties:
            if opt['back_name'] == back_name:
                for i, val in enumerate(opt['variables']):
                    inp[val['data_title']] = values[i]

        infos = options_functions[back_name]['infos'](inp,
                                                      options_functions[back_name]['raw_data'],
                                                      filter_data(back_name, inp))

        return wrap_infos(infos)

    return return_info


for back_name in [o['value'] for o in app.layout['graph-selector'].options]:

    for column in range(columns):
        callback_input = []
        for opt in options_properties:
            if opt['back_name'] == back_name:
                for variables in opt['variables']:
                    callback_input.append(Input(generate_ids(variables['data_title'],
                                                             column,
                                                             'menu'),
                                                'value'))

        app.callback(
                Output(
                        generate_ids(back_name, column, 'graph'), 'figure'),
                callback_input)(
                generate_output_callback_graph(back_name)
        )

        app.callback(
                Output(
                        generate_ids(back_name, column, 'info'), 'children'),
                callback_input)(
                generate_output_callback_info(back_name)
        )

app.css.append_css({"external_url": "https://codepen.io/JoaoCarabetta/pen/RjzpPB.css"})

if __name__ == '__main__':
    app.run_server()
