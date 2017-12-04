
# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import flask
from dash.dependencies import Input, Output
import yaml

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
    dcc.RadioItems(
        id='xaxis-type',
        options=[{'label': option['full_name'],
                  'value': option['back_name']}
                 for option in options_properties],
        value=options_properties[0]['back_name'],
        labelStyle={'display': 'inline-block'}
    ),
    html.Div([
        dcc.Input(id='input-1', type='text', value='Montréal'),
        dcc.Input(id='input-2', type='text', value='Canada'),
        html.Div(id='output')
        ]
    ),
])


@app.callback(Output('output', 'children'),
              [Input('input-1', 'value'),
               Input('input-2', 'value'),
               Input('xaxis-type', 'value')])
def draw_plot_1(input1, input2, input3):

    func = options_functions[input3]['draw_plot_1']
    return func(input1, input2)


if __name__ == '__main__':
    app.run_server()

