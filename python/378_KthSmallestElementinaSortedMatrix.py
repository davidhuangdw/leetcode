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

        def count_le(v):
            res, j = 0, m-1
            for i in range(n):
                while j >= 0 and matrix[i][j] > v:
                    j -= 1
                res += j+1
            return res
        l, r = matrix[0][0], matrix[n-1][m-1]
        while l <= r:
            md = (l+r) >> 1
            if count_le(md) < k:
                l = md+1
            else:
                r = md-1
        return l

    def test1(self):
        self.assertEqual(13, self.kthSmallest(
            [
                [1, 5, 9],
                [10, 11, 13],
                [12, 13, 15]
            ], 8
        ))


