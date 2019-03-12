from unittest import TestCase
# https://leetcode.com/problems/longest-mountain-in-array


class LongestMountainInArray(TestCase):
    def longestMountain(self, A: 'List[int]') -> 'int':
        i, n, res = 1, len(A), 0
        while i < n:
            i += 1
            if not A[i-2] < A[i-1]: continue
            j = i-2
            while i < n and A[i] > A[i-1]:
                i += 1
            top = i
            while i < n and A[i] < A[i-1]:
                i += 1
            if i != top:
                res = max(res, i-j)
        return res

    # # by state of up and down
    # def longestMountain(self, A: 'List[int]') -> 'int':
    #     res = up = down = 0
    #     for i in range(1, len(A)):
    #         if A[i] == A[i-1] or (down and A[i-1] < A[i]):
    #             down = up = 0
    #         if A[i-1] < A[i]:
    #             up += 1
    #         elif A[i-1] > A[i]:
    #             down += 1
    #         if up and down:
    #             res = max(res, up+down+1)
    #     return res

    # # by iterate top only:
    # def longestMountain(self, A: 'List[int]') -> 'int':
    #     res, n = 0, len(A)
    #     for i in range(1, n-1):
    #         if not A[i-1] < A[i] > A[i+1]: continue
    #         l, r = i-1, i+1
    #         while l and A[l-1] < A[l]:
    #             l -= 1
    #         while r+1 < n and A[r] > A[r+1]:
    #             r += 1
    #         res = max(res, r-l+1)
    #     return res

    def test1(self):
        self.assertEqual(5, self.longestMountain([2,1,4,7,3,2,5]))

    def test2(self):
        self.assertEqual(0, self.longestMountain([2,3,3,3]))

    def test3(self):
        self.assertEqual(4, self.longestMountain([875,884,239,731,723,685]))


