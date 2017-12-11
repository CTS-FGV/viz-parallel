import pandas as pd
import plotly.graph_objs as go
from .get_raw_data import output


def plot(callback_input: dict, raw_data: pd.DataFrame) -> object:
    """
    Receives the callback_input and returns a figure plotly object
    :param callback_input:
    :return:
    """

    pass

output = {'plot': plot}

if __name__ == '__main__':
    pass
