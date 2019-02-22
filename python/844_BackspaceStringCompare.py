from unittest import TestCase
# https://leetcode.com/problems/backspace-string-compare
import itertools


class BackspaceStringCompare(TestCase):
    def backspaceCompare(self, S: 'str', T: 'str') -> 'bool':
        def gen(s):
            cnt = 0
            for ch in reversed(s):
                if ch == '#':
                    cnt += 1
                elif cnt > 0:
                    cnt -= 1
                else:
                    yield ch
        return all(a == b for a, b in itertools.zip_longest(gen(S), gen(T)))

    def test1(self):
        self.assertEqual(True, self.backspaceCompare("ab#c", "ad#c"))

    def test1(self):
        self.assertEqual(True, self.backspaceCompare("a##c", "#a#c"))

    def test1(self):
        self.assertEqual(False, self.backspaceCompare("a#c", "b"))

        

