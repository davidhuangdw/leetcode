from unittest import TestCase
from Definitions import Interval
# https://leetcode.com/problems/insert-interval/
import bisect


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

    # # binary search
    # def insert(self, intervals, newInterval):
    #     n = len(intervals)
    #
    #     def bis(op):          # return the index of the first op(interval)==true
    #         l, r = 0, n-1
    #         while l <= r:
    #             m = (l+r) >> 1
    #             if op(intervals[m]):
    #                 r = m - 1
    #             else:
    #                 l = m + 1
    #         return l
    #     i = bis(lambda inv: inv.end >= newInterval.start)
    #     j = bis(lambda inv: inv.start > newInterval.end) - 1
    #     if i <= j:
    #         newInterval.start = min(newInterval.start, intervals[i].start)
    #         newInterval.end = max(newInterval.end, intervals[j].end)
    #     intervals[i: j+1] = [newInterval]
    #     return intervals

    # # bisect
    # def insert(self, intervals, newInterval):
    #     i = bisect.bisect_left([i.end for i in intervals], newInterval.start)
    #     j = bisect.bisect_right([i.start for i in intervals], newInterval.end)-1
    #     if i <= j:
    #         newInterval.start = min(newInterval.start, intervals[i].start)
    #         newInterval.end = max(newInterval.end, intervals[j].end)
    #     intervals[i: j+1] = [newInterval]
    #     return intervals

    def test1(self):
        self.assertEqual([[1,5],[6,9]], Interval.to_array_list(*self.insert(Interval.from_array_list(
            [1,3], [6,9]), Interval(2,5)
        )))

    def test2(self):
        self.assertEqual([[1,2],[3,10],[12,16]], Interval.to_array_list(*self.insert(Interval.from_array_list(
            [1, 2], [3, 5], [6, 7], [8, 10], [12, 16]), Interval(4,8)
        )))


