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


class TestCeil(object):
    def test_1(self, arw):  # BC, ISP (base choice), RACC, couple-DU
        ceil = arw.ceil(frame='day')
        assert str(ceil) == '1995-09-19T23:59:59.999999+00:00'

    def test_2(self, arw):  # ISP
        ceil = arw.ceil(frame='hour')
        assert str(ceil) == '1995-09-19T13:59:59.999999+00:00'

    def test_3(self, arw):  # ISP
        ceil = arw.ceil(frame='minute')
        assert str(ceil) == '1995-09-19T13:20:59.999999+00:00'

    def test_4(self, arw):  # ISP
        ceil = arw.ceil(frame='second')
        assert str(ceil) == '1995-09-19T13:20:55.999999+00:00'

    def test_5(self, arw):  # BC, ISP, RACC, couple-DU
        ceil = arw.ceil(frame='week')
        assert str(ceil) == '1995-09-24T23:59:59.999999+00:00'

    def test_6(self, arw):  # ISP
        ceil = arw.ceil(frame='month')
        assert str(ceil) == '1995-09-30T23:59:59.999999+00:00'

    def test_7(self, arw):  # BC, ISP, RACC, couple-DU
        ceil = arw.ceil(frame='quarter')
        assert str(ceil) == '1995-09-30T23:59:59.999999+00:00'
