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


class TestFloor(object):
    def test_1(self, arw):  # BC, ISP (base choice), RACC, couple-DU
        floor = arw.floor(frame='day')
        assert str(floor) == '1995-09-19T00:00:00+00:00'

    def test_2(self, arw):  # ISP
        floor = arw.floor(frame='hour')
        assert str(floor) == '1995-09-19T13:00:00+00:00'

    def test_3(self, arw):  # ISP
        floor = arw.floor(frame='minute')
        assert str(floor) == '1995-09-19T13:20:00+00:00'

    def test_4(self, arw):  # ISP
        floor = arw.floor(frame='second')
        assert str(floor) == '1995-09-19T13:20:55+00:00'

    def test_5(self, arw):  # BC, ISP, RACC, couple-DU
        floor = arw.floor(frame='week')
        assert str(floor) == '1995-09-18T00:00:00+00:00'

    def test_6(self, arw):  # ISP
        floor = arw.floor(frame='month')
        assert str(floor) == '1995-09-01T00:00:00+00:00'

    def test_7(self, arw):  # BC, ISP, RACC, couple-DU
        floor = arw.floor(frame='quarter')
        assert str(floor) == '1995-07-01T00:00:00+00:00'
