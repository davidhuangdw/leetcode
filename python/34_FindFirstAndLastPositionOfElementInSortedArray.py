from unittest import TestCase
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array
import bisect


class FindFirstAndLastPositionOfElementInSortedArray(TestCase):
    def searchRange(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        l = bisect.bisect_left(nums, target)
        return [l, bisect.bisect_right(nums, target)-1] if l < len(nums) and nums[l] == target else [-1, -1]

    def test1(self):
        self.assertEqual([3,4], self.searchRange([5,7,7,8,8,10], 8))

    def test2(self):
        self.assertEqual([-1,-1], self.searchRange([5,7,7,8,8,10], 6))


