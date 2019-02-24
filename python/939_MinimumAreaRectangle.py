from unittest import TestCase
# https://leetcode.com/problems/minimum-area-rectangle
import collections


class MinimumAreaRectangle(TestCase):
    def minAreaRect(self, points: 'List[List[int]]') -> 'int':
        def merge(a, b):
            b = set(b)
            return [x for x in a if x in b]

        ylist = collections.defaultdict(list)
        for x, y in sorted(points):
            ylist[x].append(y)
        ylist = list(ylist.items())
        n, res = len(ylist), float("inf")
        for i in range(n):
            for j in range(i+1, n):
                lx, lys = ylist[i]
                rx, rys = ylist[j]
                ys = merge(lys, rys)
                if len(ys) < 2: continue
                res = min(res, (rx-lx)*min(b-a for a, b in zip(ys, ys[1:])))
        return 0 if res == float("inf") else res

    def test1(self):
        self.assertEqual(4, self.minAreaRect([[1,1],[1,3],[3,1],[3,3],[2,2]]))

    def test2(self):
        self.assertEqual(2, self.minAreaRect([[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]))

    def test3(self):
        self.assertEqual(6365616, self.minAreaRect([[36219,4673],[26311,36047],[26311,4673],[36219,16024],[17010,16024],[26311,6287],[22367,6287],[17010,36047],[17010,6287],[22367,16024],[36219,6287],[22367,4673],[17010,4673],[36219,36047]]
))

        

