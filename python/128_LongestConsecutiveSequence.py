from unittest import TestCase
# https://leetcode.com/problems/longest-consecutive-sequence/


class LongestConsecutiveSequence(TestCase):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        remain = set(nums)
        result = 0
        while remain:
            num = remain.pop()
            count = 1
            for dir in (-1, 1):
                v = num+dir
                while v in remain:
                    remain.remove(v)
                    count += 1
                    v += dir
            result = max(result, count)
        return result

    def test1(self):
        self.assertEqual(4, self.longestConsecutive([100, 4, 200, 1, 3, 2]))
