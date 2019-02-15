from unittest import TestCase
# https://leetcode.com/problems/bricks-falling-when-hit/


class BricksFallingWhenHit:
    class UnionSet:
        def __init__(self):
            self.info = dict()  # value: (size, isTop)
            self.parent = dict()

        def create(self, pos):
            self.parent[pos] = pos
            self.info[pos] = (1, pos[0] == 0)

        def find(self, pos):
            if self.parent[pos] != pos:
                self.parent[pos] = self.find(self.parent[pos])
            return self.parent[pos]

        def union(self, pa, pb):
            ra, rb = self.find(pa), self.find(pb)
            if ra == rb: return
            sa, ta = self.info[ra]
            sb, tb = self.info[rb]
            self.parent[rb] = ra
            self.info[ra] = (sa+sb, ta or tb)

    def hitBricks(self, grid: 'List[List[int]]', hits: 'List[List[int]]') -> 'List[int]':
        s = self.UnionSet()
        n, m = len(grid), len(grid[0])
        for h in hits:
            i, j = h
            if grid[i][j] == 1:
                grid[i][j] = 0
            else:
                h[0] = -1   # invalidate

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    s.create((i, j))
                    if i-1 >= 0 and grid[i-1][j] == 1:
                        s.union((i-1, j), (i, j))
                    if j-1 >= 0 and grid[i][j-1] == 1:
                        s.union((i, j-1), (i, j))

        res = []
        for i, j in reversed(hits):
            if i < 0:
                res.append(0)
                continue
            s.create((i, j))
            grid[i][j] = 1
            non_top = 0
            for ni, nj in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 1 and s.find((i, j)) != s.find((ni, nj)):
                    size, top = s.info[s.find((ni, nj))]
                    if not top:
                        non_top += size
                    s.union((ni, nj), (i, j))
            res.append(non_top if s.info[s.find((i,j))][1] else 0)

        return res[::-1]


class BricksFallingWhenHitTests(TestCase):
    def test1(self):
        b = BricksFallingWhenHit()
        self.assertEqual([1,0,1,0,0], b.hitBricks([[1],[1],[1],[1],[1]], [[3,0], [4,0], [1,0], [2,0], [0,0]]))

    def test2(self):
        b = BricksFallingWhenHit()
        self.assertEqual([2], b.hitBricks([[1,0,0,0],[1,1,1,0]], [[1,0]]))

    def test3(self):
        b = BricksFallingWhenHit()
        self.assertEqual([0,0], b.hitBricks([[1,0,0,0],[1,1,0,0]], [[1,1],[1,0]]))





