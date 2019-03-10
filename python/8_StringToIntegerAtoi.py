from unittest import TestCase
# https://leetcode.com/problems/string-to-integer-atoi


class StringToIntegerAtoi(TestCase):
    def myAtoi(self, str: 'str') -> 'int':
        i, n, sign = 0, len(str), 1
        while i < n and str[i] == ' ':
            i += 1
        if i < n and str[i] in '-+':
            if str[i] == '-':
                sign = -1
            i += 1
        if not(i < n and str[i].isdigit()):
            return 0
        while i < n and str[i] == '0':
            i += 1

        j, res = i, 0
        while j < min(n, i+11) and str[j].isdigit():
            res = res*10 + int(str[j])
            j += 1
        res *= sign
        return min(max(res, -(1<<31)), (1<<31)-1)

    def test1(self):
        self.assertEqual(42, self.myAtoi("42"))

    def test2(self):
        self.assertEqual(-42, self.myAtoi("   -42"))

    def test3(self):
        self.assertEqual(4193, self.myAtoi("4193 with words"))

    def test4(self):
        self.assertEqual(0, self.myAtoi("words and 987"))

    def test5(self):
        self.assertEqual(-2147483648, self.myAtoi("-91283472332"))

    def test6(self):
        self.assertEqual(1, self.myAtoi("+1"))

    def test7(self):
        self.assertEqual(12345678, self.myAtoi(" 0000000000012345678"))


        

