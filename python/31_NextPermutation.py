from unittest import TestCase
# https://leetcode.com/problems/next-permutation/


class NextPermutation(TestCase):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        lower = next((i for i in range(len(nums)-2, -1, -1) if nums[i] < nums[i+1]), -1)
        if lower >= 0:
            k = next((i for i in range(len(nums)-1, lower, -1) if nums[i] > nums[lower]))
            nums[lower], nums[k] = nums[k], nums[lower]

        i, j = lower+1, len(nums)-1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    def test1(self):
        nums = [1, 2, 3]
        self.nextPermutation(nums)
        self.assertEqual(nums, [1, 3, 2])

    def test2(self):
        nums = [3, 2, 1]
        self.nextPermutation(nums)
        self.assertEqual(nums, [1, 2, 3])

    def test3(self):
        nums = [1, 1, 5]
        self.nextPermutation(nums)
        self.assertEqual(nums, [1, 5, 1])
