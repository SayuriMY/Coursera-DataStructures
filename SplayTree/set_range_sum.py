# python3
"""
File name: set_range_sum.py
Author: Sayuri Monarrez Yesaki
Date created: 03/23/2022
Date last modified: 03/23/2022
Python version: 3.8

Implement a data structure to store a set of integers and quickly compute range sums.

Task: Implement a data structure that stores a set S of integers with the following allowed operations:

        add(i) - add integer i into the set S (if it was there already, the set does not change).
        del(i) - remove integer i from the set S (if there was no such element, nothing happens)
        find(i) - check whether i is in the set S or not.
        sum(l,r)- output the sum of all elements v in S such that l <= v <= r.

Input: Initially the set S is empty. The first line contains n - the number of operations. The next n lines
    contains operations. Each operation is one of the following:

        Note: Each request will actually depend on the result of the last sum request. M = 1 000 000 001.
              At any moment, let x be the result of the last sum operation, or just 0 if there were no sum operations
               before.

        "+ i" - add some integer ((i+x) mod M) to S
        "- i" - delete some integer ((i+x) mod M) from S
        "? i" - find some integer ((i+x) mod M) in S
        "s l r" - compute the sum of all elements of S within some range of values sum((l+x) mod M, (r+x) mod M)

Constraints: 1 <= n <= 100 000; 0 <= i <= 10 ^ 9

Output: For each find request, just output "Found" or "Not found" depending on whether (i+x) mod M is in S or not.
        For each sum, output the sum of all values v in such that ((l+x) mod M) <= v <= ((r+x) mod M), where x is the
            result of the last sum operation or 0 if there was no previous sum operation.

Time limit: 120 sec

Memory Limit: 512 MB
"""

from sys import stdin


# Splay tree implementation

# Vertex of a splay tree
class Vertex:
    def __init__(self, key, sum, left, right, parent):
        (self.key, self.sum, self.left, self.right, self.parent) = (key, sum, left, right, parent)


def update(v):
    if v == None:
        return
    v.sum = v.key + (v.left.sum if v.left != None else 0) + (v.right.sum if v.right != None else 0)
    if v.left != None:
        v.left.parent = v
    if v.right != None:
        v.right.parent = v


def smallRotation(v):
    parent = v.parent
    if parent == None:
        return
    grandparent = v.parent.parent
    if parent.left == v:
        m = v.right
        v.right = parent
        parent.left = m
    else:
        m = v.left
        v.left = parent
        parent.right = m
    update(parent)
    update(v)
    v.parent = grandparent
    if grandparent != None:
        if grandparent.left == parent:
            grandparent.left = v
        else:
            grandparent.right = v


def bigRotation(v):
    if v.parent.left == v and v.parent.parent.left == v.parent:
        # Zig-zig
        smallRotation(v.parent)
        smallRotation(v)
    elif v.parent.right == v and v.parent.parent.right == v.parent:
        # Zig-zig
        smallRotation(v.parent)
        smallRotation(v)
    else:
        # Zig-zag
        smallRotation(v)
        smallRotation(v)


# Makes splay of the given vertex and makes
# it the new root.
def splay(v):
    if v == None:
        return None
    while v.parent != None:
        if v.parent.parent == None:
            smallRotation(v)
            break
        bigRotation(v)
    return v


# Searches for the given key in the tree with the given root
# and calls splay for the deepest visited node after that.
# Returns pair of the result and the new root.
# If found, result is a pointer to the node with the given key.
# Otherwise, result is a pointer to the node with the smallest
# bigger key (next value in the order).
# If the key is bigger than all keys in the tree,
# then result is None.
def find(root, key):
    v = root
    last = root
    next = None
    while v != None:
        if v.key >= key and (next == None or v.key < next.key):
            next = v
        last = v
        if v.key == key:
            break
        if v.key < key:
            v = v.right
        else:
            v = v.left
    root = splay(last)
    return (next, root)


def split(root, key):
    (result, root) = find(root, key)
    if result == None:
        return (root, None)
    right = splay(result)
    left = right.left
    right.left = None
    if left != None:
        left.parent = None
    update(left)
    update(right)
    return (left, right)


def merge(left, right):
    if left == None:
        return right
    if right == None:
        return left
    while right.left != None:
        right = right.left
    right = splay(right)
    right.left = left
    update(right)
    return right


# Code that uses splay tree to solve the problem

root = None


def insert(x):
    global root
    (left, right) = split(root, x)
    new_vertex = None
    if right == None or right.key != x:
        new_vertex = Vertex(x, x, None, None, None)
    root = merge(merge(left, new_vertex), right)


def erase(x):
    global root
    # Implement erase yourself
    pass


def search(x):
    global root
    # Implement find yourself

    return False


def sum(fr, to):
    global root
    (left, middle) = split(root, fr)
    (middle, right) = split(middle, to + 1)
    ans = 0
    # Complete the implementation of sum

    return ans


MODULO = 1000000001
# number of operations
n = int(stdin.readline())
last_sum_result = 0
for i in range(n):
    line = stdin.readline().split()
    # add some integer ((i+x) mod M) to S, where x is the result of the last sum operation.
    if line[0] == '+':
        x = int(line[1])
        insert((x + last_sum_result) % MODULO)
    # delete some integer ((i+x) mod M) from S, where x is the result of the last sum operation.
    elif line[0] == '-':
        x = int(line[1])
        erase((x + last_sum_result) % MODULO)
    # find some integer ((i+x) mod M) in S, where x is the result of the last sum operation.
    elif line[0] == '?':
        x = int(line[1])
        print('Found' if search((x + last_sum_result) % MODULO) else 'Not found')
    # compute the sum of all elements of S within some range of values sum((l+x) mod M, (r+x) mod M),
    # where x is the result of the last sum operation.
    elif line[0] == 's':
        l = int(line[1])
        r = int(line[2])
        res = sum((l + last_sum_result) % MODULO, (r + last_sum_result) % MODULO)
        print(res)
        last_sum_result = res % MODULO
