from unittest import TestCase
from collections import deque
# https://leetcode.com/problems/sliding-window-maximum/


class SlidingWindowMaximum(TestCase):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ret = []
        maxes = deque()

        for i, v in enumerate(nums):
            if maxes and maxes[0] <= i-k:
                maxes.popleft()
            while maxes and nums[maxes[-1]] < v:
                maxes.pop()
            maxes.append(i)
            if i >= k-1:
                ret.append(nums[maxes[0]])
        return ret

    def test1(self):
        self.assertEqual([3,3,5,5,6,7], self.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))

    def test2(self):
        self.assertEqual([], self.maxSlidingWindow([], 0))
