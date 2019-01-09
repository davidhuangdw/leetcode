from unittest import TestCase
# https://leetcode.com/problems/h-index-ii/


class HIndexII(TestCase):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        l, r = 0, n-1
        while l <= r:
            m = int((l+r)/2)
            if citations[m] >= n-m:
                r = m-1
            else:
                l = m+1
        return n-l

    def test1(self):
        self.assertEqual(3, self.hIndex([0,1,3,5,6]))
