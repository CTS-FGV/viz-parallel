import dash_core_components as dcc
import dash_html_components as html
import methods


def dropdown(**kwargs):
    kwargs = kwargs['kwargs']

    id = kwargs['id']
    className = kwargs['className']
    raw_data = kwargs['raw_data']
    column_name = kwargs['column_name']
    back_name = kwargs['back_name']
    data_title = kwargs['data_title']
    extra_options = kwargs['extra_options']

    #  Get categories

    categories = methods.get_unique_categorical(raw_data[column_name])

    options = [{'label': i, 'value': i} for i in categories]
    extra_options['value'] = categories[0]


    return dcc.Dropdown(
        id=id,
        className=className,
        options=options,
        multi=extra_options['multi'],
        clearable=extra_options['clearable'],
        placeholder=extra_options['placeholder'],
        searchable=extra_options['searchable'],
        value=extra_options['value']
    )

def range_slider(**kwargs):
    kwargs = kwargs['kwargs']

    id = kwargs['id']
    className = kwargs['className']
    raw_data = kwargs['raw_data']
    column_name = kwargs['column_name']
    back_name = kwargs['back_name']
    data_title = kwargs['data_title']
    extra_options = kwargs['extra_options']

    interval = methods.get_max_min_time(series=raw_data[column_name],
                             aggregation=extra_options['aggregation'])

    extra_options['max'] = interval['max']
    extra_options['min'] = interval['min']
    extra_options['marks'] = {i: str(i) for i in range(interval['min'], interval['max']+1,2)}
    extra_options['value'] = [interval['min'], interval['max']]
    extra_options['step'] = 1

    return dcc.RangeSlider(
        id=id,
        className=className,
        allowCross=extra_options['allowcross'],
        dots=extra_options['dots'],
        included=extra_options['included'],
        marks=extra_options['marks'],
        max=extra_options['max'],
        min=extra_options['min'],
        step=extra_options['step'],
        vertical=extra_options['vertical'],
        value=extra_options['value']
    )


components = {'dropdown': dropdown,
              'range_slider': range_slider}

if __name__ == '__main__':
    pass
