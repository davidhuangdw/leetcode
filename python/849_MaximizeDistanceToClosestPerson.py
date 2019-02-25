from unittest import TestCase
# https://leetcode.com/problems/maximize-distance-to-closest-person


class MaximizeDistanceToClosestPerson(TestCase):
    def maxDistToClosest(self, seats: 'List[int]') -> 'int':
        j, res = 0, 0
        for i, v in enumerate(seats):
            if v == 1:
                res = max(res, i-j if j == 0 else int((i-j+1)/2))
                j = i+1
        return max(res, len(seats)-j)

    def test1(self):
        self.assertEqual(2, self.maxDistToClosest([1,0,0,0,1,0,1]))

    def test2(self):
        self.assertEqual(2, self.maxDistToClosest([1,0,0,0,1,0,1]))
