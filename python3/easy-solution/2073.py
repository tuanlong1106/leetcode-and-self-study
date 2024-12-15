"""
2073. Time Needed to Buy a Ticket
    There are n people in a line queuing to buy tickets, where the 0th person is at the front of the line and the (n - 1)th person is at the back of the line.
    You are given a 0-indexed integer array tickets of length n where the number of tickets that the ith person would like to buy is tickets[i].
    Each person takes exactly 1 second to buy a ticket. A person can only buy 1 ticket at a time and has to go back to the end of the line (which happens instantaneously) in order to buy more tickets. If a person does not have any tickets left to buy, the person will leave the line.
    Return the time taken for the person initially at position k (0-indexed) to finish buying tickets.

    Example :
    Input: tickets = [2,3,2], k = 2
    Output: 6
    Explanation:
    The queue starts as [2,3,2], where the kth person is underlined.
    After the person at the front has bought a ticket, the queue becomes [3,2,1] at 1 second.
    Continuing this process, the queue becomes [2,1,2] at 2 seconds.
    Continuing this process, the queue becomes [1,2,1] at 3 seconds.
    Continuing this process, the queue becomes [2,1] at 4 seconds. Note: the person at the front left the queue.
    Continuing this process, the queue becomes [1,1] at 5 seconds.
    Continuing this process, the queue becomes [1] at 6 seconds. The kth person has bought all their tickets, so return 6.
"""

from typing import List
from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue= deque()
        wait = 0 
        for i in range(len(tickets)):
            queue.append(i)
        while queue:
            idx = queue.popleft()
            tickets[idx] -= 1
            wait += 1
            if tickets[idx] == 0 and idx == k:
                return wait
            if tickets[idx] > 0:
                queue.append(idx)
        return wait