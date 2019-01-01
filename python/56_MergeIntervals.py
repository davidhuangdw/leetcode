from unittest import TestCase
from Definitions import Interval
# https://leetcode.com/problems/merge-intervals/


class MergeIntervals(TestCase):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals: return []

        result = []
        intervals = sorted(intervals, key=lambda x: (x.start, x.end))
        join = intervals[0]
        for v in intervals:
            if v.start <= join.end:
                join.end = max(join.end, v.end)
            else:
                result.append(join)
                join = v
        result.append(join)
        return result

    def test1(self):
        self.assertEqual([[1,6],[8,10],[15,18]], Interval.to_array_list(*self.merge(Interval.from_array_list(
            [1,3],[2,6],[8,10],[15,18]
            ))))

    def test2(self):
        self.assertEqual([[1,5]], Interval.to_array_list(*self.merge(Interval.from_array_list(
            [1,4], [4,5]
            ))))
