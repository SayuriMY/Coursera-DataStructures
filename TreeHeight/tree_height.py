# python3
"""
File name: tree_height.py
Author: Sayuri Monarrez Yesaki
Date created: 01/31/2022
Date last modified: 01/31/2022
Python version: 3.8

Task: You are given a description of a rooted tree. Your task is to compute and output its height. Recall that
the height of a (rooted0 tree is the maximum depth of a node, or the maximum distance from a leaf to the
root. You are given an arbitrary tree, not necessarily a binary tree.

Input: The first line contains the number of nodes n. The second line contains n integer numbers from -1 to n - 1
parent nodes. If the i-th one of them ( 0 <= i <= n - 1 ) is -1, node i is the root, otherwise it's 0-based index of
the parent of i-th node. It is guaranteed that there is exactly one root. It is guaranteed that the input represents
a tree.

Output: the height of the tree

Constraints: 1 <= n <= 10 ^5

Time limit: 3 sec

Memory Limit: 512 MB
"""

import sys
import threading
from typing import Optional

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class Node:
    """
    Constructor of the Node class
    :param 1: data (int) -> node value
    """

    def __init__(self, data: int) -> None:
        self.data = data
        self.children = []


class TreeHeight:
    """
    Constructor of the Tree class

    :param 1: n (int) -> number of nodes
    :param 2: parents (list of int) -> list indicating the parent of each node
    """
    def __init__(self, n: int, parents: list):
        self.n = n
        self.parents = parents
        self.root = self.initialize_tree()

    """
    initialize_tree is a private class that builds a tree based
    on n and parents.
    
    "n" indicates the number of nodes, the value of the nodes go 
    from 0 to n - 1 . For example: n = 5, node values are
    0, 1, 2, 3, 4. 
    
    "parents" list contains the parent node of each node. 
    For example: n = 5 , nodes: 0, 1, 2, 3, 4, parents: 4, -1, 4, 1, 1
    In this example, node 0 is a child of node 4, node 1 is the root, 
    node 2 is a child of node 4, and nodes 3 and 4 are children of node 1.
    nodes:   0  1 2 3 4
    parents: 4 -1 4 1 1
                    1
                  /  \
                 3    4
                     / \
                    0   2
    
    :return: None or Node
    """

    def initialize_tree(self) -> Optional[Node]:
        nodes = []
        # create a Node instance for each node and store it into the nodes list.
        # this gives O(1) access to any node given its label
        for i in range(self.n):
            nodes.append(Node(i))

        root = None
        # iterate over 0 to n - 1 and access each parent's index
        for i in range(self.n):
            # if parent == -1, assign the node as the root.
            if self.parents[i] == -1:
                root = nodes[i]
            else:
                # save nodes[i] as one of the children of the parent[i] node
                # For example:
                # if i = 0, nodes[0] = Node(0), parents[0] = 4 --> nodes[4] = Node(4)
                # save Node(0) as children of parent Node(4)
                nodes[self.parents[i]].children.append(nodes[i])
        return root

    """
    Public compute tree height method.
    height of a (rooted) tree is the maximum depth of a node, or the maximum distance from a leaf
    to the root.
    If the tree root is None, the height of the tree is zero. If the root is not None, it calls
    the private compute_height_helper method to calculate the height.
    
    :return: None if root is None, otherwise, returns height of tree. 
    """

    def compute_height(self) -> int:
        if self.root is None:
            return 0
        return self.compute_height_helper(self.root)

    """
    Private class that recursively computes the height of a tree.
    :return: height of tree. 
    """

    def compute_height_helper(self, node: Node) -> int:
        max_height = 0
        for child in node.children:
            max_height = max(max_height, self.compute_height_helper(child))
        return max_height + 1

    '''
    This solution was provided by the instructors as a naive implementation
    '''

    def compute_height_naive(self) -> int:
        maxHeight = 0
        for vertex in range(self.n):
            height = 0
            i = vertex
            while i != -1:
                height += 1
                i = self.parents[i]
            maxHeight = max(maxHeight, height)
        return maxHeight


def main():
    n = int(sys.stdin.readline())
    parent = list(map(int, sys.stdin.readline().split()))
    tree = TreeHeight(n, parent)
    print(tree.compute_height())


threading.Thread(target=main).start()
