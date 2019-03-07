from unittest import TestCase
# https://leetcode.com/problems/reorganize-string
import collections, heapq


class ReorganizeString(TestCase):
    def reorganizeString(self, S: 'str') -> 'str':
        count = collections.Counter(S)
        pairs, res = [[-count[ch], ch] for ch in count], []
        heapq.heapify(pairs)
        if -pairs[0][0]*2-1 > len(S):
            return ""
        while len(pairs) > 1:
            most_two = [heapq.heappop(pairs) for _ in range(2)]
            for cnt_char in most_two:
                res.append(cnt_char[1])
                cnt_char[0] += 1
                if cnt_char[0]: heapq.heappush(pairs, cnt_char)
        return "".join(res) + (pairs[0][1] if pairs else "")

    # # by intercept directly
    # def reorganizeString(self, S: 'str') -> 'str':
    #     count = collections.Counter(S)
    #     if max(count.values())*2 -1 > len(S):
    #         return ""
    #     s = sorted(sorted(S), key=lambda c: -count[c])
    #     h = (len(s)+1) >> 1
    #     s[::2], s[1::2] = s[:h], s[h:]
    #     return "".join(s)

    def test1(self):
        self.assertEqual("aba", self.reorganizeString("aab"))

    def test2(self):
        self.assertEqual("", self.reorganizeString("aaab"))

    def test3(self):
        self.assertEqual("", self.reorganizeString("abbabbaaab"))


