
# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import flask
from dash.dependencies import Input, Output
import yaml
#from flask import send_from_directory
import os

from main_options.fluxo_tramitacao.callback import fluxo_tramitacao
from main_options.perfil_tempo_tramitacao.callback import perfil_tempo_tramitacao
from main_options.numero_pls_apresentadas.callback import numero_pls_apresentadas
from main_options.acumulado_pls_apresentadas.callback import acumulado_pls_apresentadas



### CONFIG APP

server = flask.Flask(__name__)
app = dash.Dash(name='app1', sharing=True, server=server, csrf_protect=False)


# CONSTANTS
options_properties = yaml.load(open('main_options/options_properties.yaml', 'r'))
options_functions = {'fluxo_tramitacao': fluxo_tramitacao,
                     'perfil_tempo_tramitacao': perfil_tempo_tramitacao,
                     'numero_pls_apresentadas': numero_pls_apresentadas,
                     'acumulado_pls_apresentadas': acumulado_pls_apresentadas
                     }

app.config.supress_callback_exceptions = True

# ESTRUTURA APP

app.layout = html.Div([

# (1) Título
   html.Div([

               html.H1('Estrutura de tramitações',
                       style={'margin-top': '10',
                              'margin-bottom': '-5'})

       ],
       className='row'
   ),

   html.Hr(),

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
            className='six columns'
        ),
        ]
    ),

    html.Div(id='menu',
        className='ten columns offset-by-one'
    ),

    html.Div(
        id='output-container'
    ),
    ]
)

@app.callback(Output('menu', 'children'),
              [Input('graph-selector', 'value')])
def update_menu(input1):

    menus = []

    for opt in options_properties:
        if opt['back_name'] == input1:
            for variables in opt['variables']:
                menus.append(dcc.Dropdown(
                           id='{}'.format(variables),
                           options=[{'label': i,
                                     'value': i} for i in range(4)]
                            )
                        )
    return menus


@app.callback(
    Output('output-container', 'children'),
    [Input('graph-selector', 'value')])
def display_controls(back_name):
    # create a unique output container for each pair of dyanmic controls
    return html.H5(id=back_name, className='eight columns',
                    style={'text-align': 'center'})


def generate_output_callback(back_name):
    def print_exit(*values):

        print(values)

        return """Essa é a opção que você clicou {}
                E esse é o resultado {}""".format(back_name, values)

    return print_exit

for back_name in [o['value'] for o in app.layout['graph-selector'].options]:

    callback_input = []
    for opt in options_properties:
        if opt['back_name'] == back_name:
            for variables in opt['variables']:
                callback_input.append(Input(variables, 'value'))

    app.callback(
        Output(back_name, 'children'),
        callback_input)(
        generate_output_callback(back_name)
    )

#@app.callback(Output('output', 'children'),
#              [Input('input-1', 'value'),
#               Input('input-2', 'value'),
#               Input('xaxis-type', 'value')])
#def draw_plot_1(input1, input2, input3):
#
#    func = options_functions[input3]['draw_plot_1']
#    return func(input1, input2)



#@app.callback(Output('output', 'children'),
#              [Input('input-1', 'value'),
#               Input('input-2', 'value'),
#               Input('xaxis-type', 'value')])
#def draw_plot_1(input1, input2, input3):
#
#    func = options_functions[input3]['draw_plot_1']
#    return func(input1, input2)
#
#
#@app.callback(Output('output', 'children'),
#              [Input('input-1', 'value'),
#               Input('input-2', 'value'),
#               Input('xaxis-type', 'value')])
#def draw_plot_2(input1, input2, input3):
#
#    func = options_functions[input3]['draw_plot_1']
#    return func(input1, input2)
#
#
#@app.callback(Output('output', 'children'),
#              [Input('input-1', 'value'),
#               Input('input-2', 'value'),
#               Input('xaxis-type', 'value')])
#def draw_plot_diff(input1, input2, input3):
#
#    func = options_functions[input3]['draw_plot_diff']
#    return func(input1, input2)
#
#
#@app.callback(Output('output', 'children'),
#              [Input('input-1', 'value'),
#               Input('input-2', 'value'),
#               Input('xaxis-type', 'value')])
#def big_numbers_1(input1, input2, input3):
#
#    func = options_functions[input3]['big_numbers_1']
#    return func(input1, input2)
#
#
#@app.callback(Output('output', 'children'),
#              [Input('input-1', 'value'),
#               Input('input-2', 'value'),
#               Input('xaxis-type', 'value')])
#def big_numbers_2(input1, input2, input3):
#
#    func = options_functions[input3]['big_numbers_2']
#    return func(input1, input2)

app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

if __name__ == '__main__':
    app.run_server()

