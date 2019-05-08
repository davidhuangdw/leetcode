from unittest import TestCase
# https://leetcode.com/problems/h-index/


class HIndex(TestCase):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        cnt = [0 for _ in range(n)]
        for c in citations:
            if c < n: cnt[c] += 1
        at_least = n
        for i, c in enumerate(cnt):
            if at_least < i: return i-1
            at_least -= c
        return n - (at_least < n)

    def test1(self):
        self.assertEqual(3, self.hIndex([3,0,6,1,5]))
