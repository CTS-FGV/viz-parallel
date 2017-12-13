import pandas as pd
import numpy as np
import plotly.graph_objs as go
import imp

raw_data = imp.load_source('info', 'plots/perfil_tempo_tramitacao/get_raw_data.py').output['raw_data']

org = ['Administrativa', 'Comissões Temáticas', 'Temporárias',
       'Constituição e Justiça', 'Tributação e Finanças', 'Mesa', 'Plenário']

hm_col = ['#caf1f7','#93ecf9','#76d2e0','#51bccc','#078699','#0a5c68','#04333a','#001d21','#001f23','#00090a']

bins = np.linspace(0, 300, 31)


def plot(input, raw_data, filtered_data):
    status = input['situacao-perfil']
    periodo = input['tempo-perfil']

    temp = prepare_data(raw_data, filtered_data, status, periodo)

    x = bins
    y = temp.columns.values
    z = temp.values.T
    #zmax = round(z[:-1].max())

    return draw_plot(x, y, z)


def draw_plot(x, y, z):

    #colorscale
    max = 8
    # max = int(zmax / 10)

    colorscale = [[0, hm_col[0]]]

    for i in range(0, max):
        colorscale.append([i / max, hm_col[i]])
        colorscale.append([(i + 1) / max, hm_col[i]])

    #hovertext
    hovertext = list()
    for yi, yy in enumerate(y):
       hovertext.append(list())
       for xi, xx in enumerate(x):
           if xi < len(z[yi]):
               xx = int(xx)
               hovertext[-1].append(
                   'Dos PLs tramitados de {} a {} meses na Câmara,<br>'.format(xx, xx + 10) + ' {0:.3f}% '.format(
                       z[yi][xi]) + 'do tempo foi em {}'.format(yy))
           else:
               hovertext[-1].append('Não houveram PLs tramitados na Câmara por {} meses'.format(xx))

    trace = [go.Heatmap(z=z,
                        y=y,
                        x=x,
                        text=hovertext,
                        hoverinfo='text',
                        colorscale=colorscale,
                        zmin=0,
                        zmax=80,
                        colorbar=go.ColorBar(title='Tempo no órgão (%)', titleside='top'),
                        showscale=True)]

    layout = dict(
            margin=dict(l=150, r=50, b=50, t=100, pad=4),
            xaxis=dict(title='Tempo de tramitação na Câmara (meses)'))

    figure = dict(data=trace, layout=layout)
    return figure


def prepare_data(raw_data, filtered_data, status=None, periodo=None):

    if status:
        df = filtered_data
        print('FILTEDER!!!!!!')

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


output = {'plot': plot}

if __name__ == '__main__':
    pass
