from unittest import TestCase
# https://leetcode.com/problems/word-break-ii/


class TrieNode:
    def __init__(self):
        self.nxt = {}
        self.end = False

    def add(self, word):
        node = self
        for ch in word:
            if ch not in node.nxt:
                node.nxt[ch] = TrieNode()
            node = node.nxt[ch]
        node.end = True
        return node


class WordBreakII(TestCase):
    def wordBreak(self, s: str, wordDict: 'List[str]') -> 'List[str]':
        words = set(wordDict)
        mxlen = max(map(len, wordDict)) if wordDict else 0

        n = len(s)
        pre = [[] for _ in range(n+1)]

        for i in range(0, n):
            if i and not pre[i]: continue
            for j in range(i+1, min(n+1, i+mxlen+1)):
                if s[i:j] in words:
                    pre[j].append(i)
        result = []

        def build(j, path):
            if j:
                for i in pre[j]:
                    path.append(s[i:j])
                    build(i, path)
                    path.pop()
            else:
                result.append(" ".join(reversed(path)))
        build(n, [])
        return result

    # # by trie tree
    # def wordBreak(self, s: str, wordDict: 'List[str]') -> 'List[str]':
    #     n, root = len(s), TrieNode()
    #     for word in wordDict:
    #         root.add(word)
    #
    #     pre = [[] for _ in range(n+1)]
    #     for i in range(n):
    #         if i and not pre[i]: continue
    #         node = root
    #         for j in range(i, n):
    #             if s[j] not in node.nxt: break
    #             node = node.nxt[s[j]]
    #             if node.end:
    #                 pre[j+1].append(i)
    #     result = []
    #
    #     def backtrace(j, path):
    #         if j:
    #             for i in pre[j]:
    #                 path.append(s[i:j])
    #                 backtrace(i, path)
    #                 path.pop()
    #         else:
    #             result.append(" ".join(reversed(path)))
    #     backtrace(n, [])
    #     return result

    def test1(self):
        self.assertEqual({
            "cats and dog",
            "cat sand dog"
        }, set(self.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])))

    def test2(self):
        self.assertEqual({
            "pine apple pen apple",
            "pineapple pen apple",
            "pine applepen apple"
        }, set(self.wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"])))

    def test3(self):
        self.assertEqual([
        ], self.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
