from unittest import TestCase
# https://leetcode.com/problems/longest-substring-without-repeating-characters


class LongestSubstringWithoutRepeatingCharacters(TestCase):
    def lengthOfLongestSubstring(self, s: 'str') -> 'int':
        last = {}
        j, res = -1, 0
        for i, c in enumerate(s):
            if c in last:
                j = max(j, last[c])
            res = max(res, i-j)
            last[c] = i
        return res

    def test1(self):
        self.assertEqual(3, self.lengthOfLongestSubstring("abcabcbb"))

    def test2(self):
        self.assertEqual(1, self.lengthOfLongestSubstring( "bbbbb"))

    def test3(self):
        self.assertEqual(3, self.lengthOfLongestSubstring("pwwkew"))
        

