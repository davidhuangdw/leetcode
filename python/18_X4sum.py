from unittest import TestCase
# https://leetcode.com/problems/4sum
import bisect


class X4sum(TestCase):
    def fourSum(self, nums: 'List[int]', target: 'int') -> 'List[List[int]]':
        if len(nums) < 4: return []
        nums, n, res = list(sorted(nums)), len(nums), set()
        pairs = [(vi+nums[j], i, j) for i, vi in enumerate(nums) for j in range(i + 1, n)]
        pairs.sort()
        l = bisect.bisect_left(pairs, (target - pairs[-1][0], 0, 0))
        r = bisect.bisect_right(pairs, (target - pairs[0][0], n, n))-1
        while l < r:
            ls, rs = pairs[l][0], pairs[r][0]
            if target < ls*2 or target > rs*2: break
            if ls + rs < target:
                l += 1
            elif ls + rs > target:
                r -= 1
            else:                       # might >= O(1) when equals
                nr = r-1
                while nr > l and pairs[nr][0] == rs:
                    nr -= 1
                while l <= nr and pairs[l][0] == ls:
                    _, a, b = pairs[l]
                    for j in range(nr+1, r+1):
                        _, c, d = pairs[j]
                        if b < c:
                            res.add(tuple(nums[k] for k in (a,b,c,d)))
                    l += 1
                r = nr
        return list(map(list, res))

    # # directly reduced to O(n^3)
    # def fourSum(self, nums: 'List[int]', target: 'int') -> 'List[List[int]]':
    #     nums, n, res = list(sorted(nums)), len(nums), set()
    #     for i in range(n-3):
    #         if target < nums[i]*4 or nums[-1]*4 < target: break
    #         if i > 0 and nums[i] == nums[i-1]: continue
    #         a = nums[i]
    #         for j in range(i+1, n-2):
    #             if target < nums[j]*3+a or nums[-1]*3+a < target: break
    #             if j > i+1 and nums[j] == nums[j-1]: continue
    #             b = nums[j]
    #             l, r = j+1, n-1
    #             while l < r:
    #                 c, d = nums[l], nums[r]
    #                 df = a + b + c + d - target
    #                 if df < 0:
    #                     l += 1
    #                 elif df > 0:
    #                     r -= 1
    #                 else:
    #                     res.add((a, b, c, d))
    #                     while nums[l] == c and l < r:
    #                         l += 1
    #                     while nums[r] == d and l < r:
    #                         r -= 1
    #     return list(map(list, res))

    def test1(self):
        self.assertEqual([[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]], self.fourSum([1, 0, -1, 0, -2, 2], 0))


        

