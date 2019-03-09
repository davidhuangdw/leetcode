from unittest import TestCase
# https://leetcode.com/problems/3sum-closest


class X3sumClosest(TestCase):
    def threeSumClosest(self, nums: 'List[int]', target: 'int') -> 'int':
        nums.sort()
        n, diff = len(nums), float("inf")
        for i in range(n):
            l, r, tar = i+1, n-1, target-nums[i]
            while l < r:
                s = nums[l]+nums[r]
                if s == tar:
                    return target
                if abs(tar-s) < abs(diff):
                    diff = tar - s
                if s <= tar:
                    l += 1
                else:
                    r -= 1
        return target-diff

    def test1(self):
        self.assertEqual(2, self.threeSumClosest([-1, 2, 1, -4], 1))
        

