from unittest import TestCase
# https://leetcode.com/problems/new-21-game
import collections


class New21Game(TestCase):
    def new21Game(self, N: 'int', K: 'int', W: 'int') -> 'float':
        que = [1 if i <= N else 0 for i in range(K, K+W)]
        s, que = sum(que), collections.deque(que)
        for i in range(K-1, -1, -1):
            pi = s/W
            s += pi - que.pop()
            que.appendleft(pi)
        return que[0]

    def test1(self):
        self.assertEqual(1, self.new21Game(10, 1, 10))

    def test2(self):
        self.assertEqual(0.6, self.new21Game(6, 1, 10))

    def test3(self):
        self.assertAlmostEqual(0.73278, self.new21Game(21, 17, 10), delta=1e-5)


