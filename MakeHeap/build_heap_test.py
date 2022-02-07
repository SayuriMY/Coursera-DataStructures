import os
from unittest import TestCase
from MakeHeap.build_heap import MinHeap


class Test(TestCase):
    def test_min_heap_case1(self):
        min_heap = MinHeap([5, 4, 3, 2, 1])
        self.assertEqual([1, 2, 3, 5, 4], min_heap.min_heap)
        self.assertEqual(3, len(min_heap.swaps))

    def test_min_heap_case2(self):
        min_heap = MinHeap([1, 2, 3, 4, 5])
        self.assertEqual(0, len(min_heap.swaps))

    def test_min_heap_case3(self):
        lines = []
        with open(os.path.join(os.getcwd(), 'tests', '04'), 'r') as reader:
            lines = reader.readlines()

        n = map(int, lines[0].strip().split())
        input_array = list(map(int, lines[1].strip().split()))

        min_heap = MinHeap(input_array)

        # read answer
        with open(os.path.join(os.getcwd(), 'tests', '04.a'), 'r') as reader:
            lines = reader.readlines()

        self.assertEqual(int(lines[0]), len(min_heap.swaps))

        for i in range(1, len(lines)):
            self.assertEqual(tuple(map(int, lines[i].strip().split())), min_heap.swaps[i - 1])