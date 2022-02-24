# python3
"""
File name: phone_book.py
Author: Sayuri Monarrez Yesaki
Date created: 02/24/2022
Date last modified: 02/24/2022
Python version: 3.8

Implement a simple phone book manager.

Task: Implement a simple phone book manager. It should be able to process the following types of
user's queries:
    - add number name : the user adds a person with name and phone number to the phone book. If there exists a user
    with such number already, then your manager has to overwrite the corresponding name.

    - del number : the manager should erase a person with number number from the phone book. If there is no such
    person, then it should just ignore the query.

    - find number : the user looks for a person with phone number number. The manager should reply with the
    appropriate name, or ith string "not found" (w/o quotes) if there is no such person in the book.

Input: single int N in the first line - the number of queries. It's followed by N lines, each of them contains one query
    in the format described above.

Output: Print the result of each find query - the name corresponding to the phone number or "not found" (w/o quotes)
    if there is no person in the phone book with such phone number. output one results per line in the same order
    as the find queries are given in the input.

Constraints: 1 <= N <= 10^5. All phone numbers consist of decimal digits, they don't have leading zeros, and each
    of them has no more than 7 digits. All names are non-empty strings of latin letters, and each of them has length at
    most 15. It's guaranteed that there is no person with name "not found".

Time limit: 6 sec.

Memory Limit: 512 MB
"""


class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]


def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]


def write_responses(result):
    print('\n'.join(result))


def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = []
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            for contact in contacts:
                if contact.number == cur_query.number:
                    contact.name = cur_query.name
                    break
            else:  # otherwise, just add it
                contacts.append(cur_query)
        elif cur_query.type == 'del':
            for j in range(len(contacts)):
                if contacts[j].number == cur_query.number:
                    contacts.pop(j)
                    break
        else:
            response = 'not found'
            for contact in contacts:
                if contact.number == cur_query.number:
                    response = contact.name
                    break
            result.append(response)
    return result


if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
