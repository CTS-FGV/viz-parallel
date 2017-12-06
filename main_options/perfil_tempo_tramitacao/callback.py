import pandas as pd

raw_data = pd.read_csv('main_options/perfil_tempo_tramitacao/perfil_tramitacao.csv')


def draw_plot_1(status, perido):
    pass

perfil_tempo_tramitacao = {'draw_plot_1': draw_plot_1,
                           'raw_data': raw_data}

if __name__ == '__main__':
    pass