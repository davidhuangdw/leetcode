from unittest import TestCase
# https://leetcode.com/problems/number-of-islands/


class NumberofIslands(TestCase):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    count += 1
                    self.visit(i, j, grid)
        return count

    def visit(self, i, j, grid):
        que = [(i, j)]
        while len(que)>0:
            i, j = que.pop()
            grid[i][j] = -1
            for (di, dj) in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                ni = i+di
                nj = j+dj
                if 0 <= ni < len(grid) and 0 <= nj < len(grid[ni]) and grid[ni][nj] == "1":
                    que.append((ni, nj))

    # # union-find
    # def numIslands(self, grid):
    #     root, cnt = {}, 0
    #
    #     def find(pos):
    #         if pos not in root: return None
    #         if root[pos] != pos: root[pos] = find(root[pos])
    #         return root[pos]
    #     for i in range(len(grid)):
    #         for j in range(len(grid[i])):
    #             if grid[i][j] == "0": continue
    #             cnt += 1
    #             pos = (i, j)
    #             root[pos] = pos
    #             for nei in (j-1 >= 0 and (i, j-1), i-1 >= 0 and (i-1, j)):
    #                 if not nei: continue
    #                 rn, rp = find(nei), find(pos)
    #                 if rn and rn != rp:
    #                     root[rp] = rn
    #                     cnt -= 1
    #     return cnt

    def test1(self):
        grid = [
            list("11110"),
            list("11010"),
            list("11000"),
            list("00000"),
        ]
        self.assertEqual(1, self.numIslands(grid))

    def test2(self):
        grid = [
            list("11000"),
            list("11000"),
            list("00100"),
            list("00011"),
        ]
        self.assertEqual(3, self.numIslands(grid))


