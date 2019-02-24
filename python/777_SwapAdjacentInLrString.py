from unittest import TestCase
# https://leetcode.com/problems/swap-adjacent-in-lr-string


class SwapAdjacentInLrString(TestCase):
    def canTransform(self, start: 'str', end: 'str') -> 'bool':
        start, end, n = list(start), list(end), len(start)
        if n != len(end): return False

        def next(s, ch, begin):
            for k in range(begin, n):
                if s[k] == ch: return k
            return n

        def valid(L, R):
            i = j = 0
            while True:
                ni = next(start, L, i)
                nj = next(end, L, j)
                if ni >= n or nj >= n:
                    return ni == nj
                if ni < nj or R in start[nj:ni]:
                    return False
                i, j = ni+1, nj+1

        if not valid('L', 'R'): return False
        start.reverse()
        end.reverse()
        return valid('R', 'L')

    def canTransformByIndex(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        def indexes(s):
            return [(i, c) for i, c in enumerate(s) if c in "RL"]
        start, end = indexes(start), indexes(end)
        return len(start) == len(end) and all(c1 == c2 and (i1 <= i2 if c1 == 'R' else i1 >= i2) for (i1, c1), (i2, c2) in zip(start, end))

    def test1(self):
        self.assertEqual(True, self.canTransform("RXXLRXRXL", "XRLXXRRLX"))

    def test2(self):
        self.assertEqual(True, self.canTransform("XLXRRXXRXX", "LXXXXXXRRR"))


