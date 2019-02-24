from unittest import TestCase
# https://leetcode.com/problems/bulls-and-cows


class BullsAndCows(TestCase):
    def getHint(self, secret: 'str', guess: 'str') -> 'str':
        matches, contains = 0, 0
        scount, gcount = {}, {}
        for s, g in zip(secret, guess):
            if s == g:
                matches += 1
            else:
                scount[s] = scount.get(s, 0) + 1
                gcount[g] = gcount.get(g, 0) + 1

        for k, v in scount.items():
            contains += min(v, gcount.get(k, 0))

        return f"{matches}A{contains}B"

    def test1(self):
        self.assertEqual("1A3B", self.getHint("1807", "7810"))

    def test2(self):
        self.assertEqual("1A1B", self.getHint("1123", "0111"))


