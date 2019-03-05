from unittest import TestCase
# https://leetcode.com/problems/sliding-window-maximum/
import collections


class SlidingWindowMaximum(TestCase):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res, maxes = [], collections.deque()
        for i, v in enumerate(nums):
            while maxes and nums[maxes[-1]] < v:
                maxes.pop()
            maxes.append(i)
            if maxes[0] <= i-k:
                maxes.popleft()
            if i >= k-1:
                res.append(nums[maxes[0]])
        return res

    def test1(self):
        self.assertEqual([3,3,5,5,6,7], self.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))

    def test2(self):
        self.assertEqual([], self.maxSlidingWindow([], 0))
