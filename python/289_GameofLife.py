from unittest import TestCase
# https://leetcode.com/problems/game-of-life/


class GameofLife(TestCase):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                cnt = 0
                for x in range(max(i-1, 0), min(i+2, n)):
                    for y in range(max(j-1, 0), min(j+2, m)):
                        if board[x][y] & 1:
                            cnt += 1
                if cnt == 3 or cnt-(board[i][j]&1) == 3:
                    board[i][j] |= 2

        for i in range(n):
            for j in range(m):
                board[i][j] >>= 1

    def test1(self):
        board = [
            [0,1,0],
            [0,0,1],
            [1,1,1],
            [0,0,0]
        ]
        self.gameOfLife(board)
        self.assertEqual([
            [0,0,0],
            [1,0,1],
            [0,1,1],
            [0,1,0]
        ], board)
