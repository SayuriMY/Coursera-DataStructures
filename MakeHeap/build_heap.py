# python3
"""
File name: build_heap.py
Author: Sayuri Monarrez Yesaki
Date created: 02/07/2022
Date last modified: 02/07/2022
Python version: 3.8

Convert an array of integers into a heap. This is the crucial step of the sorting algorithm HeapSort. It has a guaranteed
worst-case running time of O ( n log n) as opposed to QuickSort's average running time of O ( n log n).
QuickSort is usually used in practice, because it is typically it is faster, but HeapSort is used for external sort when
you need to sort huge files that don't fit into memory of your computer.

Task: Convert a given array of integers into a heap. You will do that by applying swaps to the array. Swap is an
operation which exchanges elements ai and aj of the array a for some i and j. You will need to convert the array into a
heap using only O(n) swaps, as described in the lectures. Tip: use a min-heap instead of a max-heap in this problem.

Input: The first line contains a single integer n. The next line contains n space-separated integers ai.

Output: The first line should contain single integer m - the total number of swaps. m must satisfy conditions
0 <- m <- 4n. The next m lines should contain the swap operations used to convert the array a into a heap.
Each swap is described by a pair of integers i, j - the 0-based indices of the elements to be swapped. After applying
all the swaps in the specified order the array must become a heap, that is, for each i where 0 <= i <= n - 1 the
following conditions must be true:
    If 2i + 1 <= n - 1, then ai < a2i+1
    If 2i + 2 ,= n - 1, then ai < a2i+2

All the elements of the input array are distinct
Any sequence of swaps that has length at most 4n and after which your initial array becomes correct heap will
be graded as correct.

Constraints: 1 ≤ 𝑛 ≤ 100 000; 0 ≤ 𝑖, 𝑗 ≤ 𝑛 − 1; 0 ≤ 𝑎0, 𝑎1, . . . , 𝑎𝑛−1 ≤ 109. All 𝑎𝑖 are distinct

Time limit: 3 sec

Memory Limit: 512 MB
"""


class MinHeap:
    """
    Constructor of the MinHeap class
    :param 1: data (list) -> array to be converted into a heap
    """
    def __init__(self, data: list):
        self.min_heap = data
        self.size = len(data)
        self.swaps = []
        self.build_heap()

    """
        Compute the index of the left child of node i of a 0-based array.
    """
    def left_child(self, i: int) -> int:
        return (2 * i) + 1

    """
        Compute the index of the parent of node i of a 0-based array.
    """
    def parent(self, i: int) -> int:
        return (i - 1) // 2

    """
        Compute the index of the right child of node i of a 0-based array.
    """
    def right_child(self, i: int) -> int:
        return (2 * i) + 2

    """
    Swap the problematic nodes with a smaller child until the min heap property
    is satisfied.
    :param 1: i (int) -> index of a node in the heap
    """
    def sift_down(self, i: int):
        min_idx = i
        # compute the index of the left child of i
        left = self.left_child(i)

        # check if i has a left child
        # if the value of the left child is less than the value of the min_idx (current node), change the
        # min_idx to the value of the left child.
        if left < self.size and self.min_heap[left] < self.min_heap[min_idx]:
            min_idx = left

        # compute the index of the right child of i
        right = self.right_child(i)

        # check if it has a right child.
        # if the value of the right child is less than the value of the min_idx, change the min_idx
        # to the value of the left child.
        if right < self.size and self.min_heap[right] < self.min_heap[min_idx]:
            min_idx = right

        # if i is not the smallest among its children, swap the node i with the min_idx
        # save the swapped nodes in the list of swaps
        # call swift down on the new swapped element.
        if i != min_idx:
            self.min_heap[i], self.min_heap[min_idx] = self.min_heap[min_idx], self.min_heap[i]
            self.swaps.append((i, min_idx))
            self.sift_down(min_idx)

    """
    Convert the given array of integers into a min heap. 
    """
    def build_heap(self):
        # iterate over n // 2 elements from back to front.
        # Call sift down method to move the bigger nodes
        # at the bottom of the heap and the smaller nodes
        # to the top.
        for i in range((len(self.min_heap) // 2), -1, -1):
            self.sift_down(i)


"""
This solution was provided by the instructors.
"""


def build_heap_naive(data: list) -> list:
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps


def run_build_min_heap():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    # swaps = build_heap(data)
    min_heap = MinHeap(data)

    print(len(min_heap.swaps))
    for i, j in min_heap.swaps:
        print(i, j)


if __name__ == "__main__":
    run_build_min_heap()
