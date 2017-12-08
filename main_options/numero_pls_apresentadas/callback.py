import pandas as pd
import plotly.graph_objs as go

raw_data = pd.read_csv('main_options/numero_pls_apresentadas/numero_pls_apresentadas.csv')

def draw_plot_1(input):

    periodo=input['tempo-numero']

    raw_data['dataInicio'] = pd.to_datetime(raw_data['dataInicio'])

    df = raw_data[raw_data['dataInicio'] >= str(periodo[0])]
    df = df[df['dataInicio'] <= str(periodo[1])]

    anos = df['dataInicio'].dt.year
    qtde = df['numero_pls']

    trace = [go.Bar(
        y=qtde,
        x=anos,
        opacity=0.75,
        text=['Qtde: {}<br>Ano: {}'.format(i, j) for i, j in zip(qtde, anos)],
        hoverinfo='text',
        name='Ano',
        marker=dict(
            color='#2DA37D'
        ),
        showlegend=False
    )
    ]

    layout = go.Layout(
        xaxis=dict(title='Anos'),
        yaxis=dict(title='Número de PLs')
    )

    figure = dict(data=trace, layout=layout)

    return figure


def draw_plot_diff(input1, input2):
    pass


numero_pls_apresentadas = {"draw_plot_1": draw_plot_1,
                           "draw_plot_diff": draw_plot_diff,
                           "raw_data": raw_data
                           # "big_numbers_1": big_numbers_1,
                           # "big_numbers_2": big_numbers_2
                           }
