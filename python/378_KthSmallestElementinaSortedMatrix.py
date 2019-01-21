from unittest import TestCase
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
import heapq


class KthSmallestElementinaSortedMatrix(TestCase):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n, m = len(matrix), len(matrix[0])
        que = [(matrix[0][0], 0, 0)]
        for _ in range(k-1):
            v, i, j = heapq.heappop(que)
            if j+1 < m:
                heapq.heappush(que, (matrix[i][j+1], i, j+1))
            if j == 0 and i+1 < n:
                heapq.heappush(que, (matrix[i+1][j], i+1, j))
        return que[0][0]

    def test1(self):
        self.assertEqual(13, self.kthSmallest(
            [
                [1, 5, 9],
                [10, 11, 13],
                [12, 13, 15]
            ], 8
        ))


