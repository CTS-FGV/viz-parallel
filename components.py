import dash_core_components as dcc
import dash_html_components as html

def dropdown(**kwargs):

    kwargs = kwargs['kwargs']

    id = kwargs['id']
    className = kwargs['className']
    column_name = kwargs['column_name']
    back_name = kwargs['back_name']
    data_title = kwargs['data_title']
    extra_options = kwargs['extra_options']


    options = [
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ]

    return dcc.Dropdown(
        id=id,
        className=className,
        options=options,
        multi=extra_options['multi'],
        clearable=extra_options['clearable'],
        placeholder=extra_options['placeholder'],
        searchable=extra_options['searchable'],
        value=extra_options['value'])



def range_slider(**kwargs):

    kwargs = kwargs['kwargs']

    id = kwargs['id']
    className = kwargs['className']
    column_name = kwargs['column_name']
    back_name = kwargs['back_name']
    data_title = kwargs['data_title']
    extra_options = kwargs['extra_options']

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
        value=extra_options['value'],)



components = {'dropdown': dropdown,
              'range_slider': range_slider}

if __name__ == '__main__':
    pass