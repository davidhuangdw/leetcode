from unittest import TestCase
# https://leetcode.com/problems/split-array-largest-sum/
import itertools


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

    # # O(n*logV) BS
    # def splitArray(self, nums, m):
    #     l, r, n = max(nums), sum(nums), len(nums)
    #     while l <= r:
    #         md = (l+r) >> 1
    #         k, pre = 1, 0
    #         for v in nums:
    #             pre += v
    #             if pre <= md: continue
    #             k += 1
    #             if k > m: break
    #             pre = v
    #         if k <= m:
    #             r = md-1
    #         else:
    #             l = md+1
    #     return l
    #
    # # O(n*m)t, O(n)s dp: d(i,m) = min{max(s[j+1, i], d(j,m-1)) | j<i }, the selected k is non-decrease to i
    # def splitArray(self, nums, m):
    #     k, n = 0, len(nums)
    #     sums = list(itertools.accumulate(nums))
    #     dp = list(sums)
    #
    #     def cal(i, k):
    #         return max(sums[i] - sums[k], dp[k]) if k >= 0 else sums[i]
    #     for r in range(2, m+1):
    #         k = n-1
    #         for i in range(n-1, -1, -1):
    #             while k and (k >= i or cal(i, k-1) <= cal(i, k)):   # bug: <= not <, otherwise k won't across ==
    #                 k -= 1
    #             dp[i] = cal(i, k)
    #     return dp[n-1]


    def test1(self):
        self.assertEqual(18, self.splitArray([7,2,5,10,8], 2))

