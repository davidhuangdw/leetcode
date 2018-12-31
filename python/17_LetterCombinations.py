from unittest import TestCase

# https://leetcode.com/problems/letter-combinations-of-a-phone-number/


class LetterCombinations(TestCase):
    LETTERS = [
        "abc",
        "def",
        "ghi",
        "jkl",
        "mno",
        "pqrs",
        "tuv",
        "wxyz",
    ]

    def letterCombinations(self, digits):
        result = []

        def build(prefix, i):
            if i >= len(digits):
                result.append(prefix)
            else:
                d = ord(digits[i]) - ord('2')
                for ch in self.LETTERS[d]:
                    build(prefix + ch, i + 1)

        if digits:
            build("", 0)
        return result


    def test1(self):
        self.assertEqual(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"], self.letterCombinations("23"))

    def test2(self):
        self.assertEqual([], self.letterCombinations(""))
