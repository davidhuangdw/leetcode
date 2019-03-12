from unittest import TestCase
# https://leetcode.com/problems/implement-magic-dictionary
import collections


class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        
    def buildDict(self, dict: 'List[str]') -> 'None':
        """
        Build a dictionary through a list of words
        """
        for word in dict:
            node = self.root
            for ch in word:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node['$'] = None

    def search(self, word: 'str') -> 'bool':
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        i, n = 0, len(word)

        def dfs(i, node, diff=False):
            if not node: return False
            if i == n:
                return diff and '$' in node
            return dfs(i+1, node.get(word[i]), True) if diff else \
                any(dfs(i+1, node[ch], ch != word[i]) for ch in node)
        return dfs(0, self.root)


    # # by pre-process dict
    # def genKeys(self, word):
    #     for i in range(len(word)):
    #         yield word[:i] + '*' + word[i+1:]
    #
    # def buildDict(self, dict: 'List[str]') -> 'None':
    #     self.dict = set(dict)
    #     self.key_count = collections.Counter()
    #     for word in dict:
    #         for key in self.genKeys(word):
    #             self.key_count[key] += 1
    #
    # def search(self, word: 'str') -> 'bool':
    #     return any(self.key_count[key] > 1 or (self.key_count[key] == 1 and word not in self.dict)
    #                for key in self.genKeys(word))


class MagicDictionaryTests(TestCase):
    def test1(self):
        m = MagicDictionary()
        m.buildDict(["hello", "leetcode"])
        self.assertEqual(False, m.search("hello"))
        self.assertEqual(True, m.search("hhllo"))
        self.assertEqual(False, m.search("hell"))
        self.assertEqual(False, m.search("leetcoded"))

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)

