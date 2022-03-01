# python3
"""
File name: substring_equality.py
Author: Sayuri Monarrez Yesaki
Date created: 02/28/2022
Date last modified: 03/1/2022
Python version: 3.8

In this problem you will use hashing to design an algorithm that is able to preprocess a given string s to answer any
query of the form "are these two substrings of s equal?" efficiently. This, in turn, is a basic building block in many
string processing algorithms.

Input: The first line contains a string s consisting of small Latin letters. The second line contains the number of
queries q. Each of the next q lines specifies a query by three integers a, b, and l.

Output: For each query, output “Yes” if 𝑠𝑎𝑠𝑎+1. . .𝑠𝑎+𝑙−1 = 𝑠𝑏𝑠𝑏+1. . .𝑠𝑏+𝑙−1 are equal, and “No”
otherwise.

Constraints: 1 ≤ |𝑠| ≤ 500 000. 1 ≤ 𝑞 ≤ 100 000. 0 ≤ 𝑎, 𝑏 ≤ |𝑠| − 𝑙 (hence the indices 𝑎 and 𝑏 are 0-based).

Time limit: 10 sec.

Memory Limit: 512 MB
"""

import sys


class Solver:
    def __init__(self, s):
        self.s = s

    def ask(self, a, b, l):
        return s[a:a + l] == s[b:b + l]


s = sys.stdin.readline()
q = int(sys.stdin.readline())
solver = Solver(s)
for i in range(q):
    a, b, l = map(int, sys.stdin.readline().split())
    print("Yes" if solver.ask(a, b, l) else "No")
