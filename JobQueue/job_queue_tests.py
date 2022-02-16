import os
from unittest import TestCase
from JobQueue.job_queue import assign_jobs


class Test(TestCase):
    def test_assign_jobs_1(self):
        assigned_jobs = assign_jobs(2, [1, 2, 3, 4, 5])
        result = [(0, 0), (1, 0), (0, 1), (1, 2), (0, 4)]

        for i in range(len(assigned_jobs)):
            self.assertEqual(assigned_jobs[i].worker, result[i][0])
            self.assertEqual(assigned_jobs[i].started_at, result[i][1])

    def test_assign_jobs_2(self):
        assigned_jobs = assign_jobs(4, [1] * 20)
        result = [(0, 0), (1,  0), (2, 0), (3, 0), (0, 1), (1,  1), (2, 1), (3, 1), (0, 2), (1,  2), (2, 2), (3, 2),
                  (0, 3), (1,  3), (2, 3), (3, 3), (0, 4), (1,  4), (2, 4), (3, 4)]

        for i in range(len(assigned_jobs)):
            self.assertEqual(assigned_jobs[i].worker, result[i][0])
            self.assertEqual(assigned_jobs[i].started_at, result[i][1])

    def test_assign_jobs_3(self):
        lines = []
        with open(os.path.join(os.getcwd(), 'tests', '02'), 'r') as reader:
            lines = reader.readlines()

        threads, jobs = map(int, lines[0].strip().split())
        times = list(map(int, lines[1].strip().split()))

        assigned_jobs = assign_jobs(threads, times)

        # read answer
        with open(os.path.join(os.getcwd(), 'tests', '02.a'), 'r') as reader:
            lines = reader.readlines()

        for i in range(len(lines)):
            result = list(map(int, lines[i].strip().split()))
            self.assertEqual(assigned_jobs[i].worker, result[0])
            self.assertEqual(assigned_jobs[i].started_at, result[1])

    def test_assign_jobs_4(self):
        lines = []
        with open(os.path.join(os.getcwd(), 'tests', '08'), 'r') as reader:
            lines = reader.readlines()

        threads, jobs = map(int, lines[0].strip().split())
        times = list(map(int, lines[1].strip().split()))

        assigned_jobs = assign_jobs(threads, times)

        # read answer
        with open(os.path.join(os.getcwd(), 'tests', '08.a'), 'r') as reader:
            lines = reader.readlines()

        for i in range(len(lines)):
            result = list(map(int, lines[i].strip().split()))
            self.assertEqual(assigned_jobs[i].worker, result[0])
            self.assertEqual(assigned_jobs[i].started_at, result[1])
