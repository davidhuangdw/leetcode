from unittest import TestCase
# https://leetcode.com/problems/range-module/


class RangeModule:
    def __init__(self):
        self.ranges = []

    def addRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void
        """
        n = len(self.ranges)
        i, j = 0, n-1
        while i < n and self.ranges[i][1] < left:
            i += 1
        while j >= 0 and self.ranges[j][0] > right:
            j -= 1
        if i <= j:
            left = min(left, self.ranges[i][0])
            right = max(right, self.ranges[j][1])
        self.ranges[i:j+1] = [[left, right]]

    def queryRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: bool
        """
        n = len(self.ranges)
        l, r = 0, n-1
        while l <= r:
            m = (l+r) >> 1
            if self.ranges[m][0] <= left:
                l = m+1
            else:
                r = m-1
        return r >= 0 and self.ranges[r][1] >= right

    def removeRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void
        """
        n = len(self.ranges)
        i, j = 0, n-1
        while i < n and self.ranges[i][1] <= left:
            i += 1
        while j >= 0 and self.ranges[j][0] >= right:
            j -= 1
        if i <= j:
            md = []
            if self.ranges[i][0] < left:
                md.append([self.ranges[i][0], left])
            if right < self.ranges[j][1]:
                md.append([right, self.ranges[j][1]])
            self.ranges[i:j+1] = md


class Tests(TestCase):
    def test1(self):
        m = RangeModule()
        m.addRange(10, 20)
        m.removeRange(14, 16)
        self.assertEqual(True, m.queryRange(10, 14))
        self.assertEqual(False, m.queryRange(13, 15))
        self.assertEqual(True, m.queryRange(16, 17))

