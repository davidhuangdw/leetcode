from unittest import TestCase
# https://leetcode.com/problems/find-peak-element/


class FindPeakElement(TestCase):
    def findPeakElement(self, nums: 'List[int]') -> int:
        l, r = 0, len(nums)-1
        while l < r:
            m = (r+l) >> 1                  # always l <= m < m+1 <= r
            if nums[m] < nums[m+1]:
                l = m+1
            else:
                r = m
        return l

    def test1(self):
        self.assertEqual(2, self.findPeakElement([1,2,3,1]))

    def test2(self):
        self.assertIn(self.findPeakElement([1,2,1,3,5,6,4]), [1, 5])
