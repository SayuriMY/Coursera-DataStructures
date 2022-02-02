# python3
"""
File name: brackets_in_code.py
Author: Sayuri Monarrez Yesaki
Date created: 01/28/2022
Date last modified: 01/28/2022
Python version: 3.8

Problem: implement a feature for a text editor to find errors in the usage of brackets in the code.

Task:
Your friend is making a text editor for programmers. He is currently working on a feature that will
find errors in the usage of different types of brackets. Code can contain any brackets from the set
[]{}(), where the opening brackets are [,{, and ( and the closing brackets corresponding to them are
],}, and ).

For convenience, the text editor should not only inform the user that there is an error in the usage
of brackets, but also point to the exact place in the code with the problematic bracket.

=> First priority is to find the first unmatched closing bracket which either doesn’t have an opening
bracket before it, like ] in ](), or closes the wrong opening bracket, like } in ()[}.

=> If there are no such mistakes, then it should find the first unmatched opening bracket without the
corresponding closing bracket after it, like ( in {}([].

=> If there are no mistakes, text editor should inform the user that the usage of brackets is correct.

Apart from the brackets, code can contain big and small latin letters, digits and punctuation marks.

More formally, all brackets in the code should be divided into pairs of matching brackets, such that
in each pair the opening bracket goes before the closing bracket, and for any two pairs of brackets
either one of them is nested inside another one as in (foo[bar]) or they are separate as in f(a,b)-g[c].

The bracket [ corresponds to the bracket ], { corresponds to }, and ( corresponds to ).

Input: Input contains one string 𝑆 which consists of big and small latin letters, digits, punctuation
marks and brackets from the set []{}().

Output: If the code in 𝑆 uses brackets correctly, output “Success" (without the quotes). Otherwise,
output the 1-based index of the first unmatched closing bracket, and if there are no unmatched closing
brackets, output the 1-based index of the first unmatched opening bracket.

Constraints: The length of 𝑆 is at least 1 and at most 10 .
Time limit: 5 sec
Memory Limit: 512MB
"""
from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left: str, right: str) -> bool:
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text: str) -> str:
    opening_brackets_stack = []

    # the enumerate method adds a counter to an iterable and returns it in a form of enumerate object.
    # the default start of the enumerate is 0.
    for idx, char in enumerate(text):

        # if open bracket, save it into the stack
        if char in "([{":
            opening_brackets_stack.append(Bracket(char, idx + 1))

        # Process closing bracket
        elif char in ")]}":
            # Priority 1: return the first unmatched closing bracket.
            if len(opening_brackets_stack) == 0:
                return str(idx + 1)

            # if closing bracket, pop the stack
            popped = opening_brackets_stack.pop()

            if not are_matching(popped.char, char):
                # Priority 1: return the first unmatched closing bracket.
                return str(idx + 1)

    # Priority 2: find first unmatched opening bracket w/o closing bracket.
    first_unmatched_opening_bracket = None
    while len(opening_brackets_stack) != 0:
        first_unmatched_opening_bracket = opening_brackets_stack.pop()

    if not (first_unmatched_opening_bracket is None):
        return str(first_unmatched_opening_bracket.position)

    # Priority 3: if no mistakes, inform the bracket usage is correct.
    return 'Success'


def run_brackets_in_code():
    text = input()
    print(find_mismatch(text))


if __name__ == "__main__":
    run_brackets_in_code()
