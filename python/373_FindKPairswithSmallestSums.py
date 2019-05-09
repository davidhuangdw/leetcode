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

    # heap: O(k*log(n*m))
    def kSmallestPairs(self, a, b, k):
        if not (a and b): return []
        n, m, res, que = len(a), len(b), [], [(a[0]+b[0], 0, 0)]
        for _ in range(min(k, n*m)):
            _, i, j = heapq.heappop(que)
            res.append([a[i], b[j]])
            if j+1 < m:
                heapq.heappush(que, (a[i]+b[j+1], i, j+1))
            if j == 0 and i+1 < n:
                heapq.heappush(que, (a[i+1]+b[j], i+1, j))
        return res

    # find kth sum first: O((n+m)*log(max_sum) + k)
    def kSmallestPairs(self, a, b, k):
        if not (a and b): return []
        n, m, l, r = len(a), len(b), a[0]+b[0], a[-1]+b[-1]
        def count_le(x):
            j = cnt = 0
            for i in range(n-1, -1, -1):
                while j < m and a[i]+b[j] <= x:
                    j += 1
                cnt += j
                if cnt >= k: break      # optimize
            return cnt
        while l <= r:
            md = (l+r) >> 1
            if count_le(md) < k:
                l = md + 1
            else:
                r = md - 1

        cap, res, eq = l, [], 0
        eq_size = k - count_le(cap-1)
        for i in range(n):
            for j in range(m):
                sum = a[i] + b[j]
                if sum > cap or (sum == cap and eq >= eq_size): break
                res.append([a[i], b[j]])
                eq += (sum == cap)
        return res

    def test1(self):
        self.assertEqual([[1,2],[1,4],[1,6]], self.kSmallestPairs([1,7,11], [2,4,6], 3))

    def test2(self):
        self.assertEqual([[1,1],[1,1]], self.kSmallestPairs([1,1,2], [1,2,3], 2))

    def test3(self):
        self.assertEqual([[1,3],[2,3]], self.kSmallestPairs([1,2], [3], 3))


