from unittest import TestCase
# https://leetcode.com/problems/find-median-from-data-stream
from heapq import *


class FindMedianfromDataStream:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.heaps = [], []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        lque, rque = self.heaps
        if len(lque) == 0 or num <= -lque[0]:
            heappush(lque, -num)
            if len(lque) - len(rque) > 1:
                heappush(rque, -heappop(lque))
        else:
            heappush(rque, num)
            if len(rque) > len(lque):
                heappush(lque, -heappop(rque))

    def findMedian(self):
        """
        :rtype: float
        """
        l, r = self.heaps
        return (-l[0]+r[0])/2 if len(l) == len(r) else -l[0]


class Tests(TestCase):
    def test1(self):
        med = FindMedianfromDataStream()
        med.addNum(1)
        med.addNum(2)
        self.assertEqual(1.5, med.findMedian())
        med.addNum(4)
        self.assertEqual(2, med.findMedian())
