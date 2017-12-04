
# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import flask
from dash.dependencies import Input, Output
import yaml
from flask import send_from_directory
import os

from main_options.fluxo_tramitacao.callback import fluxo_tramitacao
from main_options.perfil_tempo_tramitacao.callback import perfil_tempo_tramitacao



### CONFIG APP

server = flask.Flask(__name__)
app = dash.Dash(name='app1', sharing=True, server=server, csrf_protect=False)


# CONSTANTS
options_properties = yaml.load(open('main_options/options_properties.yaml', 'r'))
options_functions = {'fluxo_tramitacao': fluxo_tramitacao,
                     'perfil_tempo_tramitacao': perfil_tempo_tramitacao}



# ESTRUTURA APP

app.layout = html.Div([

# (1) Título
   html.Div([
               html.H1(
                   'Estrutura de tramitações',
                   className='four columns',
           )
       ],
       className='row'
   ),

# (2) Seleção gráfico + instância
   html.Div([

           html.Div([

               html.P('Selecione o gráfico a ser mostrado:'),
               dcc.RadioItems(
                   id='xaxis-type',
                   options=[{'label': option['full_name'],
                             'value': option['back_name']}
                            for option in options_properties],
                   value=options_properties[0]['back_name'],
                   labelStyle={'display': 'inline-block'}
                    )
                ],
               className='six columns'
           ),

           html.Div([

               html.P('Selecione a instância a ser comparada:'),
               dcc.RadioItems(
                   id='compare_instance',
                   options=[{'label': option['full_name'],
                             'value': option['back_name']}
                            for option in options_properties],
                   labelStyle={'display': 'inline-block'}
                   )
               ],
               className='six columns'
                )
            ],
            className='row'
        )
    ],
    className='ten columns offset-by-one'
)



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

