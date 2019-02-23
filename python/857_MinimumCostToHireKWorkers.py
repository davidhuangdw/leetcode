from unittest import TestCase
# https://leetcode.com/problems/minimum-cost-to-hire-k-workers
import heapq


class MinimumCostToHireKWorkers(TestCase):
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        workers = sorted(zip(quality, wage), key=lambda x: x[1]/x[0])
        que = []
        s = 0
        res = float("inf")
        for q, w in workers:
            r = w/q
            heapq.heappush(que, -q)
            s += -q
            if len(que) > K:
                s -= heapq.heappop(que)
            if len(que) == K:
                res = min(res, -r*s)
        return res

    def test1(self):
        self.assertAlmostEqual(105.0, self.mincostToHireWorkers([10,20,5], [70,50,30], 2))

    def test2(self):
        self.assertAlmostEqual(30.6666667, self.mincostToHireWorkers([3,1,10,10,1], [4,8,2,2,7], 3))


