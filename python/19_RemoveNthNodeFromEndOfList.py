from unittest import TestCase
# https://leetcode.com/problems/remove-nth-node-from-end-of-list
from Definitions import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class RemoveNthNodeFromEndOfList(TestCase):
    def removeNthFromEnd(self, head: 'ListNode', n: 'int') -> 'ListNode':
        l = r = hd = ListNode(0)
        hd.next = head
        for _ in range(n+1):
            r = r.next
        while r:
            r = r.next
            l = l.next
        l.next = l.next.next
        return hd.next

    def test1(self):
        self.assertEqual([1,2,3,5], self.removeNthFromEnd(ListNode.build_from_list(1,2,3,4,5), 2).as_list())

    def test2(self):
        self.assertEqual([2,3,4,5], self.removeNthFromEnd(ListNode.build_from_list(1,2,3,4,5), 5).as_list())

        

