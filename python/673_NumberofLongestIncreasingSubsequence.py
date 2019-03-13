from unittest import TestCase
# https://leetcode.com/problems/number-of-longest-increasing-subsequence/
import bisect


class NumberofLongestIncreasingSubsequence(TestCase):
    def findNumberOfLIS(self, nums: 'List[int]') -> 'int':
        n = len(nums)
        ends = [[] for _ in range(n)]
        for num in nums:
            l, r = 0, n-1
            while l <= r:
                m = (l+r) >> 1
                if ends[m] and ends[m][-1][0] < num:
                    l = m+1
                else:
                    r = m-1
            if l-1 >= 0:
                cnt = 0
                for v, c in reversed(ends[l-1]):
                    if v >= num: break
                    cnt += c
            else:
                cnt = 1
            ends[l].append((num, cnt))
        for ed in reversed(ends):
            if ed:
                return sum(map(lambda e: e[1], ed))
        return 0

    # concise
    def findNumberOfLIS(self, nums: 'List[int]') -> 'int':
        n, MAX = len(nums), float("inf")
        ends = [[MAX, []] for _ in range(n)]
        for v in nums:
            i = bisect.bisect_left(ends, [v, []])
            cnt = sum(c for x, c in ends[i-1][1] if x < v) if i else 1
            ends[i][0] = v
            ends[i][1].append((v, cnt))
        return sum(c for v, c in next((cnts for mv, cnts in reversed(ends) if mv != MAX), []))

    def test0(self):
        self.assertEqual(2, self.findNumberOfLIS([1,8,9,7,6,3,4,2,1,7,8,6,5,11,10]))

    def test1(self):
        self.assertEqual(2, self.findNumberOfLIS([1,3,5,4,7]))

    def test2(self):
        self.assertEqual(5, self.findNumberOfLIS([2,2,2,2,2]))
