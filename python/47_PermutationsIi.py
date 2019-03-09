from unittest import TestCase
# https://leetcode.com/problems/permutations-ii
import collections


class PermutationsIi(TestCase):
    def permuteUnique(self, nums: 'List[int]') -> 'List[List[int]]':
        count, res = collections.Counter(nums), []

        def dfs(path):
            if not count:
                res.append(list(path))
            else:
                for v in list(count):
                    count[v] -= 1
                    if not count[v]:
                        count.pop(v)
                    path.append(v)
                    dfs(path)
                    path.pop()
                    count[v] += 1
        dfs([])
        return res

    # # iterative: insert existing results
    # def permuteUnique(self, nums: 'List[int]') -> 'List[List[int]]':
    #     res = [[]]
    #     for v in nums:
    #         nxt = []
    #         for part in res:
    #             m = len(part)
    #             for i in range(m+1):
    #                 nxt.append(part[:i] + [v] + part[i:])
    #                 if i < m and part[i] == v: break          # ensure the inserted is the first one
    #         res = nxt
    #     return res

    def test1(self):
        perm = [
            [1,1,2],
            [1,2,1],
            [2,1,1]
        ]
        self.assertEqual(perm, self.permuteUnique([1,1,2]))


        

