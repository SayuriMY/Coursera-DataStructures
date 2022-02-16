import os
from unittest import TestCase
from MergingTables.merging_tables import Database


class TestDatabase(TestCase):
    def test_merge_1(self):
        db = Database([1, 1, 1, 1, 1])
        queries = [(3, 5), (2, 4), (1, 4), (5, 4), (5, 3)]
        result = []
        for i in range(len(queries)):
            dst, src = queries[i][0], queries[i][1]
            db.merge(dst - 1, src - 1)
            result.append(db.max_row_count)

        self.assertEqual([2, 2, 3, 5, 5], result)

    def test_merge_2(self):
        db = Database([10, 0, 5, 0, 3, 3])
        queries = [(6, 6), (6, 5), (5, 4), (4, 3)]
        result = []
        for i in range(len(queries)):
            dst, src = queries[i][0], queries[i][1]
            db.merge(dst - 1, src - 1)
            result.append(db.max_row_count)

        self.assertEqual([10, 10, 10, 11], result)

    def test_merge_3(self):
        lines = []
        with open(os.path.join(os.getcwd(), 'tests', '116'), 'r') as reader:
            lines = reader.readlines()

        n_tables, n_queries = map(int, lines[0].strip().split())
        counts = list(map(int, lines[1].strip().split()))

        db = Database(counts)
        result = []
        for i in range(2, len(lines)):
            query = list(map(int, lines[i].strip().split()))
            dst, src = query[0], query[1]
            db.merge(dst - 1, src - 1)
            result.append(db.max_row_count)

        # read answer
        with open(os.path.join(os.getcwd(), 'tests', '116.a'), 'r') as reader:
            lines = reader.readlines()

        for i in range(len(lines)):
            expected = int(lines[i].strip())
            self.assertEqual(result[i], expected)