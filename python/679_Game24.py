from unittest import TestCase
# https://leetcode.com/problems/24-game/
import math


class Game24(TestCase):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n == 1:
            return math.isclose(nums[0], 24)
        for i in range(n):
            for j in range(n):
                if i != j:
                    a, b = nums[i], nums[j]
                    rem = [nums[k] for k in range(n) if k not in (i, j)]
                    s = {a+b, a-b, a*b}
                    if b != 0:
                        s.add(a/b)
                    if any(self.judgePoint24(rem+[x]) for x in s):
                        return True
        return False

    def test1(self):
        self.assertEqual(True, self.judgePoint24([4, 1, 8, 7]))

    def test2(self):
        self.assertEqual(False, self.judgePoint24([1, 2, 1, 2]))

    def test3(self):
        self.assertEqual(True, self.judgePoint24([3, 3, 8, 8]))
