from unittest import TestCase
# https://leetcode.com/problems/perfect-squares/
import math, collections


class PerfectSquares(TestCase):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        squares = [i*i for i in range(1, int(n ** 0.5)+1)]
        cnt = [n]*(n+1)
        cnt[0] = 0
        for x in range(n):
            for s in squares:
                v = x+s
                if v > n: break
                cnt[v] = min(cnt[v], cnt[x]+1)
        return cnt[n]

    # # bfs
    # def numSquares(self, n):
    #     squares = [i*i for i in range(1, int(math.sqrt(n))+1)]
    #     que = collections.deque([(0, 0, 0)])
    #     while que:
    #         v, c, i = que.popleft()
    #         for j in range(i, len(squares)):
    #             nxt = v + squares[j]
    #             if nxt == n: return c+1
    #             if nxt > n: break
    #             que.append((nxt, c+1, j))
    #     return -1
    #
    # # theory number O(sqrt(n)): must <=4
    # def numSquares(self, n):
    #     sq = int(math.sqrt(n))+1
    #     for a in range(sq):
    #         for b in range(a, sq):
    #             if a*a + 2*b*b > n: break
    #             c = int(math.sqrt(n - a*a - b*b))
    #             if a*a + b*b + c*c == n:
    #                 return 1 + bool(a) + bool(b)
    #     return 4

    def test1(self):
        self.assertEqual(3, self.numSquares(12))

    def test2(self):
        self.assertEqual(2, self.numSquares(13))

    def test3(self):
        self.assertEqual(2, self.numSquares(7))
