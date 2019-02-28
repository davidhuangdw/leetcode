from unittest import TestCase
# https://leetcode.com/problems/expressive-words
import itertools


class ExpressiveWords(TestCase):
    def expressiveWords(self, S: 'str', words: 'List[str]') -> 'int':
        def nextDiff(i, s):
            for j in range(i+1, len(s)):
                if s[j] != s[j-1]:
                    return j
            return len(s)
        i, n, counts = 0, len(S), []
        while i < n:
            j = nextDiff(i, S)
            counts.append((S[i], j-i))
            i = j

        def stretchy(word):
            i, m = 0, len(word)
            for ch, count in counts:
                if i == m or word[i] != ch: return False
                j = nextDiff(i, word)
                if count < j-i or (count < 3 and count != j-i):
                    return False
                i = j
            return i == m
        return sum(1 if stretchy(word) else 0 for word in words)

    # concise:
    # def expressiveWords(self, S: 'str', words: 'List[str]') -> 'int':
    #     def counts(s):
    #         return zip(*[(ch, len(list(grp))) for ch, grp in itertools.groupby(s)])
    #
    #     s1, cs1 = counts(S)
    #     return sum(s1 == s2 and all(c1 == c2 or (c1 >= max(3, c2)) for c1, c2 in zip(cs1, cs2)) for word in words for s2, cs2 in [counts(word)])

    def test1(self):
        self.assertEqual(1, self.expressiveWords("heeellooo", ["hello", "hi", "helo"]))

    def test2(self):
        self.assertEqual(0, self.expressiveWords("abcd", ["abc"]))


