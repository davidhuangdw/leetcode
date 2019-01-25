from unittest import TestCase
# https://leetcode.com/problems/trapping-rain-water-ii/
import heapq


class TrappingRainWaterII(TestCase):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap: return 0
        n, m = len(heightMap), len(heightMap[0])

        done = set()
        edges = []
        for i in range(n):
            for j in range(m):
                if i == 0 or i == n-1 or j == 0 or j == m-1:
                    done.add((i, j))
                    heapq.heappush(edges, (heightMap[i][j], i, j))

        ret = 0
        while edges:
            cur, i, j = heapq.heappop(edges)
            for (ni, nj) in ((i, j-1), (i, j+1), (i-1, j), (i+1, j)):
                if not (0 <= ni < n and 0 <= nj < m and (ni, nj) not in done):
                    continue
                h = max(cur, heightMap[ni][nj])
                ret += h - heightMap[ni][nj]
                done.add((ni, nj))
                heapq.heappush(edges, (h, ni, nj))
        return ret

    def test1(self):
        self.assertEqual(4, self.trapRainWater([
            [1,4,3,1,3,2],
            [3,2,1,3,2,4],
            [2,3,3,2,3,1]
        ]))

    def test2(self):
        self.assertEqual(14, self.trapRainWater([
            [12,13,1,12],
            [13,4,13,12],
            [13,8,10,12],
            [12,13,12,12],
            [13,13,13,13]
        ]))