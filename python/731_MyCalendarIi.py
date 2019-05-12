from unittest import TestCase
# https://leetcode.com/problems/my-calendar-ii
import bisect


class Node:
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end
        self.md = (begin + end)/2
        self._ch = None
        self.extra = self.max = 0

    @property
    def ch(self):
        if not self._ch: self._ch = [Node(self.begin, self.md), Node(self.md, self.end)]
        return self._ch

    def add(self, l, r, v=1):
        if r <= self.begin or self.end <= l:
            return
        if l <= self.begin and self.end <= r:
            self.extra += v
            self.max += v
        else:
            for c in self.ch:
                c.add(l, r)
            self.max = max(self.ch[0].max, self.ch[1].max) + self.extra

    def rangeMax(self, l, r):
        if r <= self.begin or self.end <= l:
            return 0
        if (l <= self.begin and self.end <= r) or not self._ch:
            return self.max
        else:
            return max(self.ch[0].rangeMax(l, r), self.ch[1].rangeMax(l, r)) + self.extra


class MyCalendarTwo:
    def __init__(self):
        self.root = Node(0, int(1e9))

    def book(self, start: 'int', end: 'int') -> 'bool':
        if self.root.rangeMax(start, end) >= 2:
            return False
        self.root.add(start, end)
        return True

# # track overlap
# class MyCalendarTwo:
#     def __init__(self):
#         self.events = []
#         self.overlap = []
#
#     def book(self, start: 'int', end: 'int') -> 'bool':
#         if any(start < r and l < end for l, r in self.overlap):
#             return False
#         for l, r in self.events:
#             if l < end and start < r:
#                 self.overlap.append((max(l, start), min(r, end)))
#         self.events.append((start, end))
#         return True
#
# class MyCalendarTwo:
#     def __init__(self):
#         self.pos = []
#         self.cnt = {}
#
#     def book(self, start: 'int', end: 'int') -> 'bool':
#         i = bisect.bisect_left(self.pos, start)
#         j = bisect.bisect_left(self.pos, end)
#         if any(self.cnt[self.pos[k]] >= 2 for k in range(i, j)):
#             return False
#         if start not in self.cnt:
#             c = self.cnt[self.pos[i-1]] if i-1 >= 0 else 0
#             if c >= 2: return False
#             self.pos[i: i] = [start]
#             j += 1
#             self.cnt[start] = c
#         if end not in self.cnt:
#             self.pos[j: j] = [end]
#             self.cnt[end] = self.cnt[self.pos[j-1]]
#         # print(start, end, i, j, self.pos, self.cnt)
#         for k in range(i, j):
#             self.cnt[self.pos[k]] += 1
#         return True


class MyCalendarTwoTests(TestCase):
    def test1(self):
        c = MyCalendarTwo()
        self.assertEqual(True, c.book(10, 20))
        self.assertEqual(True, c.book(50, 60))
        self.assertEqual(True, c.book(10, 40))
        self.assertEqual(False, c.book(5, 15))
        self.assertEqual(True, c.book(5, 10))
        self.assertEqual(True, c.book(25, 55))

    def test2(self):
        e = [[47,50],[1,10],[27,36],[40,47],[20,27],[15,23],[10,18],[27,36],[17,25],[8,17],[24,33],[23,28],[21,27],[47,50],[14,21],[26,32],[16,21],[2,7],[24,33],[6,13],[44,50],[33,39],[30,36],[6,15],[21,27],[49,50],[38,45],[4,12],[46,50],[13,21]]
        c = MyCalendarTwo()
        for a, b in e:
            c.book(a, b)



# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)

