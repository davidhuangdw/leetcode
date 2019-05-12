from unittest import TestCase
# https://leetcode.com/problems/special-binary-string/


class SpecialBinaryString(TestCase):
    def makeLargestSpecial(self, S):
        """
        :type S: str
        :rtype: str
        """
        if not S: return S
        mountains = []
        n, i = len(S), 0
        while i < n:
            j = i + 1
            cnt = 1
            while cnt > 0:
                cnt += 1 if S[j] == '1' else -1
                j += 1
            mountains.append(f"1{self.makeLargestSpecial(S[i+1:j-1])}0")
            i = j
        return "".join(sorted(mountains, reverse=True))

    # def makeLargestSpecial(self, S):
    #     if S == "": return S
    #     subs, d, pre = [], 0, 0
    #     for i, ch in enumerate(S):
    #         d += 1 if ch == '1' else -1
    #         if d == 0:
    #             subs.append(f"1{self.makeLargestSpecial(S[pre+1:i])}0")
    #             pre = i+1
    #     return "".join(sorted(subs, reverse=True))


    def test1(self):
        self.assertEqual("11100100", self.makeLargestSpecial("11011000"))
