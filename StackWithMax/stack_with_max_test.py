from unittest import TestCase
from StackWithMax.stack_with_max import StackWithMax


class TestStackWithMax(TestCase):
    def test_case1(self):
        stack = StackWithMax()
        stack.push(2)
        stack.push(1)
        self.assertEqual(stack.max(), 2)
        stack.pop()
        self.assertEqual(stack.max(), 2)

    def test_case2(self):
        stack = StackWithMax()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.max(), 2)
        stack.pop()
        self.assertEqual(stack.max(), 1)

    def test_case3(self):
        stack = StackWithMax()
        stack.push(2)
        stack.push(3)
        stack.push(9)
        stack.push(7)
        stack.push(2)
        self.assertEqual(stack.max(), 9)
        self.assertEqual(stack.max(), 9)
        self.assertEqual(stack.max(), 9)
        stack.pop()
        self.assertEqual(stack.max(), 9)

    def test_case5(self):
        stack = StackWithMax()
        stack.push(7)
        stack.push(1)
        stack.push(7)
        self.assertEqual(stack.max(), 7)
        stack.pop()
        self.assertEqual(stack.max(), 7)
