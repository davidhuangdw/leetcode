from unittest import TestCase
# https://leetcode.com/problems/fraction-to-recurring-decimal/


class FractiontoRecurringDecimal(TestCase):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if not numerator:
            return "0"
        flag = 1
        if numerator < 0:
            numerator *= -1
            flag *= -1
        if denominator < 0:
            denominator *= -1
            flag *= -1
        neg = "-" if flag == -1 else ""
        integer = int(numerator/denominator)
        remain = numerator - integer*denominator
        if not remain:
            return f"{neg}{integer}"

        occur = {}
        decimals = ""
        while remain and remain not in occur:
            occur[remain] = len(decimals)
            remain *= 10
            mul = int(remain/denominator)
            decimals += str(mul)
            remain -= mul*denominator

        if remain:
            return f"{neg}{integer}.{decimals[:occur[remain]]}({decimals[occur[remain]:]})"
        else:
            return f"{neg}{integer}.{decimals}"

    def test1(self):
        self.assertEqual("0.5", self.fractionToDecimal(1, 2))

    def test2(self):
        self.assertEqual("2", self.fractionToDecimal(2, 1))

    def test3(self):
        self.assertEqual("0.(6)", self.fractionToDecimal(2, 3))

    def test4(self):
        self.assertEqual("0.(012)", self.fractionToDecimal(4, 333))

    def test5(self):
        self.assertEqual("-6.25", self.fractionToDecimal(-50, 8))

    def test6(self):
        self.assertEqual("-2147483648", self.fractionToDecimal(-2147483648, 1))

    def test6(self):
        self.assertEqual("0", self.fractionToDecimal(0, -1))
