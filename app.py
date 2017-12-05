
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
       dcc.Dropdown(
           id='choice',
           options=[{'label': variables,
                     'value': [0,1]}])]

            className='ten columns offset-by-one'
        ),

   html.Div(id='menu',
            className='ten columns offset-by-one'
        ),
    ]
)

@app.callback(Output('output', 'children'),
              [Input('input-1', 'value')])
def update_menu():

    menus = []

    for variables in options_properties[0]['variables']:

        menus.append(dcc.Dropdown(
                   id='{}'.format(variables),
                   options=[{'label': variables,
                             'value': [0,1]}]
                    )
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

