# python3
"""
File name: hash_chains.py
Author: Sayuri Monarrez Yesaki
Date created: 02/24/2022
Date last modified: 02/24/2022
Python version: 3.8

Implement a hash table using the chaining scheme. Chaining is one of the most popular ways of implementing hash tables
in practice. The hash table you will implement can be used to implement a phone book on your phone or to store the
password table of your computer or web service.

Task: Implement a hash table with lists chaining. You're already given the number of buckets m and the hash function.
    It is a polynomial hash function.
                h(S) = (E S[i] x ^ i mod p) mod m

    where S[i] is the ASCII code of the i-th symbol of S, p = 1 000 000 007 and x = 263. Your program should support
    the following kinds of queries:

        - add string : insert string into the table. If there is already such string in the hash table,
        then just ignore the query.

        - del string : remove string from the table. If there is no such string in the hash table, then just ignore
            the query.

        - find string : output "yes" or "no" (w/o quotes) depending on whether the table contains string or not.

        - check i - output the content of the i-th list in the table. Use spaces to separate the elements of the list.
        If the i-th list is empty, output the blank line.

    When inserting a new string into a has chain, you must insert it in the beginning of the chain.

Input: single int m in the first line - the number of buckets you should have. The next line contains the number of
    queries N. It's followed by N lines, each of them contains one query in the format described above.

Output: Print the result of each of the find and check queries, one result per line, in the same order as these
    queries are given in the input.

Constraints: 1 <= N <= 10^5; N/5 <= m <= N. All the strings consist of latin letters. Each of them is non-empty and has
    length at most 15.

Time limit: 7 sec.

Memory Limit: 512 MB
"""


class Query:
    def __init__(self, query: list):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count: int):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = []

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query: Query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            self.write_chain(cur for cur in reversed(self.elems)
                             if self._hash_func(cur) == query.ind)
        else:
            try:
                ind = self.elems.index(query.s)
            except ValueError:
                ind = -1
            if query.type == 'find':
                self.write_search_result(ind != -1)
            elif query.type == 'add':
                if ind == -1:
                    self.elems.append(query.s)
            else:
                if ind != -1:
                    self.elems.pop(ind)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())


if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
