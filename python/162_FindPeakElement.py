from unittest import TestCase
# https://leetcode.com/problems/find-peak-element/


class FindPeakElement(TestCase):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        l, r = 0, n-1
        while l <= r:
            m = int((r+l)/2)
            if 0 <= m-1 and nums[m-1] > nums[m]:
                r = m-1
            elif m+1 < n and nums[m] < nums[m+1]:
                l = m+1
            else:
                return m
        return -1

    def test1(self):
        self.assertEqual(2, self.findPeakElement([1,2,3,1]))

    def test2(self):
        self.assertIn(self.findPeakElement([1,2,1,3,5,6,4]), [1, 5])
