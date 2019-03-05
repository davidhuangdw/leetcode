from unittest import TestCase
# https://leetcode.com/problems/unique-paths


class UniquePaths(TestCase):
    # f(i, j) = f(i-1, j) + f(i, j-1)
    def uniquePaths(self, m: int, n: int) -> int:
        if m < n: n, m = m, n
        dp = [1 for _ in range(n)]
        for _ in range(m - 1):
            for i in range(1, n):
                dp[i] += dp[i - 1]
        return dp[n - 1]

    # # by math: C(n+m-2, m-1): (n+m-2) steps, m-1 downs
    # def uniquePaths(self, m: int, n: int) -> int:
    #     if n > m:
    #         n, m = m, n
    #     a = b = 1
    #     for i in range(1, n):
    #         a *= m-1+i
    #         b *= i
    #     return int(a/b)

    def test1(self):
        self.assertEqual(28, self.uniquePaths(7, 3))
