from unittest import TestCase
# https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/


class KthSmallestNumberinMultiplicationTable(TestCase):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        def count(v):
            cnt = 0
            cur = n
            for i in range(1, m+1):
                mul = cur*i
                while mul > v:
                    cur -= 1
                    mul -= i
                cnt += cur
            return cnt

        l, r = 1, m*n
        while l <= r:
            md = ((r-l) >> 1) + l
            if count(md) >= k:
                r = md-1
            else:
                l = md+1
        return l


    def test1(self):
        self.assertEqual(3, self.findKthNumber(3, 3, 5))

    def test2(self):
        self.assertEqual(6, self.findKthNumber(2, 3, 6))
