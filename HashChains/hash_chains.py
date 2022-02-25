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
        # cardinality of the hash function
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = []
        for i in range(self.bucket_count):
            self.elems.append([])

    def _hash_func(self, s: str) -> int:
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found: int) -> str:
        return 'yes' if was_found else 'no'

    def write_chain(self, chain: list) -> str:
        return ' '.join(chain)

    def process_queries_chaining(self, queries: list) -> list:
        result = []
        for query in queries:
            # check i - output the content of the i-th list in the table. Use spaces to separate the elements of the
            # list. if the i-th list is empty, output a blank line.
            if query.type == "check":
                result.append(self.write_chain(self.elems[query.ind]))
            else:
                # calculate hash of the string
                hash = self._hash_func(query.s)

                try:
                    ind = self.elems[hash].index(query.s)
                except ValueError:
                    ind = -1

                # find string - output "yes" or "no" depending on whether the table contains string or not.
                if query.type == 'find':
                    result.append(self.write_search_result(ind != -1))

                # add string - insert string into the table. if there is already such string in the hash table,
                # then just ignore the query.
                elif query.type == 'add':
                    if not (query.s in self.elems[hash]):
                        self.elems[hash].insert(0, query.s)

                # del string - remove string from the table. If there is no such string in  the hash table, then just
                # ignore the query
                else:
                    if query.s in self.elems[hash]:
                        self.elems[hash].pop(ind)

        return result


def write_responses(result: list):
    print('\n'.join(result))


def read_queries() -> list:
    n = int(input())
    return [Query(input().split()) for i in range(n)]


if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    queries = read_queries()
    write_responses(proc.process_queries_chaining(queries))
