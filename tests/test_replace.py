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


class TestReplace(object):
    def test_1(self, arw):  # BC, ISP (base choice), RACC
        replaced = arw.replace(day=5, month=10)
        assert str(replaced) == '1995-10-05T13:20:55+00:00'

    def test_2(self, arw):  # BC, ISP (>1 kw, all valid, all larger), RACC
        replaced = arw.replace(day=20, month=10, tzinfo='utc')
        assert str(replaced) == '1995-10-20T13:20:55+00:00'

    def test_3(self, arw):  # BC, ISP (>1 kw, none valid, some smaller & some larger), RACC
        with pytest.raises(AttributeError):
            arw.replace(week=3, moon_year=3)

    def test_4(self, arw):  # BC, ISP (>1 kw, some valid, some smaller & some larger), RACC
        with pytest.raises(AttributeError):
            arw.replace(day=5, light_year=3)

    def test_5(self, arw):  # ISP (empty, all valid, some smaller & some larger)
        replaced = arw.replace()
        assert str(replaced) == '1995-09-19T13:20:55+00:00'

    def test_6(self, arw):  # ISP (one kw, all valid, all smaller)
        replaced = arw.replace(day=5)
        assert str(replaced) == '1995-09-05T13:20:55+00:00'

    def test_7(self, arw):  # BC, ISP (>1 kw, all valid, all smaller)
        replaced = arw.replace(day=5, month=5)
        assert str(replaced) == '1995-05-05T13:20:55+00:00'

    def test_8(self, arw):  # BC, ISP (>1 kw, all valid, all equal)
        replaced = arw.replace(day=19, month=9)
        assert str(replaced) == '1995-09-19T13:20:55+00:00'

    def test_9(self, arw):  # ISP (empty, all valid, some smaller & some equal)
        replaced = arw.replace(day=19, month=5)
        assert str(replaced) == '1995-05-19T13:20:55+00:00'

    def test_10(self, arw):  # ISP (empty, all valid, some equal & some larger)
        replaced = arw.replace(day=19, month=10)
        assert str(replaced) == '1995-10-19T13:20:55+00:00'

    def test_11(self, arw):  # ISP (empty, all valid, some smaller & some larger & some equal)
        replaced = arw.replace(day=20, month=5, year=1995)
        assert str(replaced) == '1995-05-20T13:20:55+00:00'
