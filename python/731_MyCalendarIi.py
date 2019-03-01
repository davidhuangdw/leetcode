from unittest import TestCase
# https://leetcode.com/problems/my-calendar-ii


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


class MyCalendarTwoTests(TestCase):
    def test1(self):
        c = MyCalendarTwo()
        self.assertEqual(True, c.book(10, 20))
        self.assertEqual(True, c.book(50, 60))
        self.assertEqual(True, c.book(10, 40))
        self.assertEqual(False, c.book(5, 15))
        self.assertEqual(True, c.book(5, 10))
        self.assertEqual(True, c.book(25, 55))



# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)

