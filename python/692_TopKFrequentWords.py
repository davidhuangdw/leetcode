from unittest import TestCase
# https://leetcode.com/problems/top-k-frequent-words
import collections, heapq


class TopKFrequentWords(TestCase):
    def topKFrequent(self, words: 'List[str]', k: 'int') -> 'List[str]':
        que = [(-c, w) for w, c in collections.Counter(words).items()]
        heapq.heapify(que)
        return [heapq.heappop(que)[1] for _ in range(k)]

    # # bucket sort due to count <= n
    # def topKFrequent(self, words: 'List[str]', k: 'int') -> 'List[str]':
    #     buckets, res = collections.defaultdict(list), []
    #     for w, c in collections.Counter(words).items():
    #         buckets[c].append(w)
    #     for i in range(max(buckets), 0, -1):
    #         if i not in buckets: continue
    #         if len(res) >= k: break
    #         buckets[i].sort()
    #         res.extend(buckets[i][:k-len(res)])
    #     return res

    def test1(self):
        self.assertEqual(["i", "love"], self.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))

    def test2(self):
        self.assertEqual(["the", "is", "sunny", "day"], self.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4))

        

