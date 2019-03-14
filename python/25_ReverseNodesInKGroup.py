from unittest import TestCase
# https://leetcode.com/problems/reverse-nodes-in-k-group
from Definitions import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ReverseNodesInKGroup(TestCase):
    def reverseKGroup(self, node: 'ListNode', k: 'int') -> 'ListNode':
        def forward(node):
            hd, broken = ListNode(-1), False
            for _ in range(k):
                if not node:
                    broken = True
                    break
                nxt = node.next
                node.next = hd.next
                hd.next = node
                node = nxt
            return hd.next, node, broken

        hd = tail = ListNode(-1)
        while node:
            rev, nxt, broken = forward(node)
            tail.next = forward(rev)[0] if broken else rev
            tail, node = node, nxt
        return hd.next

    # # two pointers to avoid last reverse
    # def reverseKGroup(self, node: 'ListNode', k: 'int') -> 'ListNode':
    #     hd = pre = ListNode(-1)
    #     ahead = node
    #     for _ in range(k-1):
    #         if not ahead: break
    #         ahead = ahead.next
    #     while ahead:
    #         now_pre = node
    #         for _ in range(k):
    #             if ahead: ahead = ahead.next
    #             node.next, pre.next, node = pre.next, node, node.next
    #         pre = now_pre
    #     pre.next = node
    #     return hd.next

    def test1(self):
        self.assertEqual([2,1,4,3,5], self.reverseKGroup(ListNode.build_from_list(1,2,3,4,5), 2).as_list())

    def test2(self):
        self.assertEqual([3,2,1,4,5], self.reverseKGroup(ListNode.build_from_list(1,2,3,4,5), 3).as_list())


