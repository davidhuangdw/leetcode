from unittest import TestCase
# https://leetcode.com/problems/sum-of-distances-in-tree/


class SumofDistancesinTree(TestCase):
    def sumOfDistancesInTree(self, N: 'int', edges: 'List[List[int]]') -> 'List[int]':
        e = [[] for _ in range(N)]
        for i, j in edges:
            e[i].append(j)
            e[j].append(i)
        cnt = [1 for _ in range(N)]
        res = [0 for _ in range(N)]

        def dfs(i, parent):
            for j in e[i]:
                if j != parent:
                    dfs(j, i)
                    cnt[i] += cnt[j]
                    res[i] += res[j] + cnt[j]

        def cal(i, parent):
            for j in e[i]:
                if j != parent:
                    res[j] = res[i] + N - 2*cnt[j]
                    cal(j, i)

        dfs(0, -1)
        cal(0, -1)
        return res

    def test1(self):
        self.assertEqual([8,12,6,10,10,10], self.sumOfDistancesInTree(6, [[0,1],[0,2],[2,3],[2,4],[2,5]]))

