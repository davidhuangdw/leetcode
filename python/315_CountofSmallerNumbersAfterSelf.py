from unittest import TestCase
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/


class CountofSmallerNumbersAfterSelf(TestCase):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ret = [0] * n
        def sort(arr):
            if len(arr) <= 1: return arr
            half = int(len(arr)/2)
            l, r, res = sort(arr[:half]), sort(arr[half:]), []
            while l or r:
                if l and (not r or nums[l[-1]] > nums[r[-1]]):
                    ret[l[-1]] += len(r)
                    res.append(l.pop())
                else:
                    res.append(r.pop())
            return res[::-1]
        sort(list(range(n)))
        return ret

    def test1(self):
        self.assertEqual([2,1,1,0], self.countSmaller([5,2,6,1]))

    def test2(self):
        self.assertEqual([2,0,0], self.countSmaller([2, 0, 1]))
