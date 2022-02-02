import os
from unittest import TestCase
from NetworkSimulation.process_packages import Buffer, process_requests, Request, Response


def read_test_answer(test_path):
    answers = []
    with open(test_path, 'r') as reader:
        for line in reader:
            answers.append(int(line.strip()))
    return answers


def read_test_file(test_path):
    lines = []
    with open(test_path, 'r') as reader:
        lines = reader.readlines()

    buffer_size, n_requests = map(int, lines[0].strip().split())

    requests = []
    for i in range(1, n_requests + 1):
        arrived_at, time_to_process = map(int, lines[i].strip().split())
        requests.append(Request(arrived_at, time_to_process))

    return buffer_size, requests


class Test(TestCase):
    def test_process_requests(self):
        buffer_size = 1
        requests = [Request(0, 1), Request(1, 3), Request(4, 2)]
        buffer = Buffer(buffer_size)
        responses = process_requests(requests, buffer)
        answer = [0, 1, 4]
        for i in range(len(answer)):
            self.assertEqual(responses[i].started_at, answer[i])

        buffer_size = 1
        requests = [Request(0, 2), Request(1, 4), Request(5, 3)]
        buffer = Buffer(buffer_size)
        responses = process_requests(requests, buffer)
        answer = [0, -1, 5]
        for i in range(len(answer)):
            self.assertEqual(responses[i].started_at, answer[i])

        buffer_size = 1
        requests = [Request(0, 0)]
        buffer = Buffer(buffer_size)
        responses = process_requests(requests, buffer)
        answer = [0]
        for i in range(len(answer)):
            self.assertEqual(responses[i].started_at, answer[i])

        # get all files in test folder.
        test_path = os.path.join(os.getcwd(), 'tests')
        test_files = os.listdir(test_path)

        filtered_test_files = [file for file in test_files if not file.endswith('.a')]

        for test in filtered_test_files:
            # print(f'test: {test}')
            buffer_size, requests = read_test_file(os.path.join(test_path, test))
            buffer = Buffer(buffer_size)
            responses = process_requests(requests, buffer)

            # read answer
            answer = read_test_answer(os.path.join(test_path, test + '.a'))

            for i in range(len(answer)):
                self.assertEqual(responses[i].started_at, answer[i])
