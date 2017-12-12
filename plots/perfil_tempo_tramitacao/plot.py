import pandas as pd
import numpy as np
import plotly.graph_objs as go
import imp

raw_data = imp.load_source('info', 'plots/perfil_tempo_tramitacao/get_raw_data.py').output['raw_data']

#org = ['Administrativa', 'Comissões Temáticas', 'Constituição e Justiça',
#       'Mesa', 'Plenário', 'Temporárias', 'Tributação e Finanças']

org = ['Administrativa', 'Comissões Temáticas', 'Temporárias',
       'Constituição e Justiça', 'Tributação e Finanças', 'Mesa', 'Plenário']

bins = np.linspace(0, 300, 31)


def plot(input, raw_data, filtered_data):
    status = input['situacao-perfil']
    periodo = input['tempo-perfil']

    return prepare_plot(raw_data, filtered_data, status, org, bins, periodo)


def draw_plot(x, y, z, hm_col):
    trace = [go.Heatmap(z=z,
                        y=y,
                        x=x,
                        # text=hovertext,
                        # hoverinfo='text',
                        colorscale=[

                            [0, hm_col[6]],
                            [1 / 7, hm_col[6]],

                            # Let values between 10-20% of the min and max of z
                            # have color rgb(20, 20, 20)
                            [1 / 7, hm_col[5]],
                            [2 / 7, hm_col[5]],

                            # Values between 20-30% of the min and max of z
                            # have color rgb(40, 40, 40)
                            [2 / 7, hm_col[4]],
                            [3 / 7, hm_col[4]],

                            [3 / 7, hm_col[3]],
                            [4 / 7, hm_col[3]],

                            [4 / 7, hm_col[2]],
                            [5 / 7, hm_col[2]],

                            [5 / 7, hm_col[1]],
                            [6 / 7, hm_col[1]],

                            [6 / 7, hm_col[0]],
                            [1.0, hm_col[0]]],
                        zmin=0,
                        zmax=70,
                        colorbar=go.ColorBar(title='Tempo no órgão (%)', titleside='top'),
                        showscale=True)]

    layout = dict(
            margin=dict(l=150, r=50, b=50, t=100, pad=4),
            xaxis=dict(title='Tempo de tramitação na Câmara (meses)'))

    figure = dict(data=trace, layout=layout)
    return figure


def prepare_data(raw_data, filtered_data, status=None, periodo=None):
    if status:
        # df = raw_data[raw_data['situacao_tipo'] == status]
        # df['dataInicio'] = pd.to_datetime(df['dataInicio'])
        # df = df[df['dataInicio'] >= str(periodo[0])]
        # df = df[df['dataInicio'] <= str(periodo[1])]
        df = filtered_data
        print('FILTEDER!!!!!!')
        #print(filtered_data)
    else:
        df = raw_data

    df1 = df.groupby(['idProposicao', 'tipoOrgao']).sum()['tempo'].reset_index()
    df1 = df1.pivot(index='idProposicao', columns='tipoOrgao', values='tempo') / 30
    df1['Sum'] = df1.sum(1)
    df1 = df1.sort_values(by='Sum').reset_index()

    org_data = set(list(df1.columns))
    org_int = org_data.intersection(org)
    org_ext = list(org_int)


    org_sum = org_ext + ['Sum']

    a = df1.fillna(0)[org_sum]

    b = a.values
    s = a['Sum'].values

    tempo_prep = pd.DataFrame(np.divide(b.T, s).T * 100, columns=org_sum)
    groups = tempo_prep.groupby(np.digitize(df1['Sum'], bins))

    temp = groups.mean()[org_ext]

    temp = temp.fillna(0)

    return temp


# Passar para dentro de draw_plot_1
def prepare_plot(raw_data, filtered_data, status, org, bins, periodo):
    temp = prepare_data(raw_data, filtered_data, status, periodo)

    x = bins
    y = temp.columns.values
    z = temp.values.T

    #print(list(temp.columns.values))

    # hovertext = list()
    # for yi, yy in enumerate(y):
    #    hovertext.append(list())
    #    for xi, xx in enumerate(x):
    #        if xi < len(z1[yi]):
    #            xx = int(xx)
    #            hovertext[-1].append(
    #                'Dos PLs tramitados de {} a {} meses na Câmara,<br>'.format(xx, xx + 10) + ' {0:.3f}% '.format(
    #                    z1[yi][xi]) + 'do tempo foi em {}'.format(yy))
    #        else:
    #            hovertext[-1].append('Não houveram PLs tramitados na Câmara por {} meses'.format(xx))

    hm_col = ['#450A5C', '#423C81', '#34608C', '#2583A5', '#61B7C7', '#75D2DA', '#C1E1EA']

    return draw_plot(x, y, z, hm_col)


output = {'plot': plot}

if __name__ == '__main__':
    pass
