from unittest import TestCase
# https://leetcode.com/problems/rotate-image


class RotateImage(TestCase):
    # def rotate(self, matrix: 'List[List[int]]') -> 'None':
    #     """
    #     Do not return anything, modify matrix in-place instead.
    #     """
    #     def swap(xi, xj, yi, yj):
    #         matrix[xi][xj], matrix[yi][yj] = matrix[yi][yj], matrix[xi][xj]
    #     n = len(matrix)
    #     for a in range(n >> 1):
    #         b = n-1-a
    #         for j in range(0, b-a):
    #             swap(a, a+j, a+j, b)
    #             swap(a, a+j, b, b-j)
    #             swap(a, a+j, b-j, a)

    # # by flip twice
    # def rotate(self, matrix: 'List[List[int]]') -> 'None':
    #     def swap(xi, xj, yi, yj):
    #         matrix[xi][xj], matrix[yi][yj] = matrix[yi][yj], matrix[xi][xj]
    #     n = len(matrix)
    #     for i in range(n >> 1):
    #         for j in range(n):
    #             swap(i, j, n-1-i, j)
    #     for i in range(n):
    #         for j in range(i):
    #             swap(i, j, j, i)

    # by index without offset: (i, j) -> (j, n-1-i) -> (n-1-i, n-1-j) -> (n-1-j, i)
    def rotate(self, matrix: 'List[List[int]]') -> 'None':
        def swap(xi, xj, yi, yj):
            matrix[xi][xj], matrix[yi][yj] = matrix[yi][yj], matrix[xi][xj]
        n = len(matrix)
        for i in range(n >> 1):
            for j in range(i, n-1-i):
                ni, nj = j, n-1-i
                for _ in range(3):
                    swap(i, j, ni, nj)
                    ni, nj = nj, n-1-ni

    def test1(self):
        x = [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]
        y = [
            [7,4,1],
            [8,5,2],
            [9,6,3]
        ]
        self.rotate(x)
        self.assertEqual(y, x)

    def test2(self):
        x = [
            [ 5, 1, 9,11],
            [ 2, 4, 8,10],
            [13, 3, 6, 7],
            [15,14,12,16]
        ]
        y = [
            [15,13, 2, 5],
            [14, 3, 4, 1],
            [12, 6, 8, 9],
            [16, 7,10,11]
        ]
        self.rotate(x)
        self.assertEqual(y, x)


        

