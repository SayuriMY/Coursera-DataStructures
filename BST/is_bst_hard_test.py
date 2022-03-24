from unittest import TestCase
from BST.is_bst_hard import IsBinarySearchTree


class Test(TestCase):
    def test_is_binary_search_tree(self):
        tree = [[2, 1, 2], [1, -1, -1], [3, -1, -1]]
        self.assertTrue(IsBinarySearchTree(tree))

    def test_is_binary_search_tree_1(self):
        tree = [[1, 1, 2], [2, -1, -1], [3, -1, -1]]
        self.assertFalse(IsBinarySearchTree(tree))

    def test_is_binary_search_tree_2(self):
        tree = []
        self.assertTrue(IsBinarySearchTree(tree))

    def test_is_binary_search_tree_3(self):
        tree = [[2, 1, 2], [1, -1, -1], [2, -1, -1]]
        self.assertTrue(IsBinarySearchTree(tree))

    def test_is_binary_search_tree_4(self):
        tree = [[2, 1, 2], [2, -1, -1], [3, -1, -1]]
        self.assertFalse(IsBinarySearchTree(tree))

    def test_is_binary_search_tree_5(self):
        tree = [[2147483647, -1, -1]]
        self.assertTrue(IsBinarySearchTree(tree))

    def test_is_binary_search_tree_6(self):
        tree = [[1, -1, 1], [2, -1, 2], [3, -1, 3], [4, -1, 4], [5, -1, -1]]
        self.assertTrue(IsBinarySearchTree(tree))

    def test_is_binary_search_tree_7(self):
        tree = [[4, 1, 2], [2, 3, 4], [6, 5, 6], [1, -1, -1], [3, -1, -1], [5, -1, -1], [7, -1, -1]]
        self.assertTrue(IsBinarySearchTree(tree))

    def test_is_binary_search_tree_8(self):
        tree = [[2, 1, 2], [1, -1, 3], [3, -1, -1], [2, -1, -1]]
        self.assertFalse(IsBinarySearchTree(tree))

    def test_is_binary_search_tree_9(self):
        tree = [[2, 1, 2], [1, -1, -1], [3, 3, -1], [3, -1, -1]]
        self.assertFalse(IsBinarySearchTree(tree))

    def test_is_binary_search_tree_10(self):
        tree = [[10, 1, 2], [9, 3, 4], [11, -1, -1], [8, -1, -1], [9, 5, -1], [8, -1, -1]]
        self.assertFalse(IsBinarySearchTree(tree))
