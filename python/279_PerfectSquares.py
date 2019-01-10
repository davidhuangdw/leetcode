from unittest import TestCase
# https://leetcode.com/problems/perfect-squares/


class PerfectSquares(TestCase):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        squares = [i*i for i in range(1, int(n ** 0.5)+1)]
        cnt = [n]*(n+1)
        cnt[0] = 0
        for x in range(n):
            for s in squares:
                v = x+s
                if v > n: break
                cnt[v] = min(cnt[v], cnt[x]+1)
        return cnt[n]

    def test1(self):
        self.assertEqual(3, self.numSquares(12))

    def test2(self):
        self.assertEqual(2, self.numSquares(13))
