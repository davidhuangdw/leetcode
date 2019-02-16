from unittest import TestCase
# https://leetcode.com/problems/broken-calculator/


class BrokenCalculator(TestCase):
    def brokenCalc(self, X: 'int', Y: 'int') -> 'int':
        cnt = 0
        while Y > X:
            cnt += 1
            if Y & 1:
                Y += 1
            else:
                Y >>= 1
        return cnt + X-Y

    def test1(self):
        self.assertEqual(2, self.brokenCalc(2, 3))

    def test2(self):
        self.assertEqual(2, self.brokenCalc(5, 8))

    def test3(self):
        self.assertEqual(3, self.brokenCalc(3, 10))

    def test4(self):
        self.assertEqual(1023, self.brokenCalc(1024, 1))


