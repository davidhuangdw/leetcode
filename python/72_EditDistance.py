from unittest import TestCase
# https://leetcode.com/problems/edit-distance


class EditDistance(TestCase):
    def minDistance(self, word1: 'str', word2: 'str') -> 'int':
        a, b = word1, word2
        n, m = len(a), len(b)
        dp = [i for i in range(m+1)]
        for i in range(n):
            pre = dp[0]
            dp[0] += 1
            for j in range(m):
                pre_now = dp[j+1]
                if a[i] == b[j]:
                    dp[j+1] = pre
                else:
                    dp[j+1] = 1+min(pre, dp[j], dp[j+1])
                pre = pre_now
        return dp[m]

    def test1(self):
        self.assertEqual(3, self.minDistance("horse", "ros"))

    def test2(self):
        self.assertEqual(5, self.minDistance("intention", "execution"))
        

