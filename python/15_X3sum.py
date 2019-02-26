from unittest import TestCase
# https://leetcode.com/problems/3sum


class X3sum(TestCase):
    def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':
        nums.sort()
        n, res = len(nums), []
        for i in range(n):
            if i-1 >= 0 and nums[i] == nums[i-1]: continue
            j, k = i+1, n-1
            while j < k:
                a = [nums[i], nums[j], nums[k]]
                s = sum(a)
                if s == 0:
                    res.append(a)
                    while j+1 < k and nums[j+1] == nums[j]:
                        j += 1
                    while k-1 > j and nums[k-1] == nums[k]:
                        k -= 1
                if s <= 0: j += 1
                if s >= 0: k -= 1
        return res

    def test1(self):
        self.assertEqual([[-1, -1, 2], [-1, 0, 1]], self.threeSum([-1, 0, 1, 2, -1, -4]))

