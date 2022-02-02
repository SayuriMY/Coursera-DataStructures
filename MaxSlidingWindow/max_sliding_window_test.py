from unittest import TestCase
from MaxSlidingWindow.max_sliding_window import max_sliding_window


class Test(TestCase):
    def test_max_sliding_window(self):
        input_sequence = [2, 7, 3, 1, 5, 2, 6, 2]
        m = 4
        self.assertEqual(max_sliding_window(input_sequence, m), [7, 7, 5, 6, 6])

