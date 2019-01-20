# https://leetcode.com/problems/guess-number-higher-or-lower/
def guess(num):
    return 1


class GuessNumberHigherorLower:
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l < r:
            m = (l+r) >> 1
            g = guess(m)
            if g == 0:
                return m
            elif g < 0:
                r = m-1
            else:
                l = m+1
        return l
