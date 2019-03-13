from unittest import TestCase
# https://leetcode.com/problems/intersection-of-two-linked-lists


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class IntersectionOfTwoLinkedLists(object):
    def getIntersectionNode(self, a, b):
        def getLen(node):
            l = 0
            while node:
                node = node.next
                l += 1
            return l

        la, lb = getLen(a), getLen(b)
        for _ in range(la, lb):
            b = b.next
        for _ in range(lb, la):
            a = a.next
        while a != b:
            a = a.next
            b = b.next
        return a

    # # by concat
    # def getIntersectionNode(self, headA, headB):
    #     a, b = headA, headB
    #     while a != b:
    #         a = a.next if a else headB
    #         b = b.next if b else headA
    #     return a


