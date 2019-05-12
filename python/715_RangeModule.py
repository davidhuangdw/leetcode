from unittest import TestCase
# https://leetcode.com/problems/range-module/
import bisect


class RangeModule:
    def __init__(self):
        self.ranges = []

    def addRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void
        """
        n = len(self.ranges)
        i, j = 0, n-1
        while i < n and self.ranges[i][1] < left:
            i += 1
        while j >= 0 and self.ranges[j][0] > right:
            j -= 1
        if i <= j:
            left = min(left, self.ranges[i][0])
            right = max(right, self.ranges[j][1])
        self.ranges[i:j+1] = [[left, right]]

    def queryRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: bool
        """
        n = len(self.ranges)
        l, r = 0, n-1
        while l <= r:
            m = (l+r) >> 1
            if self.ranges[m][0] <= left:
                l = m+1
            else:
                r = m-1
        return r >= 0 and self.ranges[r][1] >= right

    def removeRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void
        """
        n = len(self.ranges)
        i, j = 0, n-1
        while i < n and self.ranges[i][1] <= left:
            i += 1
        while j >= 0 and self.ranges[j][0] >= right:
            j -= 1
        if i <= j:
            md = []
            if self.ranges[i][0] < left:
                md.append([self.ranges[i][0], left])
            if right < self.ranges[j][1]:
                md.append([right, self.ranges[j][1]])
            self.ranges[i:j+1] = md

# # bisect intervals
# class RangeModule:
#     def __init__(self):
#         self.rangel = []
#         self.ranger = []
#
#     # def print(self, i):
#     #     print((self.rangel[i], self.ranger[i]))
#
#     def addRange(self, left, right):
#         i = bisect.bisect_left(self.ranger, left)
#         j = bisect.bisect_right(self.rangel, right)
#         if i < j:
#             left = min(left, self.rangel[i])
#             right = max(right, self.ranger[j-1])
#         self.rangel[i:j] = [left]
#         self.ranger[i:j] = [right]
#
#     def removeRange(self, left, right):
#         i = bisect.bisect_right(self.ranger, left)
#         j = bisect.bisect_left(self.rangel, right)
#         if i < j:
#             mdl, mdr = [], []
#             if self.rangel[i] < left:
#                 mdl.append(self.rangel[i])
#                 mdr.append(left)
#             if self.ranger[j-1] > right:
#                 mdl.append(right)
#                 mdr.append(self.ranger[j-1])
#             self.rangel[i:j] = mdl
#             self.ranger[i:j] = mdr
#
#     def queryRange(self, left, right):
#         i = bisect.bisect_right(self.ranger, left)
#         return i < len(self.rangel) and self.rangel[i] <= left and self.ranger[i] >= right

# # bisect points: both ends at the same array
# class RangeModule:
#     def __init__(self):
#         self.ranges = []
#
#     # 1. which can be remove when add/remove range [a, b): a<=x<=b, x could be any end
#     # 2. keep original odd/even when insert
#     def addRange(self, left, right):
#         insert = []
#         i = bisect.bisect_left(self.ranges, left)
#         if i % 2 == 0: insert.append(left)
#         j = bisect.bisect_right(self.ranges, right)
#         if j % 2 == 0: insert.append(right)
#         self.ranges[i:j] = insert
#         # print([(self.ranges[i], self.ranges[i+1]) for i in range(0, len(self.ranges), 2)])
#
#     def removeRange(self, left, right):
#         insert = []
#         i = bisect.bisect_left(self.ranges, left)
#         if i % 2: insert.append(left)
#         j = bisect.bisect_right(self.ranges, right)
#         if j % 2: insert.append(right)
#         self.ranges[i:j] = insert
#
#     # find the nearest left end and right end
#     def queryRange(self, left, right):
#         i = bisect.bisect_right(self.ranges, left) -1
#         j = bisect.bisect_left(self.ranges, right)
#         return 0 <= i == j-1 < len(self.ranges) and i % 2 == 0

# # segment tree
# class RangeModule:
#     class Node:
#         def __init__(self, l, r):
#             self.left = l
#             self.right = r
#             self.md = (l+r) >> 1
#             self.len = r-l
#             self.ch = [None, None]
#             self.reset = self.sum = 0
#
#         def update(self, reset=-1):
#             self.reset = reset
#             self.sum = reset * self.len if reset >=0 else self.ch[0].sum + self.ch[1].sum
#
#         def pushdown(self):
#             if self.reset < 0: return
#             for i, a, b in ((0, self.left, self.md), (1, self.md, self.right)):
#                 if not self.ch[i]: self.ch[i] = self.__class__(a, b)
#                 self.ch[i].update(self.reset)
#             self.reset = -1
#
#         def set(self, l, r, reset):
#             if r <= self.left or self.right <= l: return 0
#             if l <= self.left and self.right <= r:
#                 self.update(reset)
#             else:
#                 self.pushdown()
#                 for ch in self.ch: ch.set(l, r, reset)
#                 self.update()
#
#         def query(self, l, r):
#             if r <= self.left or self.right <= l: return 0
#             if l <= self.left and self.right <= r:
#                 return self.sum
#             else:
#                 self.pushdown()
#                 return sum(ch.query(l, r) for ch in self.ch)
#
#     def __init__(self):
#         self.root = self.Node(0, int(1e9))
#
#     def addRange(self, left, right):
#         self.root.set(left, right, 1)
#
#     def removeRange(self, left, right):
#         self.root.set(left, right, 0)
#
#     def queryRange(self, left, right):
#         return self.root.query(left, right) == right-left

class Tests(TestCase):
    def test1(self):
        m = RangeModule()
        m.addRange(10, 20)
        m.removeRange(14, 16)
        self.assertEqual(True, m.queryRange(10, 14))
        self.assertEqual(False, m.queryRange(13, 15))
        self.assertEqual(True, m.queryRange(16, 17))

