
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

# (2) Seleção gráfico + instância
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

           html.Div([

               html.P('Selecione a instância a ser comparada:'),
               dcc.RadioItems(
                   id='compare-selector',
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
        ),

    html.Hr(),

# (3) Seleção da comparação
    html.Div([

            html.P('Selecione os valores para comparação:',
                   style={'margin-top': '20'})

    ]),

    html.Div([

           html.Div([
               dcc.Dropdown(
                   id='compare-values',
                   options=[{'label': option['full_name'],
                             'value': option['back_name']}
                            for option in options_properties]
                    )
                ],
               className='four columns'
           ),

           html.Div([

               dcc.Dropdown(
                   id='xaxis-type',
                   options=[{'label': option['full_name'],
                             'value': option['back_name']}
                            for option in options_properties]
                    )
                ],
               className='four columns'
                )
            ],
            className='row'
        ),

# (4) Gráficos
    html.Div(
        [
            html.Div(
                [
                    dcc.Graph(id='plot_1')
                ],
                className='six columns',
                style={'margin-top': '20'}
            ),
            html.Div(
                [
                    dcc.Graph(id='plot_2')
                ],
                className='six columns',
                style={'margin-top': '20'}
            ),
        ],
        className='row'
    ),

    html.Div(
        [
            html.Div(
                html.H5('Algo interessante para'
                        'ser colocado aqui'
                        ''
                        '\n Um número bonito:'
                        '\n 13718 coisas'),
                className='three columns',
                style={'margin-top': '40'}
            ),
            html.Div(
                [
                    dcc.Graph(id='plot-diff')
                ],
                className='six columns',
                style={'margin-top': '40'}
            ),
            html.Div(
                html.H5('Hnm... Muito interessante'
                        ''
                        '\n Outro número bonito: '
                        '\n 1823 coisas'),
                className='three columns',
                style={'margin-top': '40'}
            ),
        ],
        className='row'
    ),

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

