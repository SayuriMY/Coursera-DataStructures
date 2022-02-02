# python3
"""
File name: max_sliding_window.py
Author: Sayuri Monarrez Yesaki
Date created: 02/02/2022
Date last modified: 02/02/2022
Python version: 3.8

Task: Given a sequence 𝑎1, . . . , 𝑎𝑛 of integers and an integer 𝑚 ≤ 𝑛, find the maximum among {𝑎𝑖
, . . . , 𝑎𝑖+𝑚−1} for every 1 ≤ 𝑖 ≤ 𝑛 − 𝑚 + 1.
A naive 𝑂(𝑛𝑚) algorithm for solving this problem scans each window separately. Your goal is to design an 𝑂(𝑛) algorithm

Input: The first line contains an integer 𝑛, the second line contains 𝑛 integers 𝑎1, . . . , 𝑎𝑛 separated
by spaces, the third line contains an integer 𝑚.

Output: Output max{𝑎𝑖, . . . , 𝑎𝑖+𝑚−1} for every 1 ≤ 𝑖 ≤ 𝑛 − 𝑚 + 1.

Constraints: 1 ≤ 𝑛 ≤ 105, 1 ≤ 𝑚 ≤ 𝑛, 0 ≤ 𝑎𝑖 ≤ 105 for all 1 ≤ 𝑖 ≤ n.

Time limit: 5 sec

Memory Limit: 512 MB
"""

""""
Find the max{ai, ..., ai+m-1} for every 1 <= i <= n - m + 1.
Example:
    m = 4
    sequence = 2    7   3   1   5   2   6   2
               ______________
               2    7   3   1   start_window_idx:0; MAX : 7
                    ______________
                    7   3   1   5   start_window_idx:1; MAX: 7
                        _______________
                        3   1   5   2   start_window_idx:2; MAX: 5
                            _______________
                            1   5   2   6   start_window_idx:3; MAX: 6
                                _________________
                                5   2   6   2   start_window_idx:4; MAX: 6
                                
    The maximums = 7, 7, 5, 6, 6
"""


def max_sliding_window(sequence: list, m: int) -> list:
    # This list will save the indices of the sequence elements inside the current window.
    window_idx = []
    # List of the maximum integers among { ai, ..., ai+m-1}
    maximums = []
    # Index indicating the start of the current window.
    start_window_idx = 0

    for seq_idx in range(len(sequence)):
        # Remove elements indices from window_idx that are not inside the current window.
        while (len(window_idx) > 0) and (window_idx[0] < start_window_idx):
            window_idx.pop(0)

        # Remove the first elements in window_idx that are smaller than the new element being added to the window
        while (len(window_idx) > 0) and sequence[window_idx[0]] < sequence[seq_idx]:
            window_idx.pop(0)

        # Remove the last elements in window_idx that are smaller than the new element being added to the window
        while (len(window_idx) > 0) and sequence[window_idx[len(window_idx) - 1]] < sequence[seq_idx]:
            window_idx.pop()

        window_idx.append(seq_idx)

        if seq_idx >= m - 1:
            maximums.append(sequence[window_idx[0]])
            start_window_idx += 1

    return maximums


"""
This solution was provided by the course instructors.
Running time: O ( mn )
"""


def max_sliding_window_naive(sequence: list, m: int) -> list:
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))

    return maximums


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    # print(*max_sliding_window_naive(input_sequence, window_size))
    print(*max_sliding_window(input_sequence, window_size))
