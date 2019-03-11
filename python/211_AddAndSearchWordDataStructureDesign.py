from unittest import TestCase
# https://leetcode.com/problems/add-and-search-word-data-structure-design


class TrieNode:
    def __init__(self):
        self.nxt = {}
        self.end = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # self.root = TrieNode()
        self.root = {}

    def addWord(self, word: 'str') -> 'None':
        """
        Adds a word into the data structure.
        """
        node = self.root
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node['$'] = None

    def search(self, word: 'str') -> 'bool':
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        n = len(word)

        def dfs(i, node):
            while node and i < n and word[i] != '.':
                node = node.get(word[i])
                i += 1
            if not node: return False
            if i == n: return '$' in node
            return any(dfs(i+1, node) for ch, node in node.items())
        return dfs(0, self.root)


class WordDictionaryTests(TestCase):
    def test1(self):
        w = WordDictionary()
        w.addWord("bad")
        w.addWord("dad")
        w.addWord("mad")
        self.assertEqual(False, w.search("pad"))
        self.assertEqual(True, w.search("bad"))
        self.assertEqual(True, w.search(".ad"))
        self.assertEqual(True, w.search("b.."))

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

