# python3
"""
File name: stack_with_max.py
Author: Sayuri Monarrez Yesaki
Date created: 02/01/2022
Date last modified: 02/02/2022
Python version: 3.8

A stack is an abstract data type supporting the operations Push() and Pop(). It is not difficult to implement it in a
way that both these operations work in constant time. In this problem, your goal will be to implement a stack that also
supports finding the maximum value and to ensure that all operations still work in contant time.

Task: Implement a stack supporting the operations Push(), Pop(), and Max().

Input: The first line of the input contains the number q of queries. Each of the following q lines specifies a query of
one of the following formats: push v, pop, or max.

Output: For each max query, output (on a separate line) the maximum value of the stack.

Constraints: 1 ≤ 𝑞 ≤ 400 000, 0 ≤ 𝑣 ≤ 105

Time limit: 5 sec

Memory Limit: 512 MB
"""
import math
import sys
from typing import Optional, Union


class StackWithMax:
    """
    Constructor of the StackWithMax class. The auxiliary stack is used
    to keep track of the max value in the stack and ensure the max method
    functions in constant time.
    """

    def __init__(self) -> None:
        self.__stack = []
        # Store the maximum value of the stack at each push.
        self.__auxiliary_stack = []

    """
    Adds a key to a collection.
    The new key is appended to the end of the __stack.
    The max between the new key and the most recently key added to __auxiliary_stack
    is appended to the end of the __auxiliary_stack.
    
    :param 1: a - new key to be added to the collection.
    """

    def push(self, a: int) -> None:
        self.__stack.append(a)
        self.__auxiliary_stack.append(max(a, self._peek()))

    """
    Removes and returns the most recently added key. 
    If __stack and __auxiliary_stack are not empty, removes the most
    recently added key to __auxiliary_stack and __stack, and returns 
    the popped element from __stack.
    
    :return: (int) the most recently added key.
    """

    def pop(self) -> Optional[int]:
        assert (len(self.__stack) and len(self.__auxiliary_stack)), "The stack is empty"
        self.__auxiliary_stack.pop()
        return self.__stack.pop()

    """
    Retrieve of fetch the most recently added key without deleting it from
    the __auxiliary_stack. If the stack is empty, return -inf.

    :return: Union[int, float] the most recently added key (int). If the stack is empty returns
            negative infinite (float).
    """

    def _peek(self) -> Union[int, float]:
        if len(self.__auxiliary_stack) == 0:
            return - math.inf
        return self.__auxiliary_stack[len(self.__auxiliary_stack) - 1]

    """
    Retrieve of fetch the most recently added key without deleting it from
    the __stack. If the stack is empty, return -inf.

    :return: Union[int, float] the most recently added key (int). If the stack is empty returns
            negative infinite (float).
    """

    def peek(self) -> Union[int, float]:
        if len(self.__stack) == 0:
            return - math.inf
        return self.__stack[len(self.__stack) - 1]

    """
    Scan the current contents of the stack to find the maximum value.
    Running time: O ( n )
    """

    def max_naive(self) -> int:
        assert (len(self.__stack))
        return max(self.__stack)

    """
    Find maximum value.
    :return: (int) max value
    """

    def max(self) -> int:
        assert (len(self.__stack)), "The stack is empty"
        return self.__auxiliary_stack[len(self.__auxiliary_stack) - 1]

    """
    Get the stack size

    :return: (int) stack size
    """

    def size(self) -> int:
        return len(self.__stack)


def run_stack_with_max():
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())

    for i in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.push(int(query[1]))
        elif query[0] == "pop":
            stack.pop()
        elif query[0] == "max":
            print(stack.max())
        else:
            assert 0


if __name__ == '__main__':
    run_stack_with_max()
