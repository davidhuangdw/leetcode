from unittest import TestCase
# https://leetcode.com/problems/search-a-2d-matrix-ii/


class Search2DMatrixII(TestCase):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix: return False

        n = len(matrix)
        m = len(matrix[0])
        i, j = 0, m-1
        while i<n and 0 <= j:
            if matrix[i][j] == target:
                return True
            elif target < matrix[i][j]:
                j -= 1
            else:
                i += 1
        return False

    def test1(self):
        self.assertEqual(True, self.searchMatrix([
            [1,   4,  7, 11, 15],
            [2,   5,  8, 12, 19],
            [3,   6,  9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]
        ], 5))

    def test2(self):
        self.assertEqual(False, self.searchMatrix([
            [1,   4,  7, 11, 15],
            [2,   5,  8, 12, 19],
            [3,   6,  9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]
        ], 20))