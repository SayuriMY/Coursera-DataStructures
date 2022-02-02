import unittest
from BracketsInCode.brackets_in_code import find_mismatch, are_matching
import os


def read_test_file(test_path):
    with open(test_path, 'r') as reader:
        return reader.readline().strip()


class TestFindMismatch(unittest.TestCase):
    def test_find_mismatch(self):
        input_string = '[]'
        self.assertEqual(find_mismatch(input_string), 'Success')

        input_string = '{}[]'
        self.assertEqual(find_mismatch(input_string), 'Success')

        input_string = '[()]'
        self.assertEqual(find_mismatch(input_string), 'Success')

        input_string = '(())'
        self.assertEqual(find_mismatch(input_string), 'Success')

        input_string = '{[]}()'
        self.assertEqual(find_mismatch(input_string), 'Success')

        input_string = 'foo(bar)'
        self.assertEqual(find_mismatch(input_string), 'Success')

        input_string = '{'
        self.assertEqual(find_mismatch(input_string), '1')

        input_string = '{[}'
        self.assertEqual(find_mismatch(input_string), '3')

        input_string = 'foo(bar[i);'
        self.assertEqual(find_mismatch(input_string), '10')

        input_string = '[{{}}]'
        self.assertEqual(find_mismatch(input_string), 'Success')

        input_string = '}'
        self.assertEqual(find_mismatch(input_string), '1')

        input_string = '}()'
        self.assertEqual(find_mismatch(input_string), '1')

        # get all files in test folder.
        test_path = os.path.join(os.getcwd(), 'tests')
        test_files = os.listdir(test_path)

        filtered_test_files = [file for file in test_files if not file.endswith('.a')]

        for test in filtered_test_files:

            # read file with problem
            input_string = read_test_file(os.path.join(test_path, test))

            result = find_mismatch(input_string)

            # read answer
            answer = read_test_file(os.path.join(test_path, test + '.a'))

            self.assertEqual(result, answer)
