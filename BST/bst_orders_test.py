import os
from unittest import TestCase
from BST.bst_orders import TreeOrders


class TestTreeOrders(TestCase):
    def test_in_order_traversal(self):
        tree = TreeOrders()
        tree.n = 5
        tree.key = [4, 2, 5, 1, 3]
        tree.left = [1, 3, -1, -1, -1]
        tree.right = [2, 4, -1, -1, -1]

        result = tree.inOrder()
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_in_order_traversal_1(self):
        tree = TreeOrders()
        tree.n = 10
        tree.key = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
        tree.left = [7, -1, -1, 8, 3, -1, 1, 5, -1, -1]
        tree.right = [2, -1, 6, 9, -1, -1, -1, 4, -1, -1]

        result = tree.inOrder()
        self.assertEqual(result, [50, 70, 80, 30, 90, 40, 0, 20, 10, 60])

    def test_pre_order_traversal(self):
        tree = TreeOrders()
        tree.n = 5
        tree.key = [4, 2, 5, 1, 3]
        tree.left = [1, 3, -1, -1, -1]
        tree.right = [2, 4, -1, -1, -1]

        result = tree.preOrder()
        self.assertEqual(result, [4, 2, 1, 3, 5])

    def test_pre_order_traversal_1(self):
        tree = TreeOrders()
        tree.n = 10
        tree.key = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
        tree.left = [7, -1, -1, 8, 3, -1, 1, 5, -1, -1]
        tree.right = [2, -1, 6, 9, -1, -1, -1, 4, -1, -1]

        result = tree.preOrder()
        self.assertEqual(result, [0, 70, 50, 40, 30, 80, 90, 20, 60, 10])

    def test_post_order_traversal(self):
        tree = TreeOrders()
        tree.n = 5
        tree.key = [4, 2, 5, 1, 3]
        tree.left = [1, 3, -1, -1, -1]
        tree.right = [2, 4, -1, -1, -1]

        result = tree.postOrder()
        self.assertEqual(result, [1, 3, 2, 5, 4])

    def test_post_order_traversal_1(self):
        tree = TreeOrders()
        tree.n = 10
        tree.key = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
        tree.left = [7, -1, -1, 8, 3, -1, 1, 5, -1, -1]
        tree.right = [2, -1, 6, 9, -1, -1, -1, 4, -1, -1]

        result = tree.postOrder()
        self.assertEqual(result, [50, 80, 90, 30, 40, 70, 10, 60, 20, 0])

    def test_bst_orders(self):
        tree = TreeOrders()

        # get all files in test folder.
        test_path = os.path.join(os.getcwd(), 'tests', '21')
        answer_path = os.path.join(os.getcwd(), 'tests', '21.a')

        lines = []
        with open(test_path, 'r') as reader:
            lines = reader.readlines()

        answer = []
        with open(answer_path, 'r') as reader:
            answer = reader.readlines()

        tree.n = int(lines[0].strip())
        tree.key = []
        tree.left = []
        tree.right = []
        for i in range(1, tree.n + 1):
            [key, left, right] = map(int, lines[i].strip().split())
            tree.key.append(key)
            tree.left.append(left)
            tree.right.append(right)

        self.assertEqual(tree.inOrder(), list(map(int, answer[0].strip().split())))
        self.assertEqual(tree.preOrder(), list(map(int, answer[1].strip().split())))
        self.assertEqual(tree.postOrder(), list(map(int, answer[2].strip().split())))
