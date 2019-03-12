from unittest import TestCase
# https://leetcode.com/problems/split-array-into-consecutive-subsequences
import collections, operator


class SplitArrayIntoConsecutiveSubsequences(TestCase):
    def isPossible(self, nums: 'List[int]') -> 'bool':
        # x == the amount of length>=3,  y == the amount of length>=2, z == the amount of length >= 3
        x = y = z = 0
        i, n = 0, len(nums)
        while i < n:
            j, i = i, i+1
            while i < n and nums[i] == nums[i-1]:
                i += 1
            size = i-j
            if y+z > size: return False
            # greedy: reduce size 1 first, then size 2, then current size 1
            ex = size - (x+y+z)
            x, y, z = y+x+min(ex, 0), z, max(ex, 0)
            if i == n or nums[i] != nums[i-1]+1:
                if not (y == z == 0): return False
                x = y = z = 0
            operator.add
        return True

    # # greedy: chain as long as possible
    # # rough prove:
    # #   for num i, the decisioin how many i is put on existing chain or start as a new chain, won't affect future decision of j(> i)
    # #   but we hope to make new unfinished chains as small as possible, so we chain as long as possible
    # # impl trick here -- consume forward if impossible backward
    # def isPossible(self, nums: 'List[int]') -> 'bool':
    #     left = collections.Counter(nums)
    #     ends = collections.Counter()
    #     for i in nums:
    #         if not left[i]: continue    # allow consumed by previous value
    #         left[i] -= 1
    #         if ends[i-1] > 0:
    #             ends[i-1] -= 1
    #             ends[i] += 1
    #         elif left[i+1] and left[i+2]:   # consume forward
    #             left[i+1] -= 1
    #             left[i+2] -= 1
    #             ends[i+2] += 1              # only >=3 can mark end
    #         else:
    #             return False
    #     return True

    def test1(self):
        self.assertEqual(True, self.isPossible([1,2,3,3,4,5]))

    def test2(self):
        self.assertEqual(True, self.isPossible([1,2,3,3,4,4,5,5]))

    def test3(self):
        self.assertEqual(False, self.isPossible([1,2,3,4,4,5]))

