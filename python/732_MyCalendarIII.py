from unittest import TestCase
# https://leetcode.com/problems/my-calendar-iii/


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


class Tests(TestCase):
    def test1(self):
        c = MyCalendarThree()
        self.assertEqual(1, c.book(10, 20))
        self.assertEqual(1, c.book(50, 60))
        self.assertEqual(2, c.book(10, 40))
        self.assertEqual(3, c.book(5, 15))
        self.assertEqual(3, c.book(5, 10))
        self.assertEqual(3, c.book(25, 55))



