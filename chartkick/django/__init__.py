from django.utils.html import format_html, json_script, mark_safe
import os
import re
import secrets

__all__ = [
    'LineChart',
    'PieChart',
    'ColumnChart',
    'BarChart',
    'AreaChart',
    'ScatterChart',
    'GeoChart',
    'Timeline'
]


class Chart:
    def __init__(self, type, data, **options):
        # important! check escaping before making configurable
        element_id = 'chart-' + secrets.token_hex(16)
        json_element_id = element_id + '-json'

        height = str(options.pop('height', '300px'))
        width = str(options.pop('width', '100%'))

        for (k, v) in [('height', height), ('width', width)]:
            # limit to alphanumeric and % for simplicity
            # this prevents things like calc() but safety is the priority
            # dot does not need escaped in square brackets
            if not re.match('^[a-zA-Z0-9%.]*$', v):
                raise ValueError('Invalid ' + k)

        html_vars = [
            element_id,
            height,
            width,
            height,
            options.get('loading', 'Loading...')
        ]
        html = format_html("""<div id="{}" style="height: {}; width: {}; text-align: center; color: #999; line-height: {}; font-size: 14px; font-family: 'Lucida Grande', 'Lucida Sans Unicode', Verdana, Arial, Helvetica, sans-serif;">{}</div>""", *html_vars)

        # make sure hash order is preserved in JavaScript
        if isinstance(data, dict):
            data = list(data.items())

        js_vars = {
            'type': type,
            'id': element_id,
            'data': data,
            'options': options
        }
        json = json_script(js_vars, element_id=json_element_id)

        js = """<script>
  (function() {
    var createChart = function() {
      var o = JSON.parse(document.currentScript.previousElementSibling.textContent);
      new Chartkick[o.type](o.id, o.data, o.options);
    };
    if ("Chartkick" in window) {
      createChart();
    } else {
      window.addEventListener("chartkick:load", createChart, true);
    }
  })();
</script>"""

        self.__str = format_html('{}\n{}\n{}', mark_safe(html), json, mark_safe(js))

    def __str__(self):
        return self.__str


class LineChart(Chart):
    def __init__(self, data, **options):
        super().__init__('LineChart', data, **options)


class PieChart(Chart):
    def __init__(self, data, **options):
        super().__init__('PieChart', data, **options)


class ColumnChart(Chart):
    def __init__(self, data, **options):
        super().__init__('ColumnChart', data, **options)


class BarChart(Chart):
    def __init__(self, data, **options):
        super().__init__('BarChart', data, **options)


class AreaChart(Chart):
    def __init__(self, data, **options):
        super().__init__('AreaChart', data, **options)


class ScatterChart(Chart):
    def __init__(self, data, **options):
        super().__init__('ScatterChart', data, **options)


class GeoChart(Chart):
    def __init__(self, data, **options):
        super().__init__('GeoChart', data, **options)


class Timeline(Chart):
    def __init__(self, data, **options):
        super().__init__('Timeline', data, **options)
