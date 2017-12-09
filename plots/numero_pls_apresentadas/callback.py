import pandas as pd
import numpy as np
import plotly.graph_objs as go

raw_data = pd.read_csv('plots/perfil_tempo_tramitacao/perfil_tramitacao.csv')

def draw_plot_1(raw_data, status, periodo):

    data = []
    legis = ['2014-07-01', '2010-07-01', '2006-07-01', '2002-07-01', '1998-07-01', '1994-07-01', '1990-07-01', '1986-07-01']

    shapes=[]
    for leg in legis:
        shapes.append(dict(type='line', x0=leg, y0=0, x1=leg, y1=4200, line= dict(color='rgb(211,211,211)',width=2, dash='dot')))

    data.append(
        go.Bar(
            y=raw_data,
            x=raw_data.index,
            opacity = 0.75,
            name = 'Ano',
            marker=dict(
                color='#2DA37D'
            ),
            showlegend=False
        )
    )

    data.append(go.Scatter(
        x=['2016-07-01', '2012-07-01', '2008-07-01', '2004-07-01', '2000-07-01', '1996-07-01', '1992-07-01', '1988-07-01'],
        y=[3950, 3950, 3950, 3950, 3950, 3950, 3950, 3950],
        text=['55ª', '54ª', '53ª', '52ª', '51ª', '50ª', '49ª', '48ª'],
        mode='text',
        name='Legislatura'))

    layout = go.Layout(
        title="""Número anual de PLs apresentados por deputados""",
        xaxis=dict(title='Anos'),
        yaxis=dict(title='Número de PLs'),
        width=1000,
        shapes=shapes
    )

def draw_plot_diff(input1, input2):
    pass


numero_pls_apresentadas = {"draw_plot_1": draw_plot_1,
                            "draw_plot_diff": draw_plot_diff
                            #"big_numbers_1": big_numbers_1,
                            #"big_numbers_2": big_numbers_2
                           }