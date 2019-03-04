from unittest import TestCase
# https://leetcode.com/problems/maximum-product-subarray


class MaximumProductSubarray(TestCase):
    def maxProduct(self, nums: 'List[int]') -> 'int':
        cur, res = (1, 1), float("-inf")
        for v in nums:
            cur = max(cur[0]*v, cur[1]*v, v), min(cur[0]*v, cur[1]*v, v)
            res = max(res, cur[0])
        return res

    # # by prefix/suffix -- for any non-zero series, it must include first or last value
    # def maxProduct(self, A: 'List[int]') -> 'int':
    #     B = A[::-1]
    #     for i in range(1, len(A)):
    #         A[i] *= A[i-1] or 1
    #         B[i] *= B[i-1] or 1
    #     return max(A+B)

    def test1(self):
        self.assertEqual(6, self.maxProduct([2,3,-2,4]))

    def test2(self):
        self.assertEqual(0, self.maxProduct([-2,0,-1]))

    def test3(self):
        self.assertEqual(27, self.maxProduct([2,3,0,-2,-9,-3]))

        

