from unittest import TestCase
# https://leetcode.com/problems/spiral-matrix/


class SpiralMatrix(TestCase):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        if not matrix: return result

        steps = [len(matrix[0]), len(matrix)]

        i, j = 0, -1
        dir = [[0,1], [1,0], [0,-1], [-1,0]]
        d = 0

        while steps[d & 1] > 0:
            di, dj = dir[d & 3]
            for _ in range(steps[d & 1]):
                i += di
                j += dj
                result.append(matrix[i][j])
            d += 1
            steps[d & 1] -= 1
        return result

    def spiralOrder1(self, matrix):         # ...haha
        result = []
        while matrix:
            result += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]
        return result

    def test1(self):
        self.assertEqual([1,2,3,6,9,8,7,4,5], self.spiralOrder([
            [ 1, 2, 3 ],
            [ 4, 5, 6 ],
            [ 7, 8, 9 ]
        ]))

    def test2(self):
        self.assertEqual([1,2,3,4,8,12,11,10,9,5,6,7], self.spiralOrder([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9,10,11,12]
        ]))
