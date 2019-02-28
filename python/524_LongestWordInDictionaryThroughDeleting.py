from unittest import TestCase
# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting


class LongestWordInDictionaryThroughDeleting(TestCase):
    def findLongestWord(self, s: 'str', d: 'List[str]') -> 'str':
        s = '_' + s
        n, nxt = len(s), [{} for _ in s]
        for i, c in enumerate(s):
            for j in range(i-1, -1, -1):
                nxt[j][c] = i
                if s[j] == c: break

        def find(word):
            i = 0
            for c in word:
                i = nxt[i].get(c)
                if i is None: return False
            return True
        res = ""
        for word in d:
            if find(word) and (not res or (-len(word), word) < (-len(res), res)):
                res = word
        return res

    # by compare directly:
    # def findLongestWord(self, s: 'str', d: 'List[str]') -> 'str':
    #     n = len(s)
    #
    #     def find(word):
    #         j = 0
    #         for c in word:
    #             while j < n and s[j] != c:
    #                 j += 1
    #             if j >= n: return False
    #             j += 1
    #         return True
    #     res = ""
    #     for word in d:
    #         if find(word) and (not res or (-len(word), word) < (-len(res), res)):
    #             res = word
    #     return res

    def test1(self):
        self.assertEqual("apple", self.findLongestWord("abpcplea", ["ale","apple","monkey","plea"]))

    def test2(self):
        self.assertEqual("a", self.findLongestWord("abpcplea", ["a","b","c"]))

