import sys

sys.path.append("..")

import pytest
from arrow.arrow import Arrow
from arrow.parser import ParserError
from dateutil import tz

test_config = {
    'initial_date': [1995, 9, 19, 13, 20, 55]  # 1995-09-19T13:20:55+00:00
}


@pytest.fixture
def arw():
    return Arrow(*test_config['initial_date'])


class TestTo(object):
    def test_1(self, arw):  # BC, ISP (base choice), RACC
        time_zoned = arw.to(tz='local')
        assert str(time_zoned) == '1995-09-19T15:20:55+02:00'

    def test_2(self, arw):  # BC, ISP (tz_object, valid), RACC
        time_zoned = arw.to(tz=tz.tzutc())
        assert str(time_zoned) == '1995-09-19T13:20:55+00:00'

    def test_3(self, arw):  # ISP (string, not valid)
        with pytest.raises(ParserError):
            arw.to(tz='locale')
