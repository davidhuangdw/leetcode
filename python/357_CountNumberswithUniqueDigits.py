from unittest import TestCase
# https://leetcode.com/problems/count-numbers-with-unique-digits/


class CountNumberswithUniqueDigits(TestCase):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        muls = [9, *range(9, 0, -1)]
        ret = 1
        mul = 1
        for i in range(min(n, 10)):
            mul *= muls[i]
            ret += mul
        return ret

    def test1(self):
        self.assertEqual(91, self.countNumbersWithUniqueDigits(2))
