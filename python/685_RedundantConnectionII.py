from unittest import TestCase
# https://leetcode.com/problems/redundant-connection-ii/


class RedundantConnectionII(TestCase):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        parent = dict()
        cands = None
        circle_last = None
        root = dict()

        def find(nd):
            if root.get(nd) is None:
                return nd
            else:
                root[nd] = find(root[nd])
                return root[nd]
        for fr, to in edges:
            if parent.get(to) is not None:
                cands = [[parent[to], to], [fr, to]]    # skip the edge cands[-1]
            else:
                parent[to] = fr
                if find(fr) == to:
                    circle_last = [fr, to]
                else:
                    root[to] = find(fr)

        if not cands:
            return circle_last
        else:
            return cands[0] if circle_last else cands[-1]   # skip wrong when still circle after skip cands[-1]

    # # dfs
    # def findRedundantDirectedConnection(self, edges):
    #     ch, ind, roots = {}, {}, set(range(1, len(edges)+1))
    #     for i, (u, v) in enumerate(edges):
    #         ind[(u,v)] = i
    #         if v in roots: roots.remove(v)
    #         if u not in ch: ch[u] = []
    #         ch[u].append(v)
    #     path, vis, res = [], {}, None
    #
    #     def dfs(u, p):
    #         nonlocal res
    #         vis[u] = p
    #         path.append(u)
    #         for v in ch.get(u, []):
    #             if res: return
    #             if v in vis:
    #                 if v in path: # circle
    #                     if vis[v] == -1: # pure circle
    #                         cand, t, i = [], v, -1
    #                         while path[i] != v:
    #                             cand.append((path[i], t))
    #                             t, i = path[i], i-1
    #                         cand.append((v, t))
    #                         res = max(cand, key=lambda e: ind[e])
    #                     else:
    #                         res = [u, v]
    #                 else: # no circle, two arrows meet
    #                     res = max([(u, v), (vis[v], v)], key=lambda e: ind[e])
    #                 return
    #             dfs(v, u)
    #         path.pop()
    #
    #     assert(len(roots) < 2)
    #     dfs(next(iter(roots)) if roots else 1, -1)
    #     return list(res)

    def test1(self):
        self.assertEqual([2,3], self.findRedundantDirectedConnection([[1,2], [1,3], [2,3]]))

    def test2(self):
        self.assertEqual([4,1], self.findRedundantDirectedConnection([[1,2], [2,3], [3,4], [4,1], [1,5]]))

    def test3(self):
        self.assertEqual([2,1], self.findRedundantDirectedConnection([[2,1],[3,1],[4,2],[1,4]]))

    def test4(self):
        self.assertEqual([4,2], self.findRedundantDirectedConnection([[4,2],[1,5],[5,2],[5,3],[2,4]]))
