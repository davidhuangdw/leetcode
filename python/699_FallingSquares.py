from unittest import TestCase
# https://leetcode.com/problems/falling-squares/

index = []


class FallingSquares(TestCase):
    class Node:
        def __init__(self, begin, end):
            self._begin, self._end = begin, end
            self._md = (begin + end) >> 1
            self.reset = self._max = 0
            self.left = self.right = None

        @property
        def max(self):
            return self.reset if self.reset is not None else self._max

        @property
        def begin(self):
            return index[self._begin]

        @property
        def end(self):
            return index[self._end]

        def pushdown(self):
            if self.reset is not None:
                self.right.reset = self.left.reset = self.reset
                self.reset = None

        def query(self, l, r):
            if r <= self.begin or self.end <= l:
                return 0
            if self.reset is not None:
                return self.reset
            if l <= self.begin and self.end <= r:
                return self._max
            else:
                return max(self.left.query(l, r), self.right.query(l, r))

        def update(self, l, r, reset):
            if r <= self.begin or self.end <= l:
                return
            if l <= self.begin and self.end <= r:
                self.reset = reset
            else:
                if not self.left: self.left = self.__class__(self._begin, self._md)
                if not self.right: self.right = self.__class__(self._md, self._end)
                self.pushdown()
                self.left.update(l, r, reset)
                self.right.update(l, r, reset)
                self._max = max(self.left.max, self.right.max)

    def fallingSquares(self, positions: 'List[List[int]]') -> 'List[int]':
        global index
        index = list(sorted(set(x for l, dis in positions for x in (l, l+dis))))
        root = self.Node(0, len(index)-1)

        res = []
        for l, dis in positions:
            r = l + dis
            h = root.query(l, r)
            root.update(l, r, h+dis)
            res.append(root.max)
        return res

    def test1(self):
        self.assertEqual([2, 5, 5], self.fallingSquares([[1, 2], [2, 3], [6, 1]]))

    def test2(self):
        self.assertEqual([100, 100], self.fallingSquares([[100, 100], [200, 100]]))

