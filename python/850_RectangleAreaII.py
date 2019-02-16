from unittest import TestCase
# https://leetcode.com/problems/rectangle-area-ii/


class Node:
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end
        self.md = (begin+end) >> 1
        self.left = self.right = None
        self.cnt = self.len = 0

    def update(self, l, r, v):
        if r <= self.begin or self.end <= l:
            return
        if not self.left: self.left = Node(self.begin, self.md)
        if not self.right: self.right = Node(self.md, self.end)
        if l <= self.begin and self.end <= r:
            self.cnt += v
        else:
            self.left.update(l, r, v)
            self.right.update(l, r, v)
        self.len = self.end - self.begin if self.cnt > 0 else self.left.len + self.right.len


class RectangleAreaII(TestCase):
    def rectangleArea(self, rectangles: 'List[List[int]]') -> 'int':
        if not rectangles: return 0
        intervals = []
        for x1, y1, x2, y2 in rectangles:
            intervals.append((x1, y1, y2, 1))
            intervals.append((x2, y1, y2, -1))
        intervals.sort()
        root = Node(0, int(1e9))
        pre, res = 0, 0
        for x, y1, y2, v in intervals:
            res += (x-pre)*root.len
            pre = x
            root.update(y1, y2, v)
        return res % (int(1e9)+7)

    def test1(self):
        self.assertEqual(6, self.rectangleArea([[0,0,2,2],[1,0,2,3],[1,0,3,1]]))

    def test2(self):
        self.assertEqual(49, self.rectangleArea([[0,0,1000000000,1000000000]]))





