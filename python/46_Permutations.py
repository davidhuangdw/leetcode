from unittest import TestCase
# https://leetcode.com/problems/permutations


class Permutations(TestCase):
    def permute(self, nums: 'List[int]') -> 'List[List[int]]':
        n, res = len(nums), []

        def dfs(i):
            if i >= n:
                res.append([*nums])
            else:
                for j in range(i, n):
                    nums[i], nums[j] = nums[j], nums[i]
                    dfs(i+1)
                    nums[i], nums[j] = nums[j], nums[i]
        dfs(0)
        return res

    # # iterative: insert existing results
    # def permute(self, nums: 'List[int]') -> 'List[List[int]]':
    #     res = [[]]
    #     for v in nums:
    #         nxt = []
    #         for part in res:
    #             for i in range(len(part)+1):
    #                 nxt.append(part[:i] + [v] + part[i:])
    #         res = nxt
    #     return res

    # #by set:
    # def permute(self, nums: 'List[int]') -> 'List[List[int]]':
    #     rem, res = set(nums), []
    #
    #     def dfs(path):
    #         if not rem:
    #             res.append(path)
    #         else:
    #             for v in list(rem):
    #                 rem.remove(v)
    #                 dfs(path + [v])
    #                 rem.add(v)
    #     dfs([])
    #     return res


    def test1(self):
        self.assertEqual([[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]], self.permute([1,2,3]))


