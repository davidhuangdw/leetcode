from unittest import TestCase
# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
import heapq


class FindKPairswithSmallestSums(TestCase):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        n, m = len(nums1), len(nums2)
        if not (k and n and m): return []
        ret = []
        heap = [(nums1[0] + nums2[0], 0, 0)]
        while heap and len(ret) < k:
            _, i, j = heapq.heappop(heap)
            ret.append([nums1[i], nums2[j]])
            if j+1 < len(nums2):
                heapq.heappush(heap, (nums1[i]+nums2[j+1], i, j+1))
            if j == 0 and i+1 < len(nums1):
                heapq.heappush(heap, (nums1[i+1]+nums2[j], i+1, j))
        return ret

    def test1(self):
        self.assertEqual([[1,2],[1,4],[1,6]], self.kSmallestPairs([1,7,11], [2,4,6], 3))

    def test2(self):
        self.assertEqual([[1,1],[1,1]], self.kSmallestPairs([1,1,2], [1,2,3], 2))

    def test3(self):
        self.assertEqual([[1,3],[2,3]], self.kSmallestPairs([1,2], [3], 3))


