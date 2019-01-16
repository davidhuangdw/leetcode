from unittest import TestCase
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/


class LongestIncreasingPathinaMatrix(TestCase):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix: return 0
        n, m = len(matrix), len(matrix[0])
        cache = {}

        def dp(i, j):
            if not cache.get((i, j)):
                cache[(i, j)] = max((dp(ni, nj)+1 for (ni, nj) in ((i, j+1), (i, j-1), (i+1, j), (i-1, j))
                                    if 0 <= ni < n and 0 <= nj < m and matrix[ni][nj] > matrix[i][j]),
                                    default=1)
            return cache[(i, j)]

        return max(dp(i, j) for i in range(n) for j in range(m))

    def test1(self):
        self.assertEqual(4, self.longestIncreasingPath(
            [
                [9, 9, 4],
                [6, 6, 8],
                [2, 1, 1]
            ]
        ))

    def test2(self):
        self.assertEqual(4, self.longestIncreasingPath(
            [
                [3, 4, 5],
                [3, 2, 6],
                [2, 2, 1]
            ]
        ))


