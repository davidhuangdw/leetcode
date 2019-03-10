from unittest import TestCase
# https://leetcode.com/problems/minimum-height-trees/
import collections


class MinimumHeightTree(TestCase):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n <= 0: return []

        links = [[] for i in range(n)]
        for (f,t) in edges:
            links[f].append(t)
            links[t].append(f)

        vis = set()
        def deepest(i):
            vis.add(i)
            mx = (0, i)
            for j in links[i]:
                if j not in vis:
                    h, x = deepest(j)
                    if 1+h > mx[0]:
                        mx = (1+h, x)
            return mx

        fr = deepest(0)[1]
        vis = set()
        l, to = deepest(fr)

        ret = []
        middles = [int(l/2)] if l % 2 == 0 else [int(l/2), int(l/2)+1]
        vis = set()
        def dfs(i, d):
            vis.add(i)
            mx = 0
            for j in links[i]:
                if j not in vis:
                    mx = max(mx, 1+dfs(j, d+1))
            if d+mx == l and d in middles:
                ret.append(i)
            return mx
        dfs(fr, 0)
        return ret

    # # by longest path
    # def findMinHeightTrees(self, n, edges):
    #     if not n: return []
    #     e = [[] for _ in range(n)]
    #     for u, v in edges:
    #         e[u].append(v)
    #         e[v].append(u)
    #
    #     def longest_path(u, par=None):
    #         mx = []
    #         for v in e[u]:
    #             if v != par:
    #                 now = longest_path(v, u)
    #                 if len(now) > len(mx):
    #                     mx = now
    #         mx.append(u)
    #         return mx
    #     fr = longest_path(0)[0]
    #     path = longest_path(fr)
    #     k = len(path)
    #     return path[(k-1)>>1 : (k+2)>>1]
    #
    #
    # # # bfs by removing leafs
    # def findMinHeightTrees(self, n, edges):
    #     if not n: return []
    #     e = [[] for _ in range(n)]
    #     deg = [0 for _ in range(n)]
    #     for u, v in edges:
    #         e[u].append(v)
    #         e[v].append(u)
    #         deg[u] += 1
    #         deg[v] += 1
    #
    #     leaves = [u for u in range(n) if deg[u] <= 1]
    #     done = set(leaves)
    #
    #     while len(done) < n:
    #         nxt = []
    #         for u in leaves:
    #             for v in e[u]:
    #                 if v in done: continue
    #                 deg[v] -= 1
    #                 if deg[v] == 1:
    #                     done.add(v)
    #                     nxt.append(v)
    #         leaves = nxt
    #     return list(leaves)

    def test1(self):
        self.assertEqual([1], self.findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]))

    def test2(self):
        self.assertEqual({3, 4}, set(self.findMinHeightTrees(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]])))

    def test3(self):
        self.assertEqual([0], self.findMinHeightTrees(3, [[0,1],[0,2]]))


