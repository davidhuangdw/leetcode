from unittest import TestCase
# https://leetcode.com/problems/linked-list-random-node/
from Definitions import ListNode
import random


class Solution:

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        cur = self.head
        chosen = None
        size = 0
        while cur:
            size += 1
            if random.randint(1, size) == 1:
                chosen = cur
            cur = cur.next
        return chosen.val


