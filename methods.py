import pandas as pd
import dash_html_components as html
import base64


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

    try:
        for info in infos:
            wrap.append(html.P([info['name'],html.B(info['value'])],
                               style={'color': '#696969',
                                      'text-align': 'left',
                                      'padding-left': 80
                                      }
                               ))
    except TypeError:
        print('No info given')

    return wrap

def html_img(image_path,style={}):
    """
    Insert a image based on the path of file (with filename included).

    :param path: str -- image path
    :return: html.Img object
    """
    encoded_image = base64.b64encode(open(image_path, 'rb').read()).decode()

    return html.Img(src='data:image/png;base64,{}'.format(encoded_image),
                    style=style)
