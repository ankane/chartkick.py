from chartkick.django import LineChart, PieChart, ColumnChart, BarChart, AreaChart, ScatterChart, GeoChart, Timeline
import pytest


class TestDjango:
    def test_line_chart(self):
        self.assert_chart(LineChart([]))

    def test_pie_chart(self):
        self.assert_chart(PieChart([]))

    def test_column_chart(self):
        self.assert_chart(ColumnChart([]))

    def test_bar_chart(self):
        self.assert_chart(BarChart([]))

    def test_area_chart(self):
        self.assert_chart(AreaChart([]))

    def test_scatter_chart(self):
        self.assert_chart(ScatterChart([]))

    def test_geo_chart(self):
        self.assert_chart(GeoChart([]))

    def test_timeline(self):
        self.assert_chart(Timeline([]))

    def test_escape_data(self):
        chart = LineChart('</script><script>alert("xss")</script>')
        assert '\\u003Cscript\\u003E' in str(chart)
        assert '<script>alert' not in str(chart)

    def test_escape_options(self):
        chart = LineChart([], xss='</script><script>alert("xss")</script>')
        assert '\\u003Cscript\\u003E' in str(chart)
        assert '<script>alert' not in str(chart)

    def test_height_pixels(self):
        assert 'height: 100px;' in str(LineChart([], height='100px'))

    def test_height_percent(self):
        assert 'height: 100%;' in str(LineChart([], height='100%'))

    def test_height_dot(self):
        assert 'height: 2.5rem;' in str(LineChart([], height='2.5rem'))

    def test_height_quote(self):
        with pytest.raises(ValueError) as excinfo:
            LineChart([], height='150px"')
        assert 'Invalid height' in str(excinfo.value)

    def test_height_semicolon(self):
        with pytest.raises(ValueError) as excinfo:
            LineChart([], height='150px;background:123')
        assert 'Invalid height' in str(excinfo.value)

    def test_width_pixels(self):
        assert 'width: 100px;' in str(LineChart([], width='100px'))

    def test_width_percent(self):
        assert 'width: 100%;' in str(LineChart([], width='100%'))

    def test_width_dot(self):
        assert 'width: 2.5rem;' in str(LineChart([], width='2.5rem'))

    def test_width_quote(self):
        with pytest.raises(ValueError) as excinfo:
            LineChart([], width='80%"')
        assert 'Invalid width' in str(excinfo.value)

    def test_width_semicolon(self):
        with pytest.raises(ValueError) as excinfo:
            LineChart([], width='80%;background:123')
        assert 'Invalid width' in str(excinfo.value)

    def test_loading(self):
        assert '>Loading!!</div>' in str(LineChart([], loading='Loading!!'))

    def test_loading_escaped(self):
        assert '&lt;b&gt;Loading!!&lt;/b&gt;' in str(LineChart([], loading='<b>Loading!!</b>'))
        assert '<b>' not in str(LineChart([], loading='<b>Loading!!</b>'))

    def assert_chart(self, chart):
        assert 'new Chartkick' in str(chart)
