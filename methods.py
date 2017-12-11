import pandas as pd
import dash_html_components as html


#  Methods to fill components
def get_unique_categorical(series: pd.Series) -> list:
    """
    Get only column uniques of a Pandas Series
    :param series: Categorical Series
    :return: list of categories
    """

    return list(series.unique())


def get_max_min_time(series: object, aggregation: str) -> dict:
    """
    Get only column uniques of a Pandas Series
    :param series: Time Series
    :param aggregation:
    :return: dict with max and min according to aggregation
    """

    dates = pd.to_datetime(series)

    if aggregation == 'year':

        return {'max': dates.max().year,
                'min': dates.min().year}

    elif aggregation is None:

        return {'max': dates.max(),
                'min': dates.min()}


# Infos H5 Wrap
def wrap_infos(infos: dict) -> object:

    wrap = []

    for info in infos:

        wrap.append(html.H5('{name}{value}'.format(name=info['name'],
                                                   value=info['value'])))

    return wrap

