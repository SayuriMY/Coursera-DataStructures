#!/usr/bin/python3
"""
File name: is_bst.py
Author: Sayuri Monarrez Yesaki
Date created: 03/07/2022
Date last modified: 03/07/2022
Python version: 3.8

Test whether a BST data structure from some programming language library was implemented correctly. There is already
a program that plays with this data structure by inserting, removing, searching integers in the data structure
and outputs the state of the internal binary tree after each operation. Now you need to test whether the given binary
tree is indeed a correct BST. In other words, you want to ensure that you can search for integers in this BST using
binary search through the tree, and you will always get correct result: if the integer is in the tree, you will find it,
otherwise you will not.

Task: You are given a binary tree with integers as its keys. You need to test whether it is a correct BST. The
definition of the BST is the following:
    For any node of the tree, it its key is x, then for any node in its left subtree its jey myst be strictly less than
    x, and for any node in its right subtree its key myst be strictly greater than x.

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

Constraints:  0 ≤ 𝑛 ≤ 105; −2^31 < 𝑘𝑒𝑦𝑖 < 2^31 − 1; −1 ≤ 𝑙𝑒𝑓 𝑡𝑖, 𝑟𝑖𝑔𝑕𝑡𝑖 ≤ 𝑛 − 1. It is guaranteed that the
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


def IsBinarySearchTree(tree: list) -> bool:
    if len(tree) == 0:
        return True
    return is_bst(tree[0][1], -math.inf, tree[0][0], tree) and is_bst(tree[0][2], tree[0][0], math.inf, tree)


def is_bst(idx: int, lower_bound: float, upper_bound: float, tree: list) -> bool:
    if idx == -1:
        return True
    result = lower_bound < tree[idx][0] < upper_bound
    if result:
        return result and is_bst(tree[idx][1], min(lower_bound, tree[idx][0]), min(upper_bound, tree[idx][0]), tree) \
           and is_bst(tree[idx][2], max(lower_bound, tree[idx][0]), max(upper_bound, tree[idx][0]), tree)
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
