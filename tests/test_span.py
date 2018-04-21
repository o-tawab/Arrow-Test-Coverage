import sys

sys.path.append("..")

import pytest
from arrow.arrow import Arrow

test_config = {
    'initial_date': [1995, 9, 19, 13, 20, 55]  # 1995-09-19T13:20:55+00:00
}


@pytest.fixture
def arw():
    return Arrow(*test_config['initial_date'])


class TestSpan(object):
    def test_1(self, arw):  # BC, ISP (base choice), RACC, couple-DU
        span = arw.span(frame='day', count=1)
        assert str(span[0]) == '1995-09-19T00:00:00+00:00'
        assert str(span[1]) == '1995-09-19T23:59:59.999999+00:00'

    def test_2(self, arw):  # ISP
        span = arw.span(frame='hour', count=1)
        assert str(span[0]) == '1995-09-19T13:00:00+00:00'
        assert str(span[1]) == '1995-09-19T13:59:59.999999+00:00'

    def test_3(self, arw):  # ISP
        span = arw.span(frame='minute', count=1)
        assert str(span[0]) == '1995-09-19T13:20:00+00:00'
        assert str(span[1]) == '1995-09-19T13:20:59.999999+00:00'

    def test_4(self, arw):  # ISP
        span = arw.span(frame='second', count=1)
        assert str(span[0]) == '1995-09-19T13:20:55+00:00'
        assert str(span[1]) == '1995-09-19T13:20:55.999999+00:00'

    def test_5(self, arw):  # BC, ISP, RACC, couple-DU
        span = arw.span(frame='week', count=1)
        assert str(span[0]) == '1995-09-18T00:00:00+00:00'
        assert str(span[1]) == '1995-09-24T23:59:59.999999+00:00'

    def test_6(self, arw):  # ISP
        span = arw.span(frame='month', count=1)
        assert str(span[0]) == '1995-09-01T00:00:00+00:00'
        assert str(span[1]) == '1995-09-30T23:59:59.999999+00:00'

    def test_7(self, arw):  # BC, ISP, RACC, couple-DU
        span = arw.span(frame='quarter', count=1)
        assert str(span[0]) == '1995-07-01T00:00:00+00:00'
        assert str(span[1]) == '1995-09-30T23:59:59.999999+00:00'

    def test_8(self, arw):  # ISP
        span = arw.span(frame='day', count=-1)
        assert str(span[0]) == '1995-09-19T00:00:00+00:00'
        assert str(span[1]) == '1995-09-17T23:59:59.999999+00:00'

    def test_9(self, arw):  # ISP
        span = arw.span(frame='day', count=0)
        assert str(span[0]) == '1995-09-19T00:00:00+00:00'
        assert str(span[1]) == '1995-09-18T23:59:59.999999+00:00'

    def test_10(self, arw):  # ISP
        span = arw.span(frame='day', count=5)
        assert str(span[0]) == '1995-09-19T00:00:00+00:00'
        assert str(span[1]) == '1995-09-23T23:59:59.999999+00:00'
