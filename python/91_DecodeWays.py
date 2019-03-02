from unittest import TestCase
# https://leetcode.com/problems/decode-ways


class DecodeWays(TestCase):
    def numDecodings(self, s: 'str') -> 'int':
        pp, pre, below_six, a = 0, 1, "0123456", ''
        for b in s:
            if not (pp or pre): break
            cnt = (pre if b != '0' else 0) + \
                  (pp if a == '1' or (a == '2' and b in below_six) else 0)
            pp, pre, a = pre, cnt, b
        return pre

    # use int()
    # def numDecodings(self, s: 'str') -> 'int':
    #     pp, pre, a = 0, 1, ''
    #     for b in s:
    #         if not (pp or pre): break
    #         cnt = (pre if b != '0' else 0) + \
    #               (pp if 9 < int(a+b) < 27 else 0)
    #         pp, pre, a = pre, cnt, b
    #     return pre

    def test1(self):
        self.assertEqual(2, self.numDecodings("12"))

    def test2(self):
        self.assertEqual(3, self.numDecodings("226"))

    def test3(self):
        self.assertEqual(0, self.numDecodings("012"))

    def test4(self):
        self.assertEqual(1, self.numDecodings("10"))

    def test5(self):
        self.assertEqual(1, self.numDecodings("27"))

