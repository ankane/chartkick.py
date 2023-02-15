from flask import Blueprint
from jinja2.utils import htmlsafe_json_dumps
from markupsafe import Markup
import os
import re
import secrets

static_folder = os.path.abspath(__file__ + '/../../django/static/chartkick')
chartkick_blueprint = Blueprint('chartkick', __name__, static_folder=static_folder, static_url_path='/static/chartkick')


class Chart:
    def __init__(self, type, data, **options):
        # important! check escaping before making configurable
        element_id = 'chart-' + secrets.token_hex(16)

        height = str(options.pop('height', '300px'))
        width = str(options.pop('width', '100%'))

        for (k, v) in [('height', height), ('width', width)]:
            # limit to alphanumeric and % for simplicity
            # this prevents things like calc() but safety is the priority
            # dot does not need escaped in square brackets
            if not re.match('^[a-zA-Z0-9%.]*$', v):
                raise ValueError('Invalid ' + k)

        html_vars = {
            'element_id': element_id,
            'height': height,
            'width': width,
            'loading': options.get('loading', 'Loading...')
        }
        html = Markup("""<div id="%(element_id)s" style="height: %(height)s; width: %(width)s; text-align: center; color: #999; line-height: %(height)s; font-size: 14px; font-family: 'Lucida Grande', 'Lucida Sans Unicode', Verdana, Arial, Helvetica, sans-serif;">%(loading)s</div>""") % html_vars

        # make sure hash order is preserved in JavaScript
        if isinstance(data, dict):
            data = list(data.items())

        js_vars = {
            'type': type,
            'id': element_id,
            'data': data,
            'options': options
        }
        js = Markup("""<script>
  (function() {
    var createChart = function() {
      var o = %s;
      new Chartkick[o.type](o.id, o.data, o.options);
    };
    if ("Chartkick" in window) {
      createChart();
    } else {
      window.addEventListener("chartkick:load", createChart, true);
    }
  })();
</script>""") % htmlsafe_json_dumps(js_vars)

        self.__str = html + js

    def __str__(self):
        return self.__str

    def __html__(self):
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
