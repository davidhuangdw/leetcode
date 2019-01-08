from unittest import TestCase
# https://leetcode.com/problems/shortest-palindrome/


class ShortestPalindrome(TestCase):
    def shortestPalindrome(self, s):
        """
        :type cat: str
        :rtype: str
        """
        construct = s + "#" + s[::-1]
        f = [0]*len(construct)
        for i in range(1, len(construct)):
            j = f[i-1]
            while j > 0 and construct[j] != construct[i]:
                j = f[j-1]
            f[i] = j+1 if construct[j] == construct[i] else 0
        return s[f[-1]:][::-1] + s

    def test1(self):
        self.assertEqual("aaacecaaa", self.shortestPalindrome("aacecaaa"))

    def test2(self):
        self.assertEqual("dcbabcd", self.shortestPalindrome("abcd"))
