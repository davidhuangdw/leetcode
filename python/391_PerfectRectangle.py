from unittest import TestCase
# https://leetcode.com/problems/perfect-rectangle/


class PerfectRectangle(TestCase):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        def area(lx, ly, rx, ry):
            return (ry - ly)*(rx-lx)

        def corners(lx, ly, rx, ry):
            return {(lx, ly), (lx, ry), (rx, ly), (rx, ry)}

        sum = 0
        xor = set()
        for r in rectangles:
            sum += area(*r)
            xor ^= corners(*r)
        a, b, c, d = zip(*rectangles)
        whole = (min(a), min(b), max(c), max(d))
        return sum == area(*whole) and xor == corners(*whole)

    def test1(self):
        self.assertEqual(True, self.isRectangleCover([
            [1,1,3,3],
            [3,1,4,2],
            [3,2,4,4],
            [1,3,2,4],
            [2,3,3,4]
        ]))

    def test2(self):
        self.assertEqual(False, self.isRectangleCover([
            [1, 1, 3, 3],
            [3, 1, 4, 2],
            [1, 3, 2, 4],
            [3, 2, 4, 4]
        ]))

    def test3(self):
        self.assertEqual(False, self.isRectangleCover([
            [1, 1, 3, 3],
            [3, 1, 4, 2],
            [1, 3, 2, 4],
            [2, 2, 4, 4]
        ]))

