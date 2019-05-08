from unittest import TestCase
# https://leetcode.com/problems/moving-stones-until-consecutive-ii


class MovingStonesUntilConsecutiveIi(TestCase):
    def numMovesStonesII(self, stones: "List[int]") -> "List[int]":
        stones.sort()
        n = len(stones)
        j, mi = 0, n
        # max: distance -1 each time except for the first time
        mx = (stones[-1]+1-stones[0]) - n - (min(stones[1]-stones[0], stones[-1]-stones[-2])-1)
        for i, l in enumerate(stones):
            while j < n and stones[j] < l+n:
                j += 1
            x = n-(j-i)
            if x == 1 and stones[j-1]+1-stones[i] == n-1: x += 1
            mi = min(mi, x)
            if j >= n: break
        return [mi, mx]

    def test1(self):
        self.assertEqual([1,2], self.numMovesStonesII([7,4,9]))

    def test2(self):
        self.assertEqual([2,3], self.numMovesStonesII([6,5,4,3,10]))

    def test3(self):
        self.assertEqual([0,0], self.numMovesStonesII([100,101,104,102,103]))

