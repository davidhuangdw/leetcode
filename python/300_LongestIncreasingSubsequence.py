from unittest import TestCase
# https://leetcode.com/problems/longest-increasing-subsequence
import bisect


class LongestIncreasingSubsequence(TestCase):
    def lengthOfLIS(self, nums: 'List[int]') -> 'int':
        n, MAX = len(nums), float("inf")
        ends = [MAX for _ in range(n)]
        for v in nums:
            ends[bisect.bisect_left(ends, v)] = v
        return bisect.bisect_left(ends, MAX) if ends else 0

    def test1(self):
        self.assertEqual(4, self.lengthOfLIS([10,9,2,5,3,7,101,18]))
        

