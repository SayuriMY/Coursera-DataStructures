import os
from unittest import TestCase
from HashChains.hash_chains import QueryProcessor, Query


class TestQueryProcessor(TestCase):
    def test_process_queries(self):
        queries = [
            Query("add world".split()),
            Query("add HellO".split()),
            Query("check 4".split()),
            Query("find World".split()),
            Query("find world".split()),
            Query("del world".split()),
            Query("check 4".split()),
            Query("del HellO".split()),
            Query("add luck".split()),
            Query("add GooD".split()),
            Query("check 2".split()),
            Query("del good".split())
        ]

        proc = QueryProcessor(5)
        result = proc.process_queries_chaining(queries)

        expected = ["HellO world", "no", "yes", "HellO", "GooD luck"]
        for i in range(len(result)):
            self.assertEqual(result[i], expected[i])

    def test_process_queries_2(self):
        queries = [
            Query("add test".split()),
            Query("add test".split()),
            Query("find test".split()),
            Query("del test".split()),
            Query("find test".split()),
            Query("find test".split()),
            Query("add Test".split()),
            Query("find Test".split())
        ]

        proc = QueryProcessor(4)
        result = proc.process_queries_chaining(queries)

        expected = ["yes", "no", "no", "yes"]
        for i in range(len(result)):
            self.assertEqual(result[i], expected[i])

    def test_process_queries_3(self):
        queries = [
            Query("check 0".split()),
            Query("find help".split()),
            Query("add help".split()),
            Query("add del".split()),
            Query("add add".split()),
            Query("find add".split()),
            Query("find del".split()),
            Query("del del".split()),
            Query("find del".split()),
            Query("check 0".split()),
            Query("check 1".split()),
            Query("check 2".split())
        ]

        proc = QueryProcessor(3)
        result = proc.process_queries_chaining(queries)

        expected = ["", "no", "yes", "yes", "no", "", "add help", ""]
        for i in range(len(result)):
            self.assertEqual(result[i], expected[i])

    def test_process_queries_4(self):
        lines = []
        with open(os.path.join(os.getcwd(), 'tests', '06'), 'r') as reader:
            lines = reader.readlines()

        m = int(lines[0])
        proc = QueryProcessor(m)
        num_queries = int(lines[1])
        queries = []
        for i in range(2, num_queries + 2):
            queries.append(Query(lines[i].split()))

        result = proc.process_queries_chaining(queries)

        # read answer
        with open(os.path.join(os.getcwd(), 'tests', '06.a'), 'r') as reader:
            lines = reader.readlines()

        for i in range(len(lines)):
            self.assertEqual(lines[i].strip(), result[i])
