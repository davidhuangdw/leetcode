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
                cands = [[parent[to], to], [fr, to]]
            else:
                parent[to] = fr
                if find(fr) == to:
                    circle_last = [fr, to]
                else:
                    root[to] = find(fr)

        if not cands:
            return circle_last
        else:
            return cands[0] if circle_last else cands[-1]

    def test1(self):
        self.assertEqual([2,3], self.findRedundantDirectedConnection([[1,2], [1,3], [2,3]]))

    def test2(self):
        self.assertEqual([4,1], self.findRedundantDirectedConnection([[1,2], [2,3], [3,4], [4,1], [1,5]]))

    def test3(self):
        self.assertEqual([2,1], self.findRedundantDirectedConnection([[2,1],[3,1],[4,2],[1,4]]))
