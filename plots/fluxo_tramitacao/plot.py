import pandas as pd
import plotly.graph_objs as go


# Do not change this function name and inputs
def plot(callback_input: dict, raw_data: pd.DataFrame, filtered_data: pd.DataFrame) -> object:
    """
    This function have to be responsible on transforming raw and rude data on beautiful plots.
    You can filter the data by yourself or use the filtered data DataFrame to plot.

    The callback_input is a dict that contains the information set by the user using the components. The key is the
    data-title given at config.py and the value can be a int/float/str/tuple, depending on the component.

    The dictionary containing the information has the following structure:
    {'name' : 'Mean: ',
     'value': int/float/str}

    :param callback_input: Filters
    :param raw_data: Raw data
    :param filtered_data: Already filtered data
    :return: Plotly Figure
    """

    select_organ = filtered_data

    colors = ['#0E0F3E', '#3A3B77', '#E4CC18', '#F2B905', '#EFB104']

    data = []

    data.append(go.Scatter(
       x=select_organ['meses'],
       y=select_organ['diff'],
       mode='lines',
       name='Entrada-Saida',
       marker=dict(color=colors[0])
    ))

    data.append(go.Scatter(
            x=select_organ['meses'],
            y=select_organ['entrada'],
            mode='lines',
            name='Entrada',
            marker=dict(color=colors[2])
    ))

    data.append(go.Scatter(
            x=select_organ['meses'],
            y=select_organ['saida'],
            mode='lines',
            name='Saida',
            marker=dict(color='#1f77b4')
    ))

    layout = dict(title='Fluxo de PLs p.d. na Plenário por Mês',
                  yaxis=dict(title='Número de Tramitações'),
                  xaxis=dict(title='Anos')
                  )

    figure = dict(data=data, layout=layout)

    return figure

# Do not change this
output = {'plot': plot}

if __name__ == '__main__':
    pass
