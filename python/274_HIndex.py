from unittest import TestCase
# https://leetcode.com/problems/h-index/


class HIndex(TestCase):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        cnt = [0]*(n+1)
        for c in citations:
            cnt[min(c, n)] += 1
        sum = 0
        for i in range(n, 0, -1):
            sum += cnt[i]
            if sum >= i:
                return i
        return 0

    def test1(self):
        self.assertEqual(3, self.hIndex([3,0,6,1,5]))
