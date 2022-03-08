# python3
"""
File name: bst_orders.py
Author: Sayuri Monarrez Yesaki
Date created: 03/07/2022
Date last modified: 03/7/2022
Python version: 3.8

Implement in-order, pre-order, and post-order traversals of a binary tree. These traversals were defined in week 1
lecture on tree traversals.

Task: Your are given a rooted binary tree. Build and output its in-order, pre-order and post-order traversals.

Input: The first line contains the number of vertices n. The vertices of the tree are numbered from o to n-1. Vertex is
the root. The next n lines contain information about the vertices 0, 1, ..., n - 1 in order. Each of these lines
contains three integers keyi, lefti, and righti -
    keyi - key of the i-th vertex
    lefti - index of the left child of the i-th vertex
    righti - index of the right child of the i-th vertex
if i does not have left or right child (or both), the corresponding lefti or righti (or both) will be equal to -1.

Output: Print three lines. The first line should contain the keys of the vertices in the in-order traversal of the tree.
The second line should contain the keys of the vertices in the pre-order traversal of the tree. The third line
should contain the keys of the vertices in the post-order traversal fo the tree.

Constraints: 1 ≤ 𝑛 ≤ 105; 0 ≤ 𝑘𝑒𝑦𝑖 ≤ 109; −1 ≤ 𝑙𝑒𝑓 𝑡𝑖, 𝑟𝑖𝑔𝑕𝑡𝑖 ≤ 𝑛 − 1. It is guaranteed that the input
represents a valid binary tree. In particular, if 𝑙𝑒𝑓 𝑡𝑖 ̸= −1 and 𝑟𝑖𝑔𝑕𝑡𝑖 ̸= −1, then 𝑙𝑒𝑓 𝑡𝑖 ̸= 𝑟𝑖𝑔𝑕𝑡𝑖. Also,
a vertex cannot be a child of two different vertices. Also, each vertex is a descendant of the root vertex.

Time limit: 6 sec.

Memory Limit: 512 MB
"""

import sys, threading

sys.setrecursionlimit(10 ** 9 )  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeOrders:
    """"
    This function was provided by the instructors.
    """
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        # contain the idx of the left child of the i-th node
        self.left = [0 for i in range(self.n)]
        # contain the idx of the right child of the i-th node
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    """
    Call in_order_traversal to traverse the tree and save the node key
     as follows: left, root, right.
    """
    def inOrder(self) -> list:
        self.result = []
        self.in_order_traversal(0, self.result)
        return self.result

    """
    Recursive algorithm to traverse the nodes of a tree and append the keys
    in left, root, right order.
    """
    def in_order_traversal(self, idx: int, result_list: list):
        if idx == -1:
            return
        self.in_order_traversal(self.left[idx], result_list)
        result_list.append(self.key[idx])
        self.in_order_traversal(self.right[idx], result_list)

    """
    Call pre_order_traversal to traverse the tree and save the node key
     as follows: root, left, right.
    """
    def preOrder(self) -> list:
        self.result = []
        self.pre_order_traversal(0, self.result)
        return self.result

    """
    Recursive algorithm to traverse the nodes of a tree and append the keys
    in root, left, right order.
    """
    def pre_order_traversal(self, idx: int, result_list: list):
        if idx == -1:
            return
        result_list.append(self.key[idx])
        self.pre_order_traversal(self.left[idx], result_list)
        self.pre_order_traversal(self.right[idx], result_list)

    """
    Call post_order_traversal to traverse the tree and save the node key
     as follows: left, right, root.
    """
    def postOrder(self) -> list:
        self.result = []
        self.post_order_traversal(0, self.result)
        return self.result

    """
    Recursive algorithm to traverse the nodes of a tree and append the keys
    in left, right, root order.
    """
    def post_order_traversal(self, idx: int, result_list: list):
        if idx == -1:
            return
        self.post_order_traversal(self.left[idx], result_list)
        self.post_order_traversal(self.right[idx], result_list)
        result_list.append(self.key[idx])


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))


threading.Thread(target=main).start()
