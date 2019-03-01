from unittest import TestCase
# https://leetcode.com/problems/top-k-frequent-elements
import collections, heapq


class TopKFrequentElements(TestCase):
    def topKFrequent(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        count = collections.Counter(nums)
        heap = list((-count[num], num) for num in count)
        heapq.heapify(heap)
        return list(heapq.heappop(heap)[1] for _ in range(k))

    def test1(self):
        self.assertEqual([1,2], self.topKFrequent(nums = [1,1,1,2,2,3], k = 2))

    def test2(self):
        self.assertEqual([1], self.topKFrequent(nums = [1], k = 1))

