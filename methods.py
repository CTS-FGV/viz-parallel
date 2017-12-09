import pandas as pd


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


# Infos Methods
def get_countunique(series: pd.Series) -> int:
    """
    Count the number of uniques
    :param series:
    :return:
    """
    return len(get_unique_categorical(series))


def get_mean(series: pd.Series) -> float:
    """
    Count the number of uniques
    :param series:
    :return:
    """
    return series.mean()


def get_median(series: pd.Series) -> float:
    """
    Count the number of uniques
    :param series:
    :return:
    """
    return series.median()


def get_std(series: pd.Series) -> float:
    """
    Count the number of uniques
    :param series:
    :return:
    """
    return series.std()


def get_skew(series: pd.Series) -> float:
    """
    Count the number of uniques
    :param series:
    :return:
    """
    return series.skew()
