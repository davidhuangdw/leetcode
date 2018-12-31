from unittest import TestCase

# https://leetcode.com/problems/valid-parentheses/submissions/


class ValidParentheses(TestCase):
    TO_LEFT = {
        ')': '(',
        ']': '[',
        '}': '{',
    }

    def isValid(self, s):
        lefts = []
        for ch in s:
            if self.TO_LEFT.get(ch):
                if not lefts or lefts.pop() != self.TO_LEFT[ch]:
                    return False
            else:
                lefts.append(ch)
        return len(lefts) == 0

    def test1(self):
        self.assertEqual(True, self.isValid("()[]{}"))

    def test2(self):
        self.assertEqual(True, self.isValid("{[()]}[]"))

    def test3(self):
        self.assertEqual(False, self.isValid("[(])"))


