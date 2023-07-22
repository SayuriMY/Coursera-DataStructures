# python3
"""
File name: longest_common_substring.py
Author: Sayuri Monarrez Yesaki
Date created: 03/02/2022
Date last modified: 03/2/2022
Python version: 3.8

In this problem one is given two strings s and t and the goal is to find a string w of maximal length that is a
substring of both s and t. This is a natural measure of similarity between two strings.

The problem can be seen as a special case of the edit distance problem (where only insertions and deletions are
allowed). Hence, it can be solved in time O( |s| * |t|) using dynamic programming. In this problem, your goal is to use
hashing to solve it in almost linear time.

Input: Every line of the input contains two strings s and t consisting of lower case Latin letters.

Output: For each pair of strings s and ti, find its longest common substring and specify it by outputting three
integers: starting position in s, starting position in t, and its length. If there are many such triples with maximal l,
output any of them.

Constraints: The total length of all s's and t's does not exceed 100,000.

Time limit: 15 sec.

Memory Limit: 512 MB
"""

import sys
from collections import namedtuple

Answer = namedtuple('answer_type', 'i j len')


def solve(s, t):
    ans = Answer(0, 0, 0)
    for i in range(len(s)):
        for j in range(len(t)):
            for l in range(min(len(s) - i, len(t) - j) + 1):
                if (l > ans.len) and (s[i:i + l] == t[j:j + l]):
                    ans = Answer(i, j, l)
    return ans


if __name__ == '__main__':
    for line in sys.stdin.readlines():
        s, t = line.split()
        ans = solve(s, t)
        print(ans.i, ans.j, ans.len)
