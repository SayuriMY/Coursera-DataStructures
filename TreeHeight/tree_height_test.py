from unittest import TestCase
from TreeHeight.tree_height import TreeHeight
import os


def read_test_answer(test_path):
    with open(test_path, 'r') as reader:
        return reader.readline().strip()


def read_test_file(test_path):
    lines = []
    with open(test_path, 'r') as reader:
        lines = reader.readlines()
    return int(lines[0].strip()), list(map(int, lines[1].strip().split()))


class TestTreeHeight(TestCase):
    def test_compute_height(self):
        tree = TreeHeight(5, [4, -1, 4, 1, 1])
        self.assertEqual(tree.compute_height(), 3)

        tree = TreeHeight(5, [-1, 0, 4, 0, 3])
        self.assertEqual(tree.compute_height(), 4)

        tree = TreeHeight(10, [9, 7, 5, 5, 2, 9, 9, 9, 2, -1])
        self.assertEqual(tree.compute_height(), 4)

        tree = TreeHeight(10, [8, 8, 5, 6, 7, 3, 1, 6, -1, 5])
        self.assertEqual(tree.compute_height(), 6)

        # get all files in test folder.
        test_path = os.path.join(os.getcwd(), 'tests')
        test_files = os.listdir(test_path)

        filtered_test_files = [file for file in test_files if not file.endswith('.a')]

        for test in filtered_test_files:
            # read file with problem
            n, parents = read_test_file(os.path.join(test_path, test))

            tree = TreeHeight(n, parents)

            # read answer
            answer = int(read_test_answer(os.path.join(test_path, test + '.a')))

            self.assertEqual(tree.compute_height(), answer)
