from unittest import TestCase
# https://leetcode.com/problems/word-ladder-ii
import collections


class WordLadderIi(TestCase):
    # return all shortest paths: each node may have many previous nodes of the same distance
    def findLadders(self, beginWord: 'str', endWord: 'str', wordList: 'List[str]') -> 'List[List[str]]':
        if endWord not in wordList: return []
        m, conn = len(beginWord), collections.defaultdict(list)

        def genKeys(word):
            for i in range(m):
                yield word[:i] + '*' + word[i+1:]
        for w in wordList:
            for key in genKeys(w):
                conn[key].append(w)

        que, prev = collections.deque([beginWord]), collections.defaultdict(list)
        dis, shortest, res = {beginWord: 1}, float("inf"), []
        while que:
            word = que.popleft()
            if word == endWord:
                shortest = dis[word]
                break
            if dis[word] >= shortest: continue
            for key in genKeys(word):
                for nxt in conn[key]:
                    if nxt not in dis:
                        dis[nxt] = dis[word] + 1
                        que.append(nxt)
                    if dis[word] + 1 == dis[nxt]:
                        prev[nxt].append(word)

        def backtrace(path):
            if len(path) == shortest:
                res.append(path[::-1])
            for w in prev[path[-1]]:
                path.append(w)
                backtrace(path)
                path.pop()
        backtrace([endWord])
        return res

    # # bidirection:
    # def findLadders(self, beginWord: 'str', endWord: 'str', wordList: 'List[str]') -> 'List[List[str]]':
    #     if endWord not in wordList: return []
    #     m, conn = len(beginWord), collections.defaultdict(list)
    #
    #     def genKeys(word):
    #         for i in range(m):
    #             yield word[:i] + '*' + word[i+1:]
    #     for w in wordList:
    #         for key in genKeys(w):
    #             conn[key].append(w)
    #
    #     ques = [collections.deque([beginWord]), collections.deque([endWord])]
    #     prevs = [collections.defaultdict(set), collections.defaultdict(set)]
    #     diss, meet = [{beginWord: 1}, {endWord: 1}], set()
    #
    #     while all(ques) and not meet:
    #         for i in range(2):
    #             if meet: break
    #             size = len(ques[i])
    #             for _ in range(size):
    #                 word = ques[i].popleft()
    #                 for key in genKeys(word):
    #                     for nxt in conn[key]:
    #                         if nxt not in diss[i]:
    #                             diss[i][nxt] = diss[i][word] + 1
    #                         if diss[i][word] + 1 > diss[i][nxt]:
    #                             continue
    #                         prevs[i][nxt].add(word)
    #                         if nxt in diss[i ^ 1]:
    #                             meet.add(nxt)
    #                         else:
    #                             ques[i].append(nxt)
    #
    #     def backtrace(path, prev):
    #         last = path[-1]
    #         if prev[last]:
    #             for w in list(prev[last]):
    #                 path.append(w)
    #                 for res in backtrace(path, prev):
    #                     yield res
    #                 path.pop()
    #         else:
    #             yield path[::-1]
    #     return list(b_path[:-1] + e_path[::-1] for mt in meet
    #                 for b_path in backtrace([mt], prevs[0])
    #                 for e_path in backtrace([mt], prevs[1]))

    def test1(self):
        self.assertEqual(set(map(tuple, [["hit","hot","lot","log","cog"],["hit","hot","dot","dog","cog"]])),
                            set(map(tuple, self.findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"]))))

    def test2(self):
        self.assertEqual([], self.findLadders("hit", "cog", ["hot","dot","dog","lot","log"]))

    def test3(self):
        self.assertEqual([["red","ted","tad","tax"],["red","ted","tex","tax"],["red","rex","tex","tax"]],
                         self.findLadders("red", "tax", ["ted", "tex", "red", "tax", "tad", "den", "rex", "pee"]))


