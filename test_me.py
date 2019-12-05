from unittest import TestCase
from bifurcate import bifurcate_crab
import time


class TestIcleHelper(TestCase):
    def test_i_have_no_algebra(self):
        assert 1 == 1

    def test_bifurcate(self):
        assert bifurcate_crab()
