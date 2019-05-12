from unittest import TestCase
# https://leetcode.com/problems/prefix-and-suffix-search
import collections


class WordFilter:

    # by store all combinations directly
    def __init__(self, words: 'List[str]'):
        self.result = res = {}
        for pos, word in enumerate(words):
            for i in range(len(word)+1):
                for j in range(len(word)+1):
                    res[(word[:i], word[j:])] = pos

    def f(self, prefix: 'str', suffix: 'str') -> 'int':
        return self.result[(prefix, suffix)] if (prefix, suffix) in self.result else -1


    # # by store the trie tree of prefix+'#'+word, and dfs to search all reached words
    # def __init__(self, words: 'List[str]'):
    #     self.root = root = {}
    #     for ind, word in enumerate(words):
    #         n = len(word)
    #         for i in range(n+1):
    #             w = word[i:] + '#' + word
    #             node = root
    #             for ch in w:
    #                 if ch not in node:
    #                     node[ch] = {}
    #                 node = node[ch]
    #             node['$'] = ind
    #
    # def f(self, prefix: 'str', suffix: 'str') -> 'int':
    #     word = f"{suffix}#{prefix}"
    #     n = len(word)
    #
    #     def dfs(i, node):
    #         if not node: return -1
    #         if i < n: return dfs(i+1, node.get(word[i]))
    #         return max(node[ch] if ch == '$' else dfs(i, node[ch]) for ch in node)
    #     return dfs(0, self.root)

# # set intersect
# class WordFilter:
#     def __init__(self, words):
#         d = {w: i for i, w in enumerate(words)}
#         self.pre = collections.defaultdict(set)
#         self.suf = collections.defaultdict(set)
#         for w, i in d.items():
#             n = len(w)
#             for j in range(n+1):
#                 if j < 11: self.pre[w[:j]].add(i)
#                 if n-j < 11: self.suf[w[j:]].add(i)
#
#     def f(self, prefix: 'str', suffix: 'str') -> 'int':
#         return max(self.pre[prefix] & self.suf[suffix], default=-1)
#
# # trie
# Trie = lambda: collections.defaultdict(Trie)
# WEIGHT = False
# class WordFilter:
#     def __init__(self, words):
#         self.trie = trie = Trie()
#         d = {w: i for i, w in enumerate(words)}
#         for w, i in d.items():
#             for j in range(max(0, len(w)-10), len(w)+1):
#                 node = trie
#                 for ch in w[j:] + '#' + w:
#                     node = node[ch]
#                     node[WEIGHT] = max(node.get(WEIGHT, -1), i)
#
#     def f(self, prefix: 'str', suffix: 'str') -> 'int':
#         node = self.trie
#         for ch in suffix + '#' + prefix:
#             if ch not in node: return -1
#             node = node[ch]
#         return node[WEIGHT]

class WordFilterTests(TestCase):
    def test1(self):
        w = WordFilter(["apple"])
        self.assertEqual(0, w.f("a", "e"))
        self.assertEqual(-1, w.f("b", "#"))


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)

