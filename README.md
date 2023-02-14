# Chartkick.py

Create beautiful JavaScript charts with one line of Python. No more fighting with charting libraries!

[See it in action](https://chartkick.com/python)

**Chartkick.py 1.0 was recently released** - see [how to upgrade](#upgrading)

[![Build Status](https://github.com/ankane/chartkick.py/workflows/build/badge.svg?branch=master)](https://github.com/ankane/chartkick.py/actions)

## Quick Start

Run:

```sh
pip install chartkick
```

Then follow the instructions for your web framework:

- [Django](#django)

This sets up Chartkick with [Chart.js](https://www.chartjs.org/). For other charting libraries, see [these instructions](#additional-charting-libraries).

### Django

Add to `INSTALLED_APPS` in `settings.py`

```python
INSTALLED_APPS = [
    'chartkick.django',
    # ...
]
```

Load the JavaScript

```django
{% load static %}

<script src="{% static 'chartkick/Chart.bundle.js' %}"></script>
<script src="{% static 'chartkick/chartkick.js' %}"></script>
```

Create a chart in a view

```python
from chartkick.django import PieChart

def index(request):
    chart = PieChart({'Blueberry': 44, 'Strawberry': 23})
    return render(request, 'home/index.html', {'chart': chart})
```

And add it to the template

```django
{{ chart }}
```

## Charts

Line chart

```python
LineChart({'2023-01-01': 11, '2023-01-02': 6})
```

Pie chart

```python
PieChart({'Blueberry': 44, 'Strawberry': 23})
```

Column chart

```python
ColumnChart({'Sun': 32, 'Mon': 46, 'Tue': 28})
```

Bar chart

```python
BarChart({'Work': 32, 'Play': 1492})
```

Area chart

```python
AreaChart({'2021-01-01': 11, '2021-01-02': 6})
```

Scatter chart

```python
ScatterChart([[174.0, 80.0], [176.5, 82.3]], xtitle='Size', ytitle='Population')
```

Geo chart - *Google Charts*

```python
GeoChart({'United States': 44, 'Germany': 23, 'Brazil': 22})
```

Timeline - *Google Charts*

```python
Timeline([['Washington', '1789-04-29', '1797-03-03'], ['Adams', '1797-03-03', '1801-03-03']])
```

Multiple series

```python
data = [
    {'name': 'Workout', 'data': {'2021-01-01': 3, '2021-01-02': 4}},
    {'name': 'Call parents', 'data': {'2021-01-01': 5, '2021-01-02': 3}}
]
LineChart(data)
```

## Data

Data can be a dictionary, list, or URL.

#### Dictionary

```python
LineChart({'2023-01-01': 2, '2023-01-02': 3})
```

#### List

```python
LineChart([['2023-01-01', 2], ['2023-01-02', 3]])
```

#### URL

Make your pages load super fast and stop worrying about timeouts. Give each chart its own endpoint.

```python
LineChart('/charts/tasks')
```

## Options

Width and height

```python
LineChart(data, width='800px', height='500px')
```

Min and max values

```python
LineChart(data, min=1000, max=5000)
```

`min` defaults to 0 for charts with non-negative values. Use `None` to let the charting library decide.

Min and max for x-axis - *Chart.js*

```python
LineChart(data, xmin='2021-01-01', xmax='2022-01-01')
```

Colors

```python
LineChart(data, colors=['#b00', '#666'])
```

Stacked columns or bars

```python
ColumnChart(data, stacked=True)
```

Discrete axis

```python
LineChart(data, discrete=True)
```

Label (for single series)

```python
LineChart(data, label='Value')
```

Axis titles

```python
LineChart(data, xtitle='Time', ytitle='Population')
```

Straight lines between points instead of a curve

```python
LineChart(data, curve=False)
```

Hide points

```python
LineChart(data, points=False)
```

Show or hide legend

```python
LineChart(data, legend=False)
```

Specify legend position

```python
LineChart(data, legend='bottom')
```

Donut chart

```python
PieChart(data, donut=True)
```

Prefix, useful for currency - *Chart.js, Highcharts*

```python
LineChart(data, prefix='$')
```

Suffix, useful for percentages - *Chart.js, Highcharts*

```python
LineChart(data, suffix='%')
```

Set a thousands separator - *Chart.js, Highcharts*

```python
LineChart(data, thousands=',')
```

Set a decimal separator - *Chart.js, Highcharts*

```python
LineChart(data, decimal=',')
```

Set significant digits - *Chart.js, Highcharts*

```python
LineChart(data, precision=3)
```

Set rounding - *Chart.js, Highcharts*

```python
LineChart(data, round=2)
```

Show insignificant zeros, useful for currency - *Chart.js, Highcharts*

```python
LineChart(data, round=2, zeros=True)
```

Friendly byte sizes - *Chart.js*

```python
LineChart(data, bytes=True)
```

Specify the message when data is loading

```python
LineChart(data, loading='Loading...')
```

Specify the message when data is empty

```python
LineChart(data, empty='No data')
```

Refresh data from a remote source every `n` seconds

```python
LineChart(url, refresh=60)
```

You can pass options directly to the charting library with:

```python
LineChart(data, library={'backgroundColor': '#eee'})
```

See the documentation for [Chart.js](https://www.chartjs.org/docs/), [Google Charts](https://developers.google.com/chart/interactive/docs/gallery), and [Highcharts](https://api.highcharts.com/highcharts) for more info.

To customize datasets in Chart.js, use:

```python
LineChart(data, dataset={'borderWidth': 10})
```

You can pass this option to individual series as well.

### Multiple Series

You can pass a few options with a series:

- `name`
- `data`
- `color`
- `dataset` - *Chart.js only*
- `points` - *Chart.js only*
- `curve` - *Chart.js only*

### Code

If you want to use the charting library directly, get the code with:

```python
LineChart(data, code=True)
```

The code will be logged to the JavaScript console. JavaScript functions cannot be logged, so it may not be identical.

### Download Charts

*Chart.js only*

Give users the ability to download charts. It all happens in the browser - no server-side code needed.

```python
LineChart(data, download=True)
```

Safari will open the image in a new window instead of downloading.

Set the filename

```python
LineChart(data, download={'filename': 'boom'})
```

Set the background color

```python
LineChart(data, download={'background': '#ffffff'})
```

Set title

```python
LineChart(data, title='Awesome chart')
```

## Additional Charting Libraries

- [Google Charts](#google-charts)
- [Highcharts](#highcharts)

### Google Charts

Load the JavaScript

```django
{% load static %}

<script src="https://www.gstatic.com/charts/loader.js"></script>
<script src="{% static 'chartkick/chartkick.js' %}"></script>
```

### Highcharts

Download [highcharts.js](https://code.highcharts.com/highcharts.js) and load the JavaScript

```django
{% load static %}

<script src="{% static 'highcharts.js' %}"></script>
<script src="{% static 'chartkick/chartkick.js' %}"></script>
```

### Multiple Libraries

If more than one charting library is loaded, choose between them with:

```python
LineChart(data, adapter='google')  # or highcharts or chartjs
```

## Credits

A big thanks to [Mher Movsisyan](https://github.com/mher) for creating the [initial version](https://github.com/mher/chartkick.py).

## Upgrading

### 1.0

For Django, change `chartkick` to `chartkick.django` under `INSTALLED_APPS` in `settings.py` and remove `chartkick.js()` from `STATICFILES_DIRS`. Then update charts to use classes.

```python
from chartkick.django import LineChart

LineChart({'2023-01-01': 11, '2023-01-02': 6})
```

Flask is not supported yet.

## History

View the [changelog](https://github.com/ankane/chartkick.py/blob/master/CHANGELOG.md)

## Contributing

Everyone is encouraged to help improve this project. Here are a few ways you can help:

- [Report bugs](https://github.com/ankane/chartkick.py/issues)
- Fix bugs and [submit pull requests](https://github.com/ankane/chartkick.py/pulls)
- Write, clarify, or fix documentation
- Suggest or add new features

To get started with development:

```sh
git clone https://github.com/ankane/chartkick.py.git
cd chartkick.py
pip install -r requirements.txt
pytest
```
