from unittest import TestCase
# https://leetcode.com/problems/house-robber-ii
import collections, itertools


class HouseRobberIi(TestCase):
    def rob(self, nums: 'List[int]') -> 'int':
        n = len(nums)
        if n <= 1: return sum(nums)

        def dp(i):
            pre, now = 0, 0
            for j in range(i, i+n-1):
                pre, now = now, max(now, pre+nums[j])
            return now
        return max(dp(0), dp(1))

    # # for general K case: <=K continuous
    # def rob(self, nums: 'List[int]') -> 'int':
    #     K = 1
    #     n = len(nums)
    #     if n <= K: return sum(nums)
    #     sums = list(itertools.accumulate(nums))
    #
    #     def get_sum(i, j):
    #         return sums[j] - sums[i] + (0 if i <= j else sums[n-1])
    #
    #     def dp(i):      # the case that (i-1)%n is empty
    #         que = collections.deque([0 for _ in range(K+1)])
    #         for d in range(n-1):
    #             que.append(max(que[-u-1] + get_sum((i+d-u)%n, (i+d)%n) for u in range(min(d+2, K+1))))
    #             que.popleft()
    #         return que[-1]
    #     return max(dp(i) for i in range(K+1))


    def test1(self):
        self.assertEqual(3, self.rob([2,3,2]))

    def test2(self):
        self.assertEqual(4, self.rob([1,2,3,1]))


