from unittest import TestCase
# https://leetcode.com/problems/reverse-vowels-of-a-string/


class ReverseVowelsofaString(TestCase):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = "aeiouAEIOU"
        s = list(s)
        inds = list(filter(lambda i: s[i] in vowels, range(len(s))))
        for i in range(int(len(inds)/2)):
            s[inds[i]], s[inds[-1-i]] = s[inds[-1-i]], s[inds[i]]
        return "".join(s)

    def test1(self):
        self.assertEqual("holle", self.reverseVowels("hello"))

    def test2(self):
        self.assertEqual("leotcede", self.reverseVowels("leetcode"))
