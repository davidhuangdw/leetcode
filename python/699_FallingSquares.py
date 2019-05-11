from unittest import TestCase
# https://leetcode.com/problems/falling-squares/
import bisect

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

    # # naive
    # def fallingSquares(self, positions: 'List[List[int]]') -> 'List[int]':
    #     global index
    #     axis = set(x for l, h in positions for x in (l, l+h))
    #     index = {v: i for i, v in enumerate(sorted(axis))}
    #
    #     res = []
    #     cur = [0 for _ in range(len(axis))]
    #     for l, h in positions:
    #         l, r = index[l], index[l+h]
    #         h += max(cur[l:r])
    #         for i in range(l, r): cur[i] = h
    #         res.append(max(res[-1], h) if res else h)
    #     return res
    #
    # # naive condensed: only need to store left info
    # def fallingSquares(self, positions: 'List[List[int]]') -> 'List[int]':
    #     global index
    #     axis = set(x for l, h in positions for x in (l, l+h))
    #     index = {v: i for i, v in enumerate(sorted(axis))}
    #
    #     res, INF = [], float("inf")
    #     cur = [(0, 0)]
    #     for l, h in positions:
    #         l, r = index[l], index[l+h]
    #         i = bisect.bisect_right(cur, (l, INF))
    #         j = bisect.bisect_left(cur, (r, -1))
    #         cover = cur[i-1:j]
    #         h += max((h for l, h in cover), default=0)
    #         res.append(max(res[-1], h) if res else h)
    #         cur[i:j] = [(l, h), (r, cover[-1][1] if cover else 0)]
    #     return res

    def test1(self):
        self.assertEqual([2, 5, 5], self.fallingSquares([[1, 2], [2, 3], [6, 1]]))

    def test2(self):
        self.assertEqual([100, 100], self.fallingSquares([[100, 100], [200, 100]]))

    def test3(self):
        self.assertEqual([5, 7, 7], self.fallingSquares([[1,5],[2,2],[7,5]]))

