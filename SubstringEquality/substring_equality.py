# python3
"""
File name: substring_equality.py
Author: Sayuri Monarrez Yesaki
Date created: 02/28/2022
Date last modified: 03/03/2022
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
    _m1 = 1000000007
    _m2 = 1000000009
    _x = 31

    """
    Constructor of the Solver class

    :param 1: pattern (str) -> string
    """

    def __init__(self, s: str):
        self.text = s
        self.hash_m1 = self.precompute_hashes(self._m1)
        self.hash_m2 = self.precompute_hashes(self._m2)

    """
    Precompute all the hash values of all prefixes of text using a polynomial hash function 

    :param 1: m (int) -> value of prime
    """

    def precompute_hashes(self, m: int) -> list:
        len_t = len(self.text)
        precomputed = [0] * len_t

        # Go from left to right and compute the hash values of all prefixes of the text
        precomputed[0] = ord(self.text[0])
        for i in range(1, len_t):
            precomputed[i] = ((self._x * precomputed[i - 1]) + ord(self.text[i])) % m

        return precomputed

    """
    This naive implementation was provided by the instructors.
    """

    def ask_naive(self, a: int, b: int, l: int) -> bool:
        return self.text[a:a + l] == self.text[b:b + l]

    """
    Compute the hash value of a substring of text based on the following formula:
            H = h[start + length] - (x ** length ) * h[start]
            
        when the start position of the substring is zero, there is no need to subtract 
        (x ** length ) * h[start].

    :param 1: start (int) -> start of substring
    :param 1: length (int) -> length of the substring
    :param 1: precomputed_hashes (list) -> list with hashes of all text prefixes
    :param 1: m (int) -> value of prime
    """

    def compute_hash(self, start: int, length: int, precomputed_hashes: list, m: int) -> int:
        if start == 0:
            return precomputed_hashes[start + length - 1]
        return precomputed_hashes[start + length - 1] - pow(self._x, length, m) * precomputed_hashes[start - 1]

    """
   Check if the two substrings ( text[ a : a + l ] and text [ b : b + l ] ) of text equal
   by using hashing.

   :param 1: a (int) -> start of substring 1
   :param 1: b (int) -> start of substring 2
   :param 1: l (int) -> length of substrings
   """

    def ask(self, a: int, b: int, l: int) -> bool:

        # calculate the hash values of the two substrings using prime m1
        hash_a = self.compute_hash(a, l, self.hash_m1, self._m1) % self._m1
        hash_b = self.compute_hash(b, l, self.hash_m1, self._m1) % self._m1

        if hash_a == hash_b:
            # calculate the hash values of the two substrings using prime m2
            hash_a = self.compute_hash(a, l, self.hash_m2, self._m2) % self._m2
            hash_b = self.compute_hash(b, l, self.hash_m2, self._m2) % self._m2

            if hash_a == hash_b:
                return True
        return False


if __name__ == '__main__':
    s = sys.stdin.readline()
    q = int(sys.stdin.readline())
    solver = Solver(s)
    for i in range(q):
        a, b, l = map(int, sys.stdin.readline().split())
        print("Yes" if solver.ask(a, b, l) else "No")
