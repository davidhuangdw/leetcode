from unittest import TestCase
# https://leetcode.com/problems/largest-rectangle-in-histogram


class LargestRectangleInHistogram(TestCase):
    def largestRectangleArea(self, heights: 'List[int]') -> 'int':
        n, pivots, res = len(heights), [], 0
        for i in range(n+1):
            while pivots and (i == n or heights[pivots[-1]] > heights[i]):
                k = pivots.pop()
                res = max(res, (i - 1 - (pivots[-1] if pivots else -1))*heights[k])
            pivots.append(i)
        return res

    def test1(self):
        self.assertEqual(10, self.largestRectangleArea([2,1,5,6,2,3]))


        

