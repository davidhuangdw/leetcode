from unittest import TestCase
# https://leetcode.com/problems/redundant-connection
import collections


class RedundantConnection(TestCase):
    # find circle by dfs
    def findRedundantConnection(self, edges: 'List[List[int]]') -> 'List[int]':
        conn = collections.defaultdict(list)
        for u, v in edges:
            conn[u].append(v)
            conn[v].append(u)
        parent, done, circle = {1: -1}, False, set()

        def dfs(u, pa):
            nonlocal done
            for v in conn[u]:
                if done: break
                if v == pa:
                    continue
                if v not in parent:
                    parent[v] = u
                    dfs(v, u)
                else:
                    circle.add(v)
                    while u != v:
                        circle.add(u)
                        u = parent[u]
                    done = True
        dfs(1, -1)
        for u, v in edges[::-1]:
            if u in circle and v in circle:
                return [u, v]

    # find circle by topology sort - keep removing leafs
    # def findRedundantConnection(self, edges: 'List[List[int]]') -> 'List[int]':
    #     conn, degree = collections.defaultdict(list), collections.defaultdict(lambda : 0)
    #     for u, v in edges:
    #         conn[u].append(v)
    #         conn[v].append(u)
    #         degree[u] += 1
    #         degree[v] += 1
    #     que = [u for u in degree if degree[u] == 1]
    #     leaves = set(que)
    #     while que:
    #         u = que.pop()
    #         for v in conn[u]:
    #             if v in leaves: continue
    #             degree[v] -= 1
    #             if degree[v] == 1:
    #                 que.append(v)
    #                 leaves.add(v)
    #     for u, v in edges[::-1]:
    #         if u not in leaves and v not in leaves:
    #             return [u, v]

    # by union-find:
    # def findRedundantConnection(self, edges: 'List[List[int]]') -> 'List[int]':
    #     parent = {}
    #
    #     def find(i):
    #         if i not in parent:
    #             parent[i] = i
    #         elif parent[i] != i:
    #             parent[i] = find(parent[i])
    #         return parent[i]
    #     for e in edges:
    #         u, v = e
    #         a, b = find(u), find(v)
    #         if a == b:
    #             return [u, v]
    #         else:
    #             parent[a] = b

    def test1(self):
        self.assertEqual([2,3], self.findRedundantConnection([[1,2], [1,3], [2,3]]))

    def test2(self):
        self.assertEqual([1,4], self.findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]]))

    def test3(self):
        self.assertEqual([1,4], self.findRedundantConnection([[16,25],[7,9],[3,24],[10,20],[15,24],[2,8],[19,21],[2,15],[13,20],[5,21],[7,11],[6,23],[7,16],[1,8],[17,20],[4,19],[11,22],[5,11],[1,16],[14,20],[1,4],[22,23],[12,20],[15,18],[12,16]]))



