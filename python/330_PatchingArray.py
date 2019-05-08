from unittest import TestCase
# https://leetcode.com/problems/patching-array/


class PatchingArray(TestCase):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        x = i = ret = 0
        while x < n:
            if i < len(nums) and nums[i] <= x+1:
                x += nums[i]
                i += 1
            else:
                ret += 1
                x += x+1
        return ret

    def test1(self):
        self.assertEqual(1, self.minPatches([1, 3], 6))

    def test2(self):
        self.assertEqual(2, self.minPatches([1, 5, 10], 20))

    def test3(self):
        self.assertEqual(0, self.minPatches([1, 2, 2], 5))
