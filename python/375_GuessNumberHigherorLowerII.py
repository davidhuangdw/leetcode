from unittest import TestCase
# https://leetcode.com/problems/guess-number-higher-or-lower-ii/


class GuessNumberHigherorLowerII(TestCase):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0]*(n+1) for _ in range(n+2)]
        for d in range(1, n):
            for i in range(1, n-d+1):
                j = i+d
                dp[i][j] = min(x + max(dp[i][x-1], dp[x+1][j]) for x in range(i, j+1))
        return dp[1][n]

    def test1(self):
        self.assertEqual(10, self.getMoneyAmount(7))

