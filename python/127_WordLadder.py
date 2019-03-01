from unittest import TestCase
# https://leetcode.com/problems/word-ladder
import collections


class WordLadder(TestCase):
    def ladderLength(self, beginWord: 'str', endWord: 'str', wordList: 'List[str]') -> 'int':
        wordList = set(wordList)
        if endWord not in wordList: return 0
        que = collections.deque([(beginWord, 1)])
        A = ord('a')
        while que:
            word, k = que.popleft()
            for i, c in enumerate(word):
                cd = ord(c) - A
                for d in range(26):
                    if d == cd: continue
                    nxt = word[:i] + chr(A+d) + word[i+1:]
                    if nxt == endWord: return k+1
                    if nxt in wordList:
                        wordList.remove(nxt)
                        que.append((nxt, k+1))
        return 0

    # pre-process: O(n*w) < O(n*w*26); + bidirectional BFS
    # def ladderLength(self, beginWord: 'str', endWord: 'str', wordList: 'List[str]') -> 'int':
    #     def genKeys(word):
    #         for i in range(len(word)):
    #             yield word[:i] + '*' + word[i+1:]
    #     hasEnd, conn = False, collections.defaultdict(list)
    #     for w in wordList:
    #         if w == endWord:
    #             hasEnd = True
    #             continue
    #         for i in range(len(w)):
    #             conn[w[:i] + '*' + w[i+1:]].append(w)
    #     if not hasEnd: return 0
    #     begin_keys, end_keys = {}, {}
    #     begin_que, end_que = collections.deque([(beginWord, 0)]), collections.deque([(endWord, 0)])
    #
    #     def forward(que, cur, other):
    #         word, k = que.popleft()
    #         for key in genKeys(word):
    #             if key in cur: continue
    #             if key in other:
    #                 return k + other[key]
    #             cur[key] = k+1
    #             for w in conn[key]:
    #                 que.append((w, k+1))
    #     while begin_que and end_que:
    #         res = forward(begin_que, begin_keys, end_keys) or forward(end_que, end_keys, begin_keys)
    #         if res: return res+1
    #     return 0

    def test1(self):
        self.assertEqual(5, self.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))

    def test2(self):
        self.assertEqual(0, self.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]))
