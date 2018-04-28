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


class TestHumanize(object):
    def test_1(self, arw):  # BC, RACC,
        assert arw.humanize() == '22 years ago'
