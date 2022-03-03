import os
from unittest import TestCase

from SubstringEquality.substring_equality import Solver


class TestSolver(TestCase):
    def test_ask(self):
        solver = Solver("trololo")
        self.assertTrue(solver.ask(0, 0, 7))
        self.assertTrue(solver.ask(2, 4, 3))
        self.assertTrue(solver.ask(3, 5, 1))
        self.assertFalse(solver.ask(1, 3, 2))

    def test_ask_1(self):
        solver = Solver("bbbabbabaa")
        self.assertTrue(solver.ask(0, 2, 1))

    def test_ask_2(self):
        solver = Solver("bbbabbabaa")

        # get all files in test folder.
        test_path = os.path.join(os.getcwd(), 'tests', '01')

        with open(test_path, 'r') as reader:
            for line in reader:
                a, b, l = list(map(int, line.strip().split()))
                self.assertEqual(solver.ask(a, b, l), solver.ask_naive(a, b, l))


