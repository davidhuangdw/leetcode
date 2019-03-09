from unittest import TestCase
# https://leetcode.com/problems/find-the-duplicate-number


class FindTheDuplicateNumber(TestCase):
    # requirements:
    # You must not modify the array (assume the array is read only).
    # You must use only constant, O(1) extra space.
    # Your runtime complexity should be less than O(n2).
    # There is only one duplicate number in the array, but it could be repeated more than once.

    def findDuplicate(self, nums: 'List[int]') -> 'int':
        l, r = 1, len(nums)-1
        while l <= r:
            m = (l+r) >> 1
            lt, eq = 0, 0
            for v in nums:
                if v == m:
                    eq += 1
                elif v < m:
                    lt += 1
            if eq > 1:
                return m
            elif lt < m:
                l = m+1
            else:
                r = m-1

    # # by cycle detection(floyd):
    # # edge i -> nums[i]:
    # # must have 2 numbers nums[i] and nums[j] point to the same target: nums[i] == nums[j]
    # # 0 is out of the cycle, walk along from 0, there must a point v == nums[p] and v == nums[q]
    # # where p is out of cycle, and q is in the cycle
    # def findDuplicate(self, nums: 'List[int]') -> 'int':
    #     a, b = nums[0], nums[nums[0]]
    #     while a != b:
    #         a = nums[a]
    #         b = nums[nums[b]]
    #     b = 0
    #     while a != b:
    #         a = nums[a]
    #         b = nums[b]
    #     return a

    def test1(self):
        self.assertEqual(2, self.findDuplicate([1,3,4,2,2]))

    def test2(self):
        self.assertEqual(3, self.findDuplicate([3,1,3,4,2]))


