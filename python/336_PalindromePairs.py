from unittest import TestCase
# https://leetcode.com/problems/palindrome-pairs/


class PalindromePairs(TestCase):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        words_index = {}
        for (i, word) in enumerate(words):
            words_index[word] = i

        def isPal(word):
            for i in range(int(len(word)/2)):
                if word[i] != word[-1-i]:
                    return False
            return True
        ret = []
        for (i, word) in enumerate(words):
            for k in range(len(word)+1):
                if isPal(word[k:]):
                    j = words_index.get(word[:k][::-1])
                    if j not in (None, i):
                        ret.append([i, j])

                if k > 0 and isPal(word[:k]):
                    j = words_index.get(word[k:][::-1])
                    if j not in (None, i):
                        ret.append((j, i))

        return list(map(list, ret))

    def test1(self):
        self.assertEqual(sorted([[0,1],[1,0],[3,2],[2,4]]), sorted(self.palindromePairs(["abcd","dcba","lls","s","sssll"])))

    def test2(self):
        self.assertEqual(sorted([[0,1],[1,0]]), sorted(self.palindromePairs(["bat","tab","cat"])))

    def test3(self):
        self.assertEqual(sorted([[3,0],[1,3],[4,0],[2,4],[5,0],[0,5]]), sorted(self.palindromePairs(["a","b","c","ab","ac","aa"])))
