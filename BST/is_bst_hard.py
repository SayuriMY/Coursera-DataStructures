#!/usr/bin/python3
"""
File name: is_bst_hard.py
Author: Sayuri Monarrez Yesaki
Date created: 03/08/2022
Date last modified: 03/23/2022
Python version: 3.8

Task: You are given a binary tree with integers as its keys. You need to test whether it is a correct BST. The
definition of the BST is the following:
    For any node of the tree, it its key is x, then for any node in its left subtree its key must be strictly less than
    x, and for any node in its right subtree its key must be strictly greater than or EQUAL TO x.

You need to check whether the given binary tree structure satisfies this condition. You are guaranteed that te input
contains a valid binary tree. That is, its is a tree, and each node has at most two children.

Input: The first line contains the number of vertices n. The vertices of the tree are numbered from 0 to n - 1.
Vertex 0 is the root.

The next n lines contain information about vertices 0, 1, ..., n - 1 in order. Each of these lines contains three int
keyi, lefti, and righti
    keyi - key of the i-th vertex
    lefti - index of the left child of the i-th vertex
    righti - index of the right child of the i-th vertex
if i does not have left or right child (or both), the corresponding lefti or righti (or both) will be equal to -1.

Output: If the given binary tree is correct BST, output "CORRECT" w/o quotes. Otherwise, output "INCORRECT".

Constraints:  0 ≤ 𝑛 ≤ 10^5; −2^31 < 𝑘𝑒𝑦𝑖 < 2^31 − 1; −1 ≤ 𝑙𝑒𝑓 𝑡𝑖, 𝑟𝑖𝑔𝑕𝑡𝑖 ≤ 𝑛 − 1. It is guaranteed that the
input represents a valid binary tree. In particular, if 𝑙𝑒𝑓 𝑡𝑖 ̸= −1 and 𝑟𝑖𝑔𝑕𝑡𝑖 ̸= −1, then 𝑙𝑒𝑓 𝑡𝑖 ̸= 𝑟𝑖𝑔𝑕𝑡𝑖.
Also, a vertex cannot be a child of two different vertices. Also, each vertex is a descendant of the root
vertex. All keys in the input will be different.

Time limit: 10 sec.

Memory Limit: 512 MB
"""
import math
import sys
import threading

sys.setrecursionlimit(10 ** 9)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size

"""
Call is_bst function to determine if the given binary tree is a correct BST.
Returns True if the binary tree is a BSt, False otherwise.
"""


def IsBinarySearchTree(tree: list[list[int]]) -> bool:
    if len(tree) == 0:
        return True
    return is_bst(tree[0][1], -math.inf, tree[0][0], tree) and is_bst(tree[0][2], tree[0][0] - 1, math.inf, tree)


"""
Recursively check if each node of the given tree satisfies the BST condition: for any node of the tree, 
if its key is x, then for any node in its left subtree its key must be strictly less than x, and for 
any node in its right subtree its key must be greater than or equal to x.
"""


def is_bst(idx: int, lower_bound: float, upper_bound: float, tree: list[list[int]]) -> bool:
    if idx == -1:
        return True

    # check if the key the current node satisfies the condition of BST.
    result = lower_bound < tree[idx][0] < upper_bound

    if result:
        return result \
               and is_bst(tree[idx][1], lower_bound, min(tree[idx][0], upper_bound), tree) \
               and is_bst(tree[idx][2], tree[idx][0] - 1, upper_bound, tree)
    return result


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()
