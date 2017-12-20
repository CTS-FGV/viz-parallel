import pandas as pd
import plotly.graph_objs as go


def plot(callback_input, raw_data, filtered_data, colors):

    select_organ = filtered_data

    data = []

    data.append(go.Scatter(
       x=select_organ['meses'],
       y=select_organ['diff'],
       mode='lines',
       name='Entrada-Saida',
       marker=dict(color=colors[11])
    ))

    data.append(go.Scatter(
            x=select_organ['meses'],
            y=select_organ['entrada'],
            mode='lines',
            name='Entrada',
            marker=dict(color=colors[5])
    ))

    data.append(go.Scatter(
            x=select_organ['meses'],
            y=select_organ['saida'],
            mode='lines',
            name='Saida',
            marker=dict(color=colors[3])
    ))

    layout = dict(title='Fluxo de PLs p.d. na Plenário por Mês',
                  yaxis=dict(title='Número de Tramitações'),
                  xaxis=dict(title='Ano')
                  )

    figure = dict(data=data, layout=layout)

    return figure

# Do not change this
output = {'plot': plot}

if __name__ == '__main__':
    pass
