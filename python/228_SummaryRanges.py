from unittest import TestCase
# https://leetcode.com/problems/summary-ranges/submissions/


class SummaryRanges(TestCase):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ret = []
        l = 0
        for i in range(1, len(nums)+1):
            if i == len(nums) or nums[i]-1 != nums[i-1]:
                ret.append(f"{nums[l]}" if l == i-1 else f"{nums[l]}->{nums[i-1]}")
                l = i
        return ret

    def test1(self):
        self.assertEqual(["0->2","4->5","7"], self.summaryRanges([0,1,2,4,5,7]))

    def test2(self):
        self.assertEqual(["0","2->4","6","8->9"], self.summaryRanges([0,2,3,4,6,8,9]))
