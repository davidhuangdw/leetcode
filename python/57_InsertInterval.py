from unittest import TestCase
from Definitions import Interval
# https://leetcode.com/problems/insert-interval/

class InsertInterval(TestCase):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        n = len(intervals)
        l = next((i for i in range(n) if intervals[i].end >= newInterval.start), n)
        r = next((i for i in range(n-1, -1, -1) if newInterval.end >= intervals[i].start), -1)

        if l <= r:
            newInterval = Interval(min(newInterval.start, intervals[l].start),
                                   max(newInterval.end, intervals[r].end))
        intervals[l:r+1] = [newInterval]
        return intervals

    def test1(self):
        self.assertEqual([[1,5],[6,9]], Interval.to_array_list(*self.insert(Interval.from_array_list(
            [1,3], [6,9]), Interval(2,5)
        )))

    def test2(self):
        self.assertEqual([[1,2],[3,10],[12,16]], Interval.to_array_list(*self.insert(Interval.from_array_list(
            [1, 2], [3, 5], [6, 7], [8, 10], [12, 16]), Interval(4,8)
        )))


