from unittest import TestCase
# https://leetcode.com/problems/frog-jump/


class FrogJump(TestCase):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        if stones[1] != 1: return False
        last = stones[-1]
        stones = set(stones)
        tried = set()

        def dp(cur, k):
            if cur == last: return True
            if (cur, k) in tried: return False
            tried.add((cur, k))
            return any(dp(cur+nk, nk) for nk in range(max(1, k-1), k+2) if (cur+nk in stones))
        return dp(1, 1)

    def test1(self):
        self.assertEqual(True, self.canCross([0,1,3,5,6,8,12,17]))

    def test2(self):
        self.assertEqual(False, self.canCross([0,1,2,3,4,8,9,11]))
