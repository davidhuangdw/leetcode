from unittest import TestCase
# https://leetcode.com/problems/largest-divisible-subset/


class LargestDivisibleSubset(TestCase):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = sorted(nums)
        dp = []
        for i in range(len(nums)):
            dp.append(max((dp[j] for j in range(i) if nums[i] % nums[j] == 0), key=len, default=[]) + [nums[i]])
        return max(dp, key=len, default=[])

    def test1(self):
        self.assertEqual([1,2], self.largestDivisibleSubset([1, 2, 3]))

    def test2(self):
        self.assertEqual([1,2,4,8], self.largestDivisibleSubset([1,2,4,8]))

