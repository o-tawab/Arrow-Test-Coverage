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


class TestShift(object):
    def test_1(self, arw):  # BC, ISP (base choice), RACC
        shifted = arw.shift(days=5, months=-2)
        assert str(shifted) == '1995-07-24T13:20:55+00:00'

    def test_2(self, arw):  # ISP (1 kw, all valid, all +ve), RACC
        shifted = arw.shift(weeks=1)
        assert str(shifted) == '1995-09-26T13:20:55+00:00'

    def test_3(self, arw):  # BC, ISP (>1 kw, none valid, some +ve and some -ve), RACC
        with pytest.raises(AttributeError):
            arw.shift(day=-1, tzinfo='local')

    def test_4(self, arw):  # ISP (>1 kw, some valid & some not, some +ve and some -ve), RACC
        with pytest.raises(AttributeError):
            arw.shift(weeks=3, day=-1)

    def test_5(self, arw):  # ISP (empty)
        shifted = arw.shift()
        assert str(shifted) == '1995-09-19T13:20:55+00:00'

    def test_6(self, arw):  # ISP (>1 kw, all valid, all +ve)
        shifted = arw.shift(years=3, months=2)
        assert str(shifted) == '1998-11-19T13:20:55+00:00'

    def test_7(self, arw):  # ISP (>1 kw, all valid, all -ve)
        shifted = arw.shift(years=-3, months=-2)
        assert str(shifted) == '1992-07-19T13:20:55+00:00'

    def test_8(self, arw):  # ISP (>1 kw, all valid, some +ve & some zero)
        shifted = arw.shift(years=3, months=0)
        assert str(shifted) == '1998-09-19T13:20:55+00:00'

    def test_9(self, arw):  # ISP (>1 kw, all valid, some -ve & some zero)
        shifted = arw.shift(years=-3, months=0)
        assert str(shifted) == '1992-09-19T13:20:55+00:00'

    def test_10(self, arw):  # ISP (>1 kw, all valid, some +ve & some -ve & some zero)
        shifted = arw.shift(years=-3, months=0, days=3)
        assert str(shifted) == '1992-09-22T13:20:55+00:00'
