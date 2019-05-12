from unittest import TestCase
# https://leetcode.com/problems/my-calendar-iii/
import bisect, collections


class Node:
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end
        self.count = 0
        self.max = 0
        self.left = self.right = None
        self.md = (begin+end) >> 1

    def add(self, l, r):
        if r < self.begin or self.end < l:
            return
        if l <= self.begin and self.end <= r:
            self.count += 1
            self.max += 1
            return
        if not self.left:
            self.left = Node(self.begin, self.md)
        if not self.right:
            self.right = Node(self.md + 1, self.end)
        self.left.add(l, r)
        self.right.add(l, r)
        self.max = self.count + max(self.left.max, self.right.max)


class MyCalendarThree(object):

    def __init__(self):
        self.root = Node(0, int(1e9))

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: int
        """
        self.root.add(start, end-1)
        return self.root.max

# # bisect count_delta
# class MyCalendarThree(object):
#     def __init__(self):
#         self.pos = []
#         self.delta = {}
#         self.max = 0
#
#     def book(self, start, end):
#         i = bisect.bisect_left(self.pos, start)
#         if start not in self.delta:
#             self.delta[start] = self.delta[self.pos[i-1]] if i else 0
#             self.pos[i:i] = [start]
#
#         j = bisect.bisect_left(self.pos, end)
#         if end not in self.delta:
#             self.delta[end] = self.delta[self.pos[j-1]]
#             self.pos[j:j] = [end]
#         for k in range(i, j):
#             self.delta[self.pos[k]] = c = self.delta[self.pos[k]] + 1
#             self.max = max(self.max, c)
#         return self.max
#
# # segment tree by hash
# class MyCalendarThree(object):
#     def __init__(self):
#         self.max = collections.defaultdict(int)
#         self.lazy = collections.defaultdict(int)
#
#     def update(self, l, r, left=0, right=int(1e9), id=1):
#         if right <= l or r <= left: return
#         if l <= left and right <= r:
#             self.max[id] += 1
#             self.lazy[id] += 1
#         else:
#             md = (left + right) >> 1
#             lc, rc = id*2, id*2+1
#             self.update(l, r, left, md, lc)
#             self.update(l, r, md, right, rc)
#             self.max[id] = self.lazy[id] + max(self.max[lc], self.max[rc])
#
#     def book(self, start, end):
#         self.update(start, end)
#         return self.max[1]

class Tests(TestCase):
    def test1(self):
        c = MyCalendarThree()
        self.assertEqual(1, c.book(10, 20))
        self.assertEqual(1, c.book(50, 60))
        self.assertEqual(2, c.book(10, 40))
        self.assertEqual(3, c.book(5, 15))
        self.assertEqual(3, c.book(5, 10))
        self.assertEqual(3, c.book(25, 55))



