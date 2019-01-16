from unittest import TestCase
# https://leetcode.com/problems/maximum-product-of-word-lengths/


class MaximumProductofWordLengths(TestCase):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        def bits(word):
            bits = 0
            for ch in word:
                bits |= 1<<(ord(ch) - ord('a'))
            return bits

        n = len(words)
        word_bits = list(map(bits, words))
        ret = 0
        for i in range(n):
            for j in range(i+1, n):
                if not (word_bits[i] & word_bits[j]):
                    ret = max(ret, len(words[i])*len(words[j]))
        return ret

    def test1(self):
        self.assertEqual(16, self.maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))

    def test2(self):
        self.assertEqual(4, self.maxProduct(["a","ab","abc","d","cd","bcd","abcd"]))

    def test3(self):
        self.assertEqual(0, self.maxProduct(["a","aa","aaa","aaaa"]))
