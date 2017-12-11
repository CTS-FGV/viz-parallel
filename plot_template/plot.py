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

    return figure

# Do not change this
output = {'plot': plot}

if __name__ == '__main__':
    pass
