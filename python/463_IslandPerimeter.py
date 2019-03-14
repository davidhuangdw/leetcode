from unittest import TestCase
# https://leetcode.com/problems/island-perimeter


class IslandPerimeter(TestCase):
    def islandPerimeter(self, grid: 'List[List[int]]') -> int:
        n, m, res = len(grid), len(grid[0]), 0
        for i in range(n):
            for j in range(m):
                if not grid[i][j]: continue
                for ni, nj in ((i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)):
                    if not (0 <= ni < n and 0 <= nj < m and grid[ni][nj]):
                        res += 1
        return res

    # # by test each edge(of two adjacent grid, including border)
    # def islandPerimeter(self, grid: 'List[List[int]]') -> 'int':
    #     return sum(int(x != y) for row in grid + list(map(list, zip(*grid))) for x, y in zip([0]+row, row+[0]))

    def test1(self):
        grid = [[0,1,0,0],
                [1,1,1,0],
                [0,1,0,0],
                [1,1,0,0]]
        self.assertEqual(16, self.islandPerimeter(grid))



