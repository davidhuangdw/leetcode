from unittest import TestCase
# https://leetcode.com/problems/split-array-largest-sum/


class SplitArrayLargestSum(TestCase):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        n = len(nums)
        sums = [0]
        for v in nums:
            sums.append(sums[-1]+v)
        dp = list(sums)

        for r in range(2, m+1):
            k = n-1
            for i in range(n, r-1, -1):
                def cal(j):
                    return max(dp[j], sums[i]-sums[j])
                while k >= r and cal(k-1) <= cal(k):
                    k -= 1
                dp[i] = cal(k)

        return dp[n]

    def test1(self):
        self.assertEqual(18, self.splitArray([7,2,5,10,8], 2))

