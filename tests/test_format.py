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


class TestFormat(object):
    def test_1(self, arw):  # ISP (base choice)
        assert arw.format(fmt='YYYY-MM-DD#HH:mm:ssZZ') == '1995-09-19#13:20:55+00:00'

    def test_2(self, arw):  # ISP (12 hours)
        assert arw.format(fmt='YYYY.MM.DD-hh:mm:ss') == '1995.09.19-01:20:55'

    def test_3(self, arw):  # ISP (no hours)
        assert arw.format(fmt='YYYY.MM.DD-mm:ss') == '1995.09.19-20:55'

    def test_4(self, arw):  # ISP (no months)
        assert arw.format(fmt='YYYY.DD-hh:mm:ss') == '1995.19-01:20:55'

    def test_5(self, arw):  # ISP (2 digits year)
        assert arw.format(fmt='YY.MM.DD-hh:mm:ss') == '95.09.19-01:20:55'

    def test_6(self, arw):  # ISP (no year)
        assert arw.format(fmt='MM.DD-hh:mm:ss') == '09.19-01:20:55'

    def test_7(self, arw):  # ISP (no day)
        assert arw.format(fmt='YYYY.MM-hh:mm:ss') == '1995.09-01:20:55'

    def test_8(self, arw):  # ISP (no minutes)
        assert arw.format(fmt='YYYY.MM.DD-hh:ss') == '1995.09.19-01:55'

    def test_9(self, arw):  # ISP (no seconds)
        assert arw.format(fmt='YYYY.MM.DD-hh:mm') == '1995.09.19-01:20'

    def test_10(self, arw):  # ISP (spaces separators)
        assert arw.format(fmt='YYYY MM DD hh mm ss') == '1995 09 19 01 20 55'
