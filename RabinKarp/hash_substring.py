# python3
"""
File name: hash_substring.py
Author: Sayuri Monarrez Yesaki
Date created: 02/24/2022
Date last modified: 03/02/2022
Python version: 3.8

Implement the Rabin-Karp algorithm.

Task: Implement the Rabin-Karp's algorithm for searching the given pattern in the given text.

Input: There are two strings in the input: the pattern P and the text T.

Output: Print all the positions of the occurrences of P in T in the ascending order. Use 0-based indexing of
    positions in the text T.

Constraints: 1 <= |P| <= |T| <= 5 * 10 ^5. The total length of all occurrences of P in T doesn't exceed 10 ^8.
    The pattern and the text contain only latin letters.

Time limit: 5 sec.

Memory Limit: 512 MB
"""
from collections import deque


def read_input():
    return input().rstrip(), input().rstrip()


def print_occurrences(output: list):
    print(' '.join(map(str, output)))


def get_occurrences(pattern: str, text: str) -> list:
    return [
        i
        for i in range(len(text) - len(pattern) + 1)
        if text[i:i + len(pattern)] == pattern
    ]


''''======================My solution to the problem starts here======================'''


class RabinKarp:
    # 1 and 1000000007 are coprime - their highest common factor is 1, minimising the number of collisions.
    # fixed prime value - select a big p to get a low probability of collision.
    _prime = 100000007
    _x = 1

    """
    Constructor of the RabinKarp class

    :param 1: pattern (str) -> pattern to be searched for in the text
    :param 2: text (str) -> text
    """

    def __init__(self, pattern: str, text: str):
        self.pattern = pattern
        self.text = text
        self.occurrences = []

    """
    Calculate the hash of a string using polynomial hashing.
    :param 1: s (str) -> string to be hashed.
    """

    def _hash_func(self, s: str) -> int:
        len_s = len(s)
        ans = 0
        for i in range(len_s - 1, -1, -1):
            ans = ((ans * self._x + ord(s[i])) % self._prime + self._prime) % self._prime
        return ans

    """
    Precompute all the hash values of the polynomial hash function on the substrings of the text Text with length
    equal to the length of the pattern and with the prime number p and selected constant x.
    
    :param 1: len_p (int) -> length of pattern
    :param 2: len_t (int) -> length of text
    """

    def precompute_hashes(self, len_p: int, len_t: int) -> deque:
        precomputed = deque()  # []

        # last substring of the text
        s = self.text[len_t - len_p:]

        # precompute the hash value for the last substring
        precomputed.append(self._hash_func(s))

        # precompute the value of x to the power of length of the pattern
        y = 1
        for i in range(1, len_p + 1):
            y = ((y * self._x) % self._prime + self._prime) % self._prime

        # Use rolling hash function to calculate the hash of each sliding window in linear time.
        # H = ( x * prev_hash + new_char - x^|pattern| * prev_char ) % prime
        # Go from right to left and compute the hash values of all substrings of the text but the last one
        # since we already know the answer to the last one.
        for i in range(len_t - len_p - 1, -1, -1):
            prec = (((self._x * precomputed[0]) + ord(self.text[i]) -
                     (y * ord(self.text[i + len_p]))) % self._prime + self._prime) % self._prime
            precomputed.appendleft(prec)

        return precomputed

    """
    Search the pattern in the given text and return the positions of occurrences of the pattern.
    """

    def find_occurrences(self) -> list:
        len_p = len(self.pattern)
        len_t = len(self.text)

        # compute the hash of the pattern
        pattern_hash = self._hash_func(self.pattern)

        # precompute the hash values of the substrings of the text with length equal to pattern P
        text_hashes = self.precompute_hashes(len_p, len_t)

        for i in range(len_t - len_p + 1):
            if pattern_hash == text_hashes[i]:
                if self.pattern == self.text[i:i + len_p]:
                    self.occurrences.append(i)

        return self.occurrences


if __name__ == '__main__':
    pattern, text = read_input()
    rk = RabinKarp(pattern, text)
    print_occurrences(rk.find_occurrences())
