from unittest import TestCase
# https://leetcode.com/problems/max-area-of-island
import collections


class MaxAreaOfIsland(TestCase):
    def maxAreaOfIsland(self, grid: 'List[List[int]]') -> 'int':
        parent, area = {}, {}

        def find(x):
            if x not in parent:
                return None
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx and ry and rx != ry:
                parent[rx] = ry
                area[ry] += area[rx]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    x = (i, j)
                    parent[x] = x
                    area[x] = 1
                    union((i-1, j), x)
                    union((i, j-1), x)
        return max(area.values(), default=0)

    # # by dfs:
    # def maxAreaOfIsland(self, grid: 'List[List[int]]') -> 'int':
    #     n, m = len(grid), len(grid[0])
    #
    #     def dfs(i, j):
    #         if 0 <= i < n and 0 <= j < m and grid[i][j]:
    #             grid[i][j] = 0
    #             return 1 + dfs(i-1, j) + dfs(i+1, j) + dfs(i, j-1) + dfs(i, j+1)
    #         return 0
    #     return max((dfs(i, j) for i in range(n) for j in range(m)), default=0)

    # by bfs:
    # def maxAreaOfIsland(self, grid: 'List[List[int]]') -> 'int':
    #     n, m = len(grid), len(grid[0])
    #
    #     def has_one(i, j):
    #         return 0 <= i < n and 0 <= j < m and grid[i][j]
    #
    #     def bfs(i, j):
    #         if not has_one(i, j): return 0
    #         que, area, grid[i][j] = collections.deque([(i, j)]), 1, 0
    #         while que:
    #             i, j = que.popleft()
    #             for ni, nj in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
    #                 if has_one(ni, nj):
    #                     grid[ni][nj] = 0
    #                     area += 1
    #                     que.append((ni, nj))
    #         return area
    #     return max((bfs(i, j) for i in range(n) for j in range(m)), default=0)

    def test1(self):
        self.assertEqual(6, self.maxAreaOfIsland(
            [[0,0,1,0,0,0,0,1,0,0,0,0,0],
             [0,0,0,0,0,0,0,1,1,1,0,0,0],
             [0,1,1,0,1,0,0,0,0,0,0,0,0],
             [0,1,0,0,1,1,0,0,1,0,1,0,0],
             [0,1,0,0,1,1,0,0,1,1,1,0,0],
             [0,0,0,0,0,0,0,0,0,0,1,0,0],
             [0,0,0,0,0,0,0,1,1,1,0,0,0],
             [0,0,0,0,0,0,0,1,1,0,0,0,0]]
        ))

    def test2(self):
        self.assertEqual(0, self.maxAreaOfIsland(
            [[0, 0, 0, 0, 0, 0, 0, 0]]
        ))

    def test3(self):
        self.assertEqual(4, self.maxAreaOfIsland(
            [[1, 1, 0, 0, 0],
             [1, 1, 0, 0, 0],
             [0, 0, 0, 1, 1],
             [0, 0, 0, 1, 1]]
        ))

