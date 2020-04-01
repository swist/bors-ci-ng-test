from unittest import TestCase
from bifurcate import bifurcate
import time


class TestIcleHelper(TestCase):
    def test_i_have_no_algebra(self):
        assert 1 == 1

    def test_bifurcate(self):
        assert bifurcate()

    def test_that_takes_some_time(self):
        time.sleep(1 * 60)  # sleep one minute
        assert True
