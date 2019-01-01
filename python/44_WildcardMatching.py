from unittest import TestCase
# https://leetcode.com/problems/wildcard-matching/


class WildcardMatching(TestCase):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        n = len(s)
        mat = [True] + [False]*n

        for i in range(len(p)):
            if p[i] == "*":
                for j in range(n):
                    mat[j+1] = mat[j+1] or mat[j]
            else:
                # mt[0] = False         # bug!: should assign at last because right to left
                for j in range(n-1, -1, -1):
                    mat[j+1] = (p[i] == s[j] or p[i] == '?') and mat[j]
                mat[0] = False

        return mat[n]

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
