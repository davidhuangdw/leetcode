from unittest import TestCase
# https://leetcode.com/problems/burst-balloons/


class BurstBalloons(TestCase):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1, *filter(lambda x: x>0, nums), 1]
        n = len(nums)
        dp = [[0]*n for _ in range(n)]
        for d in range(2, n):
            for l in range(0, n-d):
                r = l+d
                for i in range(l+1, r):
                    dp[l][r] = max(dp[l][r], dp[l][i] + dp[i][r] + nums[l]*nums[i]*nums[r])
        return dp[0][n-1]

    def test1(self):
        self.assertEqual(167, self.maxCoins([3,1,5,8]))