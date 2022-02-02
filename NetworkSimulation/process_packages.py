# python3
"""
File name: process_packages.py
Author: Sayuri Monarrez Yesaki
Date created: 01/31/2022
Date last modified: 02/01/2022
Python version: 3.8

Implement a program to simulate the processing of network packets.

Task: Simulate the processing of a series of incoming network packets. Packets arrive in some order. For each packet
number i, you know the time when it arrived Ai and the time it takes to processor to process it Pi (both in
milliseconds). There is only one processor, and it processes the incoming packets in the order of their arrival. If the
processor started to process some packet, it doesn't interrupt or stop until it finished the processing of this packet,
and the processing of packet i takes exactly Pi milliseconds.

The computer processing the packets has a network buffer of fixed size S. When the packets arrive, they are stored
in the buffer before being processed. However, if the buffer is full when a packet arrives ( there are S packets which
have arrived before this packet, and the computer hasn't finished processing any of them), it is dropped and won't be
processed at all. If several packets arrive at the same time, they are first all stored in the buffer r (some of
them may be dropped because of that — those which are described later in the input). The computer processes the packets
in the order of their arrival, and it starts processing the next available packet from the buffer as soon as it finishes
processing the previous one. If at some point the computer is not busy, and there are no packets in
the buffer, the computer just waits for the next packet to arrive. Note that a packet leaves the buffer
and frees the space in the buffer as soon as the computer finishes processing it.

Input: The first line of the input contains the size 𝑆 of the buffer and the number 𝑛 of incoming
network packets. Each of the next 𝑛 lines contains two numbers. 𝑖-th line contains the time of arrival
𝐴𝑖 and the processing time 𝑃𝑖 (both in milliseconds) of the 𝑖-th packet. It is guaranteed that the
sequence of arrival times is non-decreasing (however, it can contain the exact same times of arrival in
milliseconds — in this case the packet which is earlier in the input is considered to have arrived earlier).

Output: For each packet output either the moment of time (in milliseconds) when the processor
began processing it or −1 if the packet was dropped (output the answers for the packets in the same
order as the packets are given in the input).


Constraints: All the numbers in the input are integers. 1 ≤ 𝑆 ≤ 105 ; 0 ≤ 𝑛 ≤ 105 ; 0 ≤ 𝐴𝑖 ≤ 106 ; 0 ≤ 𝑃𝑖 ≤ 103 ;
𝐴𝑖 ≤ 𝐴𝑖+1 for 1 ≤ 𝑖 ≤ 𝑛 − 1.

Time limit: 10 sec

Memory Limit: 512 MB
"""

from collections import namedtuple

"""
Specialized container datatype. Namedtuple() is used for creating tuple
subclasses with named fields.
"""
Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    """
        Constructor of the Buffer class

        :param 1: size (int) -> network buffer size - number of non-processed packets
                  that can be stored by the network
    """
    def __init__(self, size: int) -> None:
        self.size = size
        # store the times when the computer will finish processing the packets which are currently stored in the
        # network buffer
        self.finish_time = []

    """
    Process a new packet:
    Pop all the packets that have been processed by the time the new packet arrives. If the buffer is full
    after dropping the processed packets, drop the new packet. Otherwise, try to append the processing finish
    time of the new packed in the finish_time. 
    If the buffer is empty, process the new packet immediately. Otherwise, store it in the buffer.
    
    :param 1: request (Request) -> Namedtuple with the packet time of arrival and time it takes to process a packet
    :return : response (Response) -> Namedtuple with the processing response - was dropped, processing start time
    """
    def process(self, request: Request) -> Response:
        # Pop from the from the front of finish_time all the packets which are already processed
        # by the time a new packet arrives.
        while len(self.finish_time) != 0 and self.finish_time[0] <= request.arrived_at:
            self.finish_time.pop(0)

        # If there is space in the buffer, add the new packet's processing finish time.
        if len(self.finish_time) < self.size:

            # Calculate the new packet's finish and start time assuming the buffer is empty -  start processing the
            # new packet immediately as soon as it arrives.

            # If the buffer is empty, the finish time of the new packet is the time of arrival plus the time
            # it takes the new packet to be processed.
            finish_time = request.arrived_at + request.time_to_process
            # start time == time of arrival.
            start_time = request.arrived_at

            # if finish_time list is not empty, access the last element of the packets in finish_time to
            # determine when the computer will start to process the new packet.
            if len(self.finish_time) != 0:
                # Since the buffer is not empty, the finish time of the new packet is the finish time of the last
                # packet plus the time it takes the new packet to be processed.
                finish_time = self.finish_time[len(self.finish_time) - 1] + request.time_to_process
                # start time == finish_time of the last element in the buffer.
                start_time = self.finish_time[len(self.finish_time) - 1]

            self.finish_time.append(finish_time)
            # If buffer is not full: Response - was_dropped : False, started_at : start_time
            return Response(False, start_time)

        # the buffer is full, drop the packet
        return Response(True, -1)


"""
This method iterates over all requests and process them using the
process function in the Buffer class. The responses from the 
Buffer.process are saved in a list and returned.

:param 1: requests (list of Requests) 
:param 1: Buffer object 

:return: list of responses
"""


def process_requests(requests: list, buffer: Buffer) -> list:
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def run_process_packages():
    # size 𝑆 of the buffer and the number 𝑛 of incoming network packets
    buffer_size, n_requests = map(int, input().split())

    # save all packet processing requests in a list.
    requests = []
    # Iterate over each request. For each request, convert the input time of arrival and processing time into an int,
    # save it in a Request namedtuple, and append the instantiated tuple to the list of requests.
    for n in range(n_requests):
        # packet time of arrival, packet processing time
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    run_process_packages()