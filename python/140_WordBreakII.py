from unittest import TestCase
# https://leetcode.com/problems/word-break-ii/


class WordBreakII(TestCase):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        words = set(wordDict)
        mxlen = max(map(len, wordDict)) if wordDict else 0

        n = len(s)
        pre = [[] for i in range(n)]

        for i in range(0, n):
            if not (i == 0 or pre[i-1]):
                continue
            for j in range(i, min(n, i+mxlen)):
                if s[i:j+1] in words:
                    pre[j].append(i-1)
        result = []

        def build(j, backs):
            if j == -1:
                result.append(" ".join(reversed(backs)))
            else:
                for i in pre[j]:
                    build(i, backs+[s[i+1:j+1]])
        build(n-1, [])
        return list(reversed(result))

    def test1(self):
        self.assertEqual([
            "cats and dog",
            "cat sand dog"
        ], self.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))

    def test2(self):
        self.assertEqual([
            "pine apple pen apple",
            "pineapple pen apple",
            "pine applepen apple"
        ], self.wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]))

    def test3(self):
        self.assertEqual([
        ], self.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
