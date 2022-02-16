# python3
"""
File name: job_queue.py
Author: Sayuri Monarrez Yesaki
Date created: 02/07/2022
Date last modified: 02/10/2022
Python version: 3.8

Simulate a program that processes a list of jobs in parallel. Operating systems have special programs in them called
schedulers which do exactly this with the programs on your computer.

Task: You have a problem which is parallelized and uses n independent threads to process the given list of m jobs.
Threads take jobs in the order they are given in the input. If there is a free thread, it immediately takes the next
job from the list. If a thread has started processing a job, it doesn't interrupt or stop until it finishes
processing the job. If several threads try to take jobs from the list simultaneously, the thread with smaller index
takes the job.
For each job you know exactly how long will it take any thread to process this job, and this time is the same for
all the threads. You need to determine for each job which thread will process it and when will it start processing.

Input: The first line of the input contains integers n and m. n - number of threads.
The second line contains m integers ti - the times in seconds it takes any thread to process i-th job. The times
are given in the same order as they are in the list from which threads take jobs.
Threads are indexed starting form 0.

Output: Output m lines. i-th line should contain two space-separated integers - the0-based index of the thread which
will process the i-th job and the time in seconds when it will start processing that job.

Constraints:  1 ≤ 𝑛 ≤ 10^5 ; 1 ≤ 𝑚 ≤ 10^5 ; 0 ≤ 𝑡𝑖 ≤ 10^9

Time limit: 6 sec.

Memory Limit: 512 MB
"""

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


class Worker:
    """
        Constructor of the Worker class
        :param 1: worker_id (int) -> worker (thread) id.
        :param 2: next_free_time(int) -> time when the worker will be free to start a new job.
    """
    def __init__(self, worker_id: int, next_free_time: int):
        self.id = worker_id
        self.next_free_time = next_free_time

    """
        Assign the time when the worker will be free to start a new job.
    """
    def assign_next_free_time(self, time: int):
        self.next_free_time = time


class MinHeap:
    """
        Constructor of the MinHeap class
        :param 1: num_threads (int) -> number of threads
    """

    def __init__(self, num_threads: int):
        self.size = num_threads
        self.min_heap = []
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
        if left < self.size and ((self.min_heap[left].next_free_time < self.min_heap[min_idx].next_free_time) or
                                 ((self.min_heap[left].next_free_time == self.min_heap[min_idx].next_free_time) and
                                  self.min_heap[left].id < self.min_heap[min_idx].id)):
            min_idx = left

        # compute the index of the right child of i
        right = self.right_child(i)

        # check if it has a right child.
        # if the value of the right child is less than the value of the min_idx, change the min_idx
        # to the value of the left child.
        if right < self.size and ((self.min_heap[right].next_free_time < self.min_heap[min_idx].next_free_time) or
                                  (self.min_heap[right].next_free_time == self.min_heap[min_idx].next_free_time and
                                   self.min_heap[right].id < self.min_heap[min_idx].id)):
            min_idx = right

        # if i is not the smallest among its children, swap the node i with the min_idx
        # save the swapped nodes in the list of swaps
        # call swift down on the new swapped element.
        if i != min_idx:
            self.min_heap[i], self.min_heap[min_idx] = self.min_heap[min_idx], self.min_heap[i]
            self.sift_down(min_idx)

    """
        Build heap based on the number of threads or workers.
    """

    def build_heap(self):
        for i in range(self.size):
            self.min_heap.append(Worker(i, 0))

    """
        Return the worker that will be available to start a new job sooner.
    """

    def get_next_free_worker(self) -> Worker:
        return self.min_heap[0]

    """
        Update the next free time of a worker and call sift_down method to 
        move the worker down the heap.
    """

    def update_next_free_time_of_root(self, heap_pos: int, next_free_time: int):
        self.min_heap[heap_pos].next_free_time = next_free_time

        self.sift_down(heap_pos)


def assign_jobs(n_workers: int, jobs: list) -> list:
    result = []
    min_heap = MinHeap(n_workers)

    for job in jobs:
        next_worker = min_heap.get_next_free_worker()
        result.append(AssignedJob(next_worker.id, next_worker.next_free_time))
        min_heap.update_next_free_time_of_root(0, job + next_worker.next_free_time)

    return result


"""
This solution was provided by instructors
Running time: O ( n ^2 )
"""


def assign_jobs_naive(n_workers: int, jobs: list) -> list:
    result = []
    next_free_time = [0] * n_workers
    for job in jobs:
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job

    return result


def run_assign_jobs():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    run_assign_jobs()
