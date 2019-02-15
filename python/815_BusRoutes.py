from unittest import TestCase
# https://leetcode.com/problems/bus-routes/
import collections


class BusRoutes(TestCase):
    def numBusesToDestination(self, routes: 'List[List[int]]', S: 'int', T: 'int') -> 'int':
        if S == T: return 0
        n, done, que = len(routes), set(), collections.deque()
        edges = [[] for _ in range(n)]
        for i in range(len(routes)):
            routes[i] = set(routes[i])
            if S in routes[i]:
                que.appendleft((1, i))
                done.add(i)
        for i in range(n):
            for j in range(i+1, n):
                if any(s in routes[j] for s in routes[i]):
                    edges[i].append(j)
                    edges[j].append(i)
        while que:
            cnt, i = que.pop()
            if T in routes[i]:
                return cnt
            for j in edges[i]:
                if j not in done:
                    done.add(j)
                    que.appendleft((cnt+1, j))
        return -1

    def test1(self):
        self.assertEqual(2, self.numBusesToDestination([[1, 2, 7], [3, 6, 7]], 1, 6))

