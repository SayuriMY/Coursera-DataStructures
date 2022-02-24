from unittest import TestCase
from PhoneBook.phone_book import Query, process_queries


class Test(TestCase):
    def test_process_queries(self):
        queries = [
            Query("add 911 police".split()),
            Query("add 76213 Mom".split()),
            Query("add 17239 Bob".split()),
            Query("find 76213".split()),
            Query("find 910".split()),
            Query("find 911".split()),
            Query("del 910".split()),
            Query("del 911".split()),
            Query("find 911".split()),
            Query("find 76213".split()),
            Query("add 76213 daddy".split()),
            Query("find 76213".split())
        ]
        result = process_queries(queries)
        expected = ["Mom", "not found", "police", "not found", "Mom", "daddy"]

        for i in range(len(result)):
            self.assertEqual(result[i], expected[i])

    def test_process_queries_2(self):
        queries = [
            Query("find 3839442".split()),
            Query("add 123456 me".split()),
            Query("add 0 granny".split()),
            Query("find 0".split()),
            Query("find 123456".split()),
            Query("del 0".split()),
            Query("del 0".split()),
            Query("find 0".split())
        ]
        result = process_queries(queries)
        expected = ["not found", "granny", "me", "not found"]

        for i in range(len(result)):
            self.assertEqual(result[i], expected[i])
