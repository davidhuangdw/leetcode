from unittest import TestCase
# https://leetcode.com/problems/word-search-ii/


class Node:
    count = 0

    def __init__(self):
        Node.count += 1
        self.id = Node.count
        self.end = False
        self.next = {}

    def insert(self, word):
        if not word:
            self.end = True
        else:
            ch = word[0]
            if not self.next.get(ch):
                self.next[ch] = Node()
            self.next[ch].insert(word[1:])


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        self.root.insert(word)


class WordSearchII:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie = Trie()
        for w in words:
            trie.insert(w)

        result = set()
        visited = set()

        def search(node, i, j, pre):
            if not (0 <= i < len(board) and 0 <= j < len(board[i])) or (i, j) in visited:
                return
            ch = board[i][j]
            node = node.next.get(ch)
            if not node:
                return
            pre += ch
            if node.end:
                result.add(pre)
            visited.add((i, j))
            for (ni, nj) in ((i,j+1), (i+1,j), (i,j-1), (i-1,j)):
                search(node, ni, nj, pre)
            visited.remove((i, j))

        for i in range(len(board)):
            for j in range(len(board[i])):
                search(trie.root, i, j, "")
        return list(result)


class Tests(TestCase):
    def test1(self):
        search = WordSearchII()
        self.assertEqual({"eat", "oath"}, set(
            search.findWords(
                [
                    ['o', 'a', 'a', 'n'],
                    ['e', 't', 'a', 'e'],
                    ['i', 'h', 'k', 'r'],
                    ['i', 'f', 'l', 'v']
                ],
                ["oath", "pea", "eat", "rain"]
            )
        ))

    def test2(self):
        search = WordSearchII()
        self.assertEqual([],
            search.findWords(
                [
                    ["a", "a"]
                ],
                ["aaa"]
            )
        )

    def test3(self):
        search = WordSearchII()
        self.assertEqual(["a"],
                         search.findWords(
                             [
                                 ["a"]
                             ],
                             ["a"]
                         ))




