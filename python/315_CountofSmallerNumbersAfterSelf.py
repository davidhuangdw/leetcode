from unittest import TestCase
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/


class CountofSmallerNumbersAfterSelf(TestCase):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ret, arr = [0] * n, list(range(n))

        def sort(i, j):
            if j-i <= 1: return arr[i:j]
            md = (i+j) >> 1
            l, r, res = sort(i, md), sort(md, j), []
            while l or r:
                if l and (not r or nums[l[-1]] > nums[r[-1]]):
                    ret[l[-1]] += len(r)
                    res.append(l.pop())
                else:
                    res.append(r.pop())
            return res[::-1]
        sort(0, n)
        return ret

    # # by BIT(Fenwick Tree)
    # def countSmaller(self, nums):
    #     ind = {v: i+1 for i, v in enumerate(sorted(set(nums)))}
    #     m = len(ind)+1
    #     pre = [0]*m
    #
    #     def update(i, add=1):
    #         while i < m:
    #             pre[i] += add
    #             i += i & -i
    #
    #     def query(i):
    #         s = 0
    #         while i > 0:
    #             s += pre[i]
    #             i -= i & -i
    #         return s
    #     ret = []
    #     for v in reversed(nums):
    #         i = ind[v]
    #         ret.append(query(i-1))
    #         update(i)
    #     return ret[::-1]

    def test1(self):
        self.assertEqual([2,1,1,0], self.countSmaller([5,2,6,1]))

    def test2(self):
        self.assertEqual([2,0,0], self.countSmaller([2, 0, 1]))
