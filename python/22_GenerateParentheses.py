from unittest import TestCase
# https://leetcode.com/problems/generate-parentheses/


class GenerateParenthesis(TestCase):
    def generateParenthesis(self, n):
        result = []

        def build(pre, nl):
            if len(pre) == n+n:
                result.append(pre)
            else:
                if nl < n:
                    build(pre+"(", nl+1)
                if nl > len(pre) - nl:
                    build(pre+")", nl)
        if n > 0:
            build("", 0)
        return result

    def test1(self):
        self.assertEqual([
            "((()))",
            "(()())",
            "(())()",
            "()(())",
            "()()()"
        ], self.generateParenthesis(3))


