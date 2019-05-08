from unittest import TestCase
# https://leetcode.com/problems/count-numbers-with-unique-digits/


class CountNumberswithUniqueDigits(TestCase):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret, mul = 1, 1
        for k in [9, *range(9, 0, -1)][:n]:
            mul *= k
            ret += mul
        return ret

    def test1(self):
        self.assertEqual(91, self.countNumbersWithUniqueDigits(2))
