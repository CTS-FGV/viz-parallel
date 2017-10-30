
# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import flask
import importlib
import sqlalchemy


### CONFIG APP

server = flask.Flask(__name__)
app = dash.Dash(name='app1', sharing=True, server=server, csrf_protect=False)


### CONEXÃO POSTGRES

utils = importlib.machinery.SourceFileLoader('utils','utils.py')
utils = utils.load_module()

con = utils.connect_sqlalchemy_GC()


### IMPORTAÇÃO DOS DADOS

df = pd.read_sql_query("""SELECT sigla_orgao, 
        count(sigla_orgao) AS qtde_tramitacoes,
        EXTRACT(YEAR FROM data_tramitacao) ano
        FROM c_camdep.camdep_proposicoes_tramitacao
        GROUP BY ano, sigla_orgao
        ORDER BY ano, qtde_tramitacoes, sigla_orgao;""", con)

df['ano'] = df['ano'].astype(int)


### ESTRUTURA APP

app.layout = html.Div([
	dcc.Graph(id='graph-with-slider'),
	dcc.RangeSlider(
        	id='year-range-slider',
       		min=df['ano'].min(),
        	max=df['ano'].max(),
        	value=[df['ano'].unique()[-10], df['ano'].unique()[-1]],
        	step=None,
        	marks={str(year): str(year) for year in df['ano'].unique()}
    	)
	])

@app.callback(
	dash.dependencies.Output('graph-with-slider', 'figure'),
	[dash.dependencies.Input('year-range-slider', 'value')])

def update_figure(selected_range):

	traces = []
	for i in range(selected_range[0], selected_range[1]+1):
		tram_anual = df[df.ano == i]
		traces.append(
			go.Scatter(
				x=i,
				y=tram_anual['qtde_tramitacoes'],
				text=tram_anual['sigla_orgao'],
				mode='markers',
           		 	opacity=0.7,
            			marker={
                			'size': 15,
                			'line': {'width': 0.5, 'color': 'white'}
            			},
            			name=i
        		))

	return {
        	'data': traces,
        	'layout': go.Layout(
            		xaxis={'title': 'Ano'},
            		yaxis={'title': 'Volume de tramitações'},
            		margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            		legend={'x': 1, 'y': 1},
            		hovermode='closest'
        		)
    		}

if __name__ == '__main__':
	app.run_server()

