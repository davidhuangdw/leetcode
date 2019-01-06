from unittest import TestCase
# https://leetcode.com/problems/implement-trie-prefix-tree/


class TrieNode:
    def __init__(self):
        self.end = False
        self.next = {}


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for ch in word:
            if not node.next.get(ch):
                node.next[ch] = TrieNode()
            node = node.next[ch]
        node.end = True

    def walk(self, word):
        node = self.root
        for ch in word:
            if not node.next.get(ch):
                return None
            node = node.next[ch]
        return node

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.walk(word)
        return bool(node and node.end)

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        return bool(self.walk(prefix))


class Tests(TestCase):
    def test1(self):
        trie = Trie()
        trie.insert("apple")
        self.assertTrue(trie.search("apple"))
        self.assertTrue(not trie.search("app"))
        self.assertTrue(trie.startsWith("app"))
        trie.insert("app")
        self.assertTrue(trie.search("app"))
