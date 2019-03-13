from unittest import TestCase
# https://leetcode.com/problems/search-in-rotated-sorted-array


class SearchInRotatedSortedArray(TestCase):
    def search(self, nums: 'List[int]', target: 'int') -> 'int':
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r) >> 1      # l <= m < r
            if target == nums[m]:
                return m
            if nums[m] < nums[r]:       # m != r
                if nums[m] < target <= nums[r]: l = m+1
                else: r = m-1
            else:
                if nums[l] <= target < nums[m]: r = m-1
                else: l = m+1
        return -1

    def test1(self):
        self.assertEqual(4, self.search([4,5,6,7,0,1,2], 0))

    def test2(self):
        self.assertEqual(-1, self.search([4,5,6,7,0,1,2], 3))

    def test3(self):
        self.assertEqual(1, self.search([3,1], 1))



