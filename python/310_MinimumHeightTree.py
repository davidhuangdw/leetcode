from unittest import TestCase
# https://leetcode.com/problems/minimum-height-trees/


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

    def test1(self):
        self.assertEqual([1], self.findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]))

    def test2(self):
        self.assertEqual([3, 4], self.findMinHeightTrees(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]))


