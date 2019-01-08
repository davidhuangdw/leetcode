from unittest import TestCase
from heapq import *
# https://leetcode.com/problems/the-skyline-problem/


class TheSkylineProblem(TestCase):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        points = []
        for b in buildings:
            x, y, h = b
            points.append((x, -h))
            points.append((y, h))
        points.sort()
        count = {}
        heap = []

        def peek():
            while len(heap) > 0 and not count[heap[0]]:
                heappop(heap)
            return heap[0] if len(heap) > 0 else 0

        result = []
        for p in points:
            last = peek()
            x, h = p
            if h < 0:   # up
                count[h] = count.get(h, 0) + 1
                heappush(heap, h)
            else:
                h = -h  # due to heapq is min-heap
                count[h] -= 1
            cur = peek()
            if cur != last:
                result.append([x, -cur])
        return result

    def test1(self):
        self.assertEqual([[2, 10], [3,15], [7,12], [12,0], [15,10], [20,8], [24,0]], self.getSkyline(
            [[2,9,10], [3,7,15], [5,12,12], [15,20,10], [19,24,8]]
        ))

    def test2(self):
        self.assertEqual([[2, 7], [4, 0]], self.getSkyline(
            [[2, 4, 7], [2, 4, 5], [2, 4, 6]]
        ))

    def test3(self):
        self.assertEqual([[0, 3], [5, 0]], self.getSkyline(
            [[0, 2, 3], [2, 5, 3]]
        ))
