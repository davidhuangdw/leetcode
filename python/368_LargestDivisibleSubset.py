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

    # def largestDivisibleSubset(self, nums):
    #     nums.sort()
    #     dp, res = {}, []
    #     for v in nums:
    #         dp[v] = max(((1+dp[k][0], k) for k in dp if v % k == 0), default=(1,0))
    #     x = max(dp, key=lambda k: dp[k], default=0)
    #     while x > 0:
    #         res.append(x)
    #         x = dp[x][1]
    #     return res[::-1]

    def test1(self):
        self.assertEqual([1,2], self.largestDivisibleSubset([1, 2, 3]))

    def test2(self):
        self.assertEqual([1,2,4,8], self.largestDivisibleSubset([1,2,4,8]))

