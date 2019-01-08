from unittest import TestCase
# https://leetcode.com/problems/basic-calculator/


class BasicCalculator(TestCase):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        def cal(s, i):
            sum = 0
            sign = 1
            num = 0
            while i < len(s) and s[i] != ')':
                if ord('0') <= ord(s[i]) <= ord('9'):
                    num = num*10 + ord(s[i])-ord('0')
                elif s[i] in "+-":
                    sum += sign*num
                    num = 0
                    sign = 1 if s[i] == "+" else -1
                elif s[i] == '(':
                    num, i = cal(s, i+1)
                    sum += sign*num
                    num = 0
                i += 1
            return sum+sign*num, i
        return cal(s, 0)[0]

    def test1(self):
        self.assertEqual(2, self.calculate("1 + 1"))

    def test2(self):
        self.assertEqual(3, self.calculate(" 2-1 + 2 "))

    def test3(self):
        self.assertEqual(23, self.calculate("(1+(4+5+2)-3)+(6+8)"))

    def test4(self):
        self.assertEqual(2, self.calculate("1 - (2-3)"))





