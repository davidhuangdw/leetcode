from unittest import TestCase
# https://leetcode.com/problems/patching-array/


class PatchingArray(TestCase):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        ret = 0
        cur = 0
        for v in nums:
            while v > cur+1 and cur < n:
                ret += 1
                cur += cur+1
            cur += v
        while cur < n:
            ret += 1
            cur += cur+1
        return ret

    def test1(self):
        self.assertEqual(1, self.minPatches([1, 3], 6))

    def test2(self):
        self.assertEqual(2, self.minPatches([1, 5, 10], 20))

    def test3(self):
        self.assertEqual(0, self.minPatches([1, 2, 2], 5))
