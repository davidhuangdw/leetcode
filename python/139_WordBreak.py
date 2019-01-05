from unittest import TestCase
# https://leetcode.com/problems/word-break/


class WordBreak(TestCase):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        maxlen = max(map(len, wordDict)) if wordDict else 0
        words = set(wordDict)
        reach = [True, *[False]*n]

        for i in range(n):
            if not reach[i]: continue
            for j in range(i+1, min(n, i+maxlen)+1):
                if not reach[j] and s[i:j] in words:
                    reach[j] = True

        return reach[n]

    def test1(self):
        self.assertEqual(True, self.wordBreak("leetcode", ["leet", "code"]))

    def test2(self):
        self.assertEqual(True, self.wordBreak("applepenapple", ["apple", "pen"]))

    def test3(self):
        self.assertEqual(False, self.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
