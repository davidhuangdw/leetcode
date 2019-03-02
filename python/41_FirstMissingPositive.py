from unittest import TestCase
# https://leetcode.com/problems/first-missing-positive


class FirstMissingPositive(TestCase):
    def firstMissingPositive(self, nums: 'List[int]') -> 'int':
        n = len(nums)
        for i in range(n):
            j = nums[i]-1
            while 0 < nums[i] <= n and nums[j] != nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                j = nums[i]-1
        for i, v in enumerate(nums):
            if v != i+1:
                return i+1
        return n+1

    def test1(self):
        self.assertEqual(3, self.firstMissingPositive([1,2,0]))

    def test2(self):
        self.assertEqual(2, self.firstMissingPositive([3,4,-1,1]))

    def test3(self):
        self.assertEqual(1, self.firstMissingPositive([7,8,9,11,12]))


