from unittest import TestCase
# https://leetcode.com/problems/combination-sum-iv/


class CombinationSumIV(TestCase):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [1, *[0]*target]
        for t in range(1, target+1):
            for num in nums:
                if t-num >= 0:
                    dp[t] += dp[t-num]
        return dp[target]

    def test1(self):
        self.assertEqual(7, self.combinationSum4([1,2,3], 4))
