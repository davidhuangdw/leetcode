from unittest import TestCase
# https://leetcode.com/problems/count-of-range-sum/


class CountofRangeSum(TestCase):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        sums = [0]
        for v in nums:
            sums.append(sums[-1]+v)
        ret = 0

        def sort(sub):
            nonlocal ret
            n = len(sub)
            if n <= 1:
                return sub
            hf = int(n/2)
            l = sort(sub[:hf])
            r = sort(sub[hf:])
            m = len(r)
            cur = []
            j = k = t = 0
            for v in l:
                while j < m and r[j] - v < lower:
                    j += 1
                while k < m and r[k] - v <= upper:
                    k += 1
                while t < m and r[t] <= v:
                    cur.append(r[t])
                    t += 1
                cur.append(v)
                ret += k-j
            return cur + r[t:m]
        sort(sums)
        return ret

    def test1(self):
        self.assertEqual(3, self.countRangeSum([-2,5,-1], -2, 2))

    def test2(self):
        self.assertEqual(7, self.countRangeSum([-3,1,2,-2,2,-1], -3, -1))

    def test3(self):
        self.assertEqual(0, self.countRangeSum([], 0, 0))

