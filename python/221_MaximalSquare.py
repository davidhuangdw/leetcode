from unittest import TestCase
# https://leetcode.com/problems/maximal-square


class MaximalSquare(TestCase):
    def maximalSquare(self, matrix: 'List[List[str]]') -> 'int':
        if not matrix: return 0
        n, m = len(matrix), len(matrix[0])
        dp, res = [0 for _ in range(m)], 0
        for i in range(n):
            pre = None
            for j in range(m):
                pre_now = dp[j]
                dp[j] = (min(pre, dp[j-1], dp[j])+1 if j else 1) if matrix[i][j] == '1' else 0
                res = max(res, dp[j])
                pre = pre_now
        return res*res

    def test1(self):
        mat = [
            "10100",
            "10110",
            "11110",
            "10100",
        ]
        self.assertEqual(4, self.maximalSquare(mat))


