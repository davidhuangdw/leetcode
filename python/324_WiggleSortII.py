from unittest import TestCase
# https://leetcode.com/problems/wiggle-sort-ii/


def wiggled(nums):
    return not any(map(lambda i: nums[i] >= nums[i+1], range(0, len(nums)-1, 2)))


class WiggleSortII(TestCase):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        st = sorted(nums)
        n = len(nums)
        m = int((n+1)/2)
        l, r = st[:m][::-1], st[m:][::-1]
        for (i,v) in enumerate(l):
            nums[i*2] = v
        for (i,v) in enumerate(r):
            nums[i*2+1] = v

    def test1(self):
        nums = [1,2,3,4,5]
        self.wiggleSort(nums)
        self.assertTrue(wiggled(nums))

    def test2(self):
        nums = [4,5,5,6]
        self.wiggleSort(nums)
        self.assertTrue(wiggled(nums))



