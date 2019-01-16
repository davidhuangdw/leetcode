from unittest import TestCase
# https://leetcode.com/problems/create-maximum-number/


class CreateMaximumNumber(TestCase):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        def largestSubArray(nums, maxSize):
            ndrops = len(nums) - maxSize
            cur = []
            for num in nums:
                while cur and ndrops > 0 and cur[-1] < num:
                    cur.pop()
                    ndrops -= 1
                cur.append(num)
            return cur[:maxSize]

        def merge(a, b):
            return [max(a, b).pop(0) for _ in a+b]      # handle a[i]==b[j]: choose max(a[i:], b[j:])

        n, m = len(nums1), len(nums2)
        ret = None
        for i in range(max(0, k-m), min(n, k)+1):
            num = merge(largestSubArray(nums1, i), largestSubArray(nums2, k-i))
            if len(num) == k and (ret is None or ret < num):
                ret = num
        return ret


    def maxNumber1(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        l, r = 0, 0
        n, m = len(nums1), len(nums2)
        ret = []
        for i in range(0, k):
            lmax = max(range(l, min((m-r)+n-(k-i)+1, n)), key=lambda x: nums1[x], default=-1)
            rmax = max(range(r, min((n-l)+m-(k-i)+1, m)), key=lambda x: nums2[x], default=-1)
            if lmax >= 0 and (rmax < 0 or nums1[lmax] >= nums2[rmax]):     # error: cannot handle 'equal case'
                ret.append(nums1[lmax])
                l = lmax+1
            else:
                ret.append(nums2[rmax])
                r = rmax+1
        return ret

    def test1(self):
        self.assertEqual([9, 8, 6, 5, 3], self.maxNumber([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5))

    def test2(self):
        self.assertEqual([6, 7, 6, 0, 4], self.maxNumber([6, 7], [6, 0, 4], 5))

    def test3(self):
        self.assertEqual([9, 8, 9], self.maxNumber([8, 9], [3, 9], 3))

    def test4(self):
        self.assertEqual([9, 7, 5], self.maxNumber([8, 6, 9], [1, 7, 5], 3))

    def test5(self):
        self.assertEqual([7,3,8,2,5,6,4,4,0,6,5,7,6,2,0], self.maxNumber([2, 5, 6, 4, 4, 0], [7, 3, 8, 0, 6, 5, 7, 6, 2], 15))
