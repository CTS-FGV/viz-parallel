Components Reference

### Dropdown

https://plot.ly/dash/dash-core-components/dropdown

```
  - type: 'dropdown'
    column_name: 'situacao_tipo'
    data_title: 'situacao-perfil'
    menu_text: 'intervalo de tempo'
    options:
      multi: False
      clearable: False
      placeholder: False
      searchable: True
      value: None
```

### Range Slider

https://plot.ly/dash/dash-core-components/rangeslider

```
  - type: 'range_slider'
    column_name: 'dataInicio'
    data_title: 'tempo-numero'
    menu_text: 'intervalo de tempo'
    options:
      aggregation: year
      allowcross: False
      dots: False
      count: 1
      included: True
      marks: None
      max: 10
      min: -5
      step: 0.5
      vertical: False
      value: [-3, 7]
```