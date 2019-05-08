from unittest import TestCase
# https://leetcode.com/problems/wildcard-matching/


class WildcardMatching(TestCase):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        mat = [i == 0 for i in range(len(s)+1)]
        for pi in p:
            pre, mat[0] = mat[0], mat[0] and pi == '*'
            for j, sj in enumerate(s):
                pre, mat[j+1] = mat[j+1], mat[j+1] or mat[j] if pi == '*' else pre and pi in (sj, '?')
        return mat[-1]

    def test1(self):
        self.assertEqual(False, self.isMatch("aa", "a"))

    def test2(self):
        self.assertEqual(True, self.isMatch("aa", "*"))

    def test3(self):
        self.assertEqual(False, self.isMatch("cb", "?a"))

    def test4(self):
        self.assertEqual(True, self.isMatch("abceb", "*a*b"))

    def test5(self):
        self.assertEqual(False, self.isMatch("acdcb", "a*c?b"))

    def test6(self):
        self.assertEqual(False, self.isMatch("aab", "c*a*b"))
