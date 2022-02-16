# python3
"""
File name: merging_tables.py
Author: Sayuri Monarrez Yesaki
Date created: 02/10/2022
Date last modified: 02/10/2022
Python version: 3.8

The goal of this problem is to simulate a sequence of merge operations with tables in a database.

Task: There are n tables stored in some database. The tables are numbered from 1 to n. All tables share the same set
of columns. Each table contains either several rows with real data or a symbolic link to another table. Initially,
all tables contain data, and i-th table has ri rows. You need to perform m of the following operations:

    1. Consider table number destinationi. Traverse the path of symbolic links to get to the data. That is, while
        destinationi contains a symbolic link instead of real data do
            destinationi <- symlink(destinationi)

    2. Consider the table number sourcei and traverse the path of symbolic links from it in the same manner
        as for destinationi.

    3. Now, destionationi and sourcei are the numbers of two table with real data.If destionationi != sourcei, copy
        all the rows from table sourcei to table destionationi, then clear the table sourcei and instead of
        real data put a symbolic link to destionationi into it.

    4. Print the maximum size among all n tables (recall that size is the number of rows in the table). If the table
        contains only a symbolic link, its size is considered to be 0.

Input: The first line of the input contains two integers n and m - the number of tables in the database and the number
    of merge queries to perform, respectively.
    The second line of the input contains n integers ri - number of rows in the i-th table.
    Then follow m lines describing merge queries. Each of them contains two integers destinationi and sourcei -
        the numbers of the tables to merge.

Output: For each query print a line containing a single integer - the maximum of the size of all tables ( in terms
    of the number of rows ) after the corresponding operation.

Constraints: 1 ≤ 𝑛, 𝑚 ≤ 100 000; 0 ≤ 𝑟𝑖 ≤ 10 000; 1 ≤ 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖, 𝑠𝑜𝑢𝑟𝑐𝑒𝑖 ≤ n

Time limit: 6 sec.

Memory Limit: 512 MB
"""


class Database:
    """
        Constructor of the Database class
        :param 1: row_counts (list) -> list with the number of rows in the i-th table.
    """
    def __init__(self, row_counts: list) -> None:
        self.row_counts = row_counts
        self.max_row_count = max(row_counts)
        n_tables = len(row_counts)
        self.ranks = [0] * n_tables
        self.parents = list(range(n_tables))

    """
        Merge destination and source tables using union by rank heuristic.
    """
    def merge(self, dst: int, src: int) -> bool:
        # source parent
        src_parent = self.get_parent(src)
        # destination parent
        dst_parent = self.get_parent(dst)

        if src_parent == dst_parent:
            return False

        # merge two components
        merged_tables = self.row_counts[src_parent] + self.row_counts[dst_parent]
        # use union by rank heuristic - Hang the shorter tree under a taller one.
        if self.ranks[src_parent] > self.ranks[dst_parent]:
            self.row_counts[src_parent] = merged_tables
            self.row_counts[dst_parent] = 0
            self.parents[dst_parent] = src_parent
        else:
            self.row_counts[dst_parent] = merged_tables
            self.row_counts[src_parent] = 0
            self.parents[src_parent] = dst_parent

            if self.ranks[dst_parent] == self.ranks[src_parent]:
                self.ranks[dst_parent] = self.ranks[dst_parent] + 1

        # # update max_row_count with the new maximum table size
        if merged_tables > self.max_row_count:
            self.max_row_count = merged_tables

        return True

    """
        Traverse the path of symbolic links to get to the data. 
        Follow the parent links from table until the root is
        reached.
        running time: O ( tree height )
    """
    def get_parent(self, table: int) -> int:
        i = table
        # find parent and compress path
        while i != self.parents[i]:
            i = self.parents[i]
        return i


def run_merging_tables():
    n_tables, n_queries = map(int, input().split())
    counts = list(map(int, input().split()))
    assert len(counts) == n_tables
    db = Database(counts)
    for i in range(n_queries):
        dst, src = map(int, input().split())
        db.merge(dst - 1, src - 1)
        print(db.max_row_count)


if __name__ == "__main__":
    run_merging_tables()