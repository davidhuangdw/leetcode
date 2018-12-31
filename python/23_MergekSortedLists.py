from unittest import TestCase
import queue
from Definitions import ListNode
# https://leetcode.com/problems/merge-k-sorted-lists/


class MergekSortedLists(TestCase):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        tail = head = ListNode(0)
        que = queue.PriorityQueue()
        for i in range(len(lists)):
            lists[i] and que.put((lists[i].val, i))
        while not que.empty():
            i = que.get()[1]
            tail.next = lists[i]
            tail = tail.next
            lists[i] = lists[i].next
            lists[i] and que.put((lists[i].val, i))
        return head.next

    def test1(self):
        self.assertEqual([1, 1, 2, 3, 4, 4, 5, 6], self.mergeKLists([
            ListNode.build_from_list(1, 4, 5),
            ListNode.build_from_list(1, 3, 4),
            ListNode.build_from_list(2, 6),
        ]).as_list())
