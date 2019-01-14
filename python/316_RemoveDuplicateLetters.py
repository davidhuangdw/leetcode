from unittest import TestCase
# https://leetcode.com/problems/remove-duplicate-letters/


class RemoveDuplicateLetters(TestCase):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        done = set()
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        ret = []
        for ch in s:
            count[ch] -= 1
            if ch in done:
                continue
            while ret and count[ret[-1]] > 0 and ret[-1] > ch:
                done.remove(ret.pop())
            # reason: if ret[-1] cannot be remove, its previous also shouldn't remove, otherwise become bigger
            ret.append(ch)
            done.add(ch)
        return "".join(ret)

    def test1(self):
        self.assertEqual("abc", self.removeDuplicateLetters("bcabc"))

    def test2(self):
        self.assertEqual("acdb", self.removeDuplicateLetters("cbacdcbc"))

    def test3(self):
        self.assertEqual("bac", self.removeDuplicateLetters("cbac"))
