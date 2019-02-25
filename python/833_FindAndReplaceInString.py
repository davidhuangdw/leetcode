from unittest import TestCase
# https://leetcode.com/problems/find-and-replace-in-string


class FindAndReplaceInString(TestCase):
    def findReplaceString(self, S: 'str', indexes: 'List[int]', sources: 'List[str]', targets: 'List[str]') -> 'str':
        order = dict((i, (src, tar)) for i, src, tar in zip(indexes, sources, targets))
        order = [(i, *order[i]) for i in range(len(S)) if i in order]
        pre, words = 0, []
        for i, src, tar in order:
            if S[i:i+len(src)] == src:
                words.append(S[pre:i])
                pre = i+len(src)
                words.append(tar)
        words.append(S[pre:])
        return "".join(words)

    def test1(self):
        self.assertEqual("eeebffff", self.findReplaceString("abcd", [0,2], ["a","cd"], ["eee","ffff"]))

    def test2(self):
        self.assertEqual("eeecd", self.findReplaceString("abcd", [0,2], ["ab","ec"], ["eee","ffff"]))

