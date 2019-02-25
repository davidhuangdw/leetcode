from unittest import TestCase
# https://leetcode.com/problems/kth-largest-element-in-an-array
import itertools
import random


class KthLargestElementInAnArray(TestCase):
    def findKthLargest(self, nums: 'List[int]', k: 'int') -> 'int':
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        st, ed = 0, len(nums)
        while True:
            if k == 1: return max(itertools.islice(nums, st, ed))
            if k == ed-st: return min(itertools.islice(nums, st, ed))
            swap(random.randint(st, ed-1), ed-1)
            pivot = nums[ed-1]
            i, j, u = st, st, ed-2
            while j <= u:
                if nums[j] > pivot:
                    swap(i, j)
                    i += 1
                    j += 1
                elif nums[j] == pivot:
                    j += 1
                else:
                    swap(j, u)
                    u -= 1
            if k <= i-st:
                ed = i
            elif k <= j+1-st:      # plus 1 due to pivot at nums[ed-1]
                return pivot
            else:
                k -= j+1-st
                st = j
                ed -= 1

    def test1(self):
        self.assertEqual(5, self.findKthLargest([3,2,1,5,6,4], 2))

    def test2(self):
        self.assertEqual(4, self.findKthLargest([3,2,3,1,2,4,5,5,6], 4))

