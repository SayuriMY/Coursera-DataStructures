# python3
"""
File name: hash_substring.py
Author: Sayuri Monarrez Yesaki
Date created: 02/24/2022
Date last modified: 02/24/2022
Python version: 3.8

Implement the Rabin-Karp algorithm.

Task: Implement the Rabin-Karp's algorithm for searching the given pattern in the given text.

Input: There are two strings in the input: the pattern P and the text T.

Output: Print all the positions of the occurrences of P in T in the ascending order. Use 0-based indexing of
    positions in the text T.

Constraints: 1 <= |P| <+ |T| <= 5 * 10 ^5. The total length of all occurrences of P in T doesn't exceed 10 ^8.
    The pattern and the text contain only latin letters.

Time limit: 5 sec.

Memory Limit: 512 MB
"""


def read_input():
    return input().rstrip(), input().rstrip()


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    return [
        i
        for i in range(len(text) - len(pattern) + 1)
        if text[i:i + len(pattern)] == pattern
    ]


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
