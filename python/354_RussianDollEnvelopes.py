from unittest import TestCase
# https://leetcode.com/problems/russian-doll-envelopes/


class RussianDollEnvelopes(TestCase):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        n = len(envelopes)
        ret = 0
        mins = [-1, *[float("inf")]*(n+1)]
        for w, h in sorted(envelopes, key=lambda x: (x[0], -x[1])):
            l, r = 0, n
            while l <= r:
                m = int((l+r)/2)
                if mins[m] < h:
                    l = m + 1
                else:
                    r = m - 1
            mins[l] = h
            ret = max(ret, l)
        return ret

    def test1(self):
        self.assertEqual(3, self.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))




