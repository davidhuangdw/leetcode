from unittest import TestCase
# https://leetcode.com/problems/partition-equal-subset-sum


class PartitionEqualSubsetSum(TestCase):
    # dp using set: O(n*m) time and O(m) space
    def canPartition(self, nums: 'List[int]') -> bool:
        s = sum(nums)
        if s % 2: return False
        half, valids = s >> 1, {0}
        for v in sorted(nums, reverse=True):        # optimization: larger first
            if v > half: continue
            for x in list(valids):
                now = x + v
                if now == half: return True
                if now < half: valids.add(now)
        return False

    # # dfs(top-down dp): O(n*m) time and space, fastest
    # def canPartition(self, nums: 'List[int]') -> bool:
    #     s, n = sum(nums), len(nums)
    #     if s % 2: return False
    #     half, nums, done = s >> 1, sorted(nums), set()      # optimization: larger first
    #
    #     def dfs(tar, i):
    #         if tar == 0: return True
    #         if i < 0 or tar < 0 or (tar, i) in done: return False
    #         done.add((tar, i))
    #         return dfs(tar-nums[i], i-1) or dfs(tar, i-1)
    #     return dfs(s >> 1, n-1)
    #
    # # normal dp
    # def canPartition(self, nums: 'List[int]') -> bool:
    #     s, n = sum(nums), len(nums)
    #     if s % 2: return False
    #     half, dp = s>>1, [False for _ in range((s>>1) + 1)]
    #     dp[0] = True
    #     for v in sorted(nums, reverse=True):    # optimization: larger first
    #         for x in range(half, v-1, -1):
    #             dp[x] = dp[x] or dp[x-v]
    #         if dp[half]: return True
    #     return False

    def test1(self):
        self.assertEqual(True, self.canPartition([97,100,88,49,43,55,2,62,72,13,60,36,67,64,13,39,66,6,26,45,46,75,28,66,71,75,91,33,64,54,3,76,76,35,49,6,63,11,80,86,73,95,60,58,61,42,52,27,73,51,58,38,28,62,84,55,90,40,52,96,55,32,52,63,44,90,14,68,50,32,73,64,92,74,66,64,22,51,27,30,83,30,37,25,22,46,95,59,57,21,29,72,7,56,47,48,54,75,67,33]))

    def test2(self):
        self.assertEqual(False, self.canPartition([1, 2, 3, 5]))


