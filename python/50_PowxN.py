from unittest import TestCase
# https://leetcode.com/problems/powx-n


class PowxN(TestCase):
    def myPow(self, x: 'float', n: 'int') -> 'float':
        res, mul, k = 1.0, x, abs(n)
        while k:
            if k & 1:
                res *= x
            x *= x
            k >>= 1
        return res if n >= 0 else 1/res

    # # recursive
    # def myPow(self, x: 'float', n: 'int') -> 'float':
    #     if n < 0: return 1/self.myPow(x, -n)
    #     if n == 0: return 1.0
    #     return (x if n & 1 else 1.0) * self.myPow(x*x, n>>1)

    def test1(self):
        self.assertAlmostEqual(1024.00000, self.myPow(2.00000, 10))

    def test2(self):
        self.assertAlmostEqual(9.26100, self.myPow(2.10000, 3))

    def test3(self):
        self.assertAlmostEqual(0.25000, self.myPow(2.00000, -2))

    def test4(self):
        self.assertAlmostEqual(1.0, self.myPow(0.9, 0))

