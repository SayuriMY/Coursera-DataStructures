from unittest import TestCase
from main import flippingMatrix


class Test(TestCase):
    def test_flipping_matrix(self):
        flippingMatrix([[1, 2], [3, 4]])
