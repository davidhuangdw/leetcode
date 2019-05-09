from unittest import TestCase
# https://leetcode.com/problems/student-attendance-record-ii/
import collections


class StudentAttendanceRecordII(TestCase):
    # forward update: cur -> next_state: dp[i][next_state] += dp[i-1][cur]
    # add P: (a, l) -> (a, 0)
    # add A: (0, l) -> (1, 0)
    # add L: (a, l) -> (a, l+1)

    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1, 0, 0, 0, 0, 0]
        mod = 1e9 + 7
        for r in range(1, n+1):
            dp = [sum(dp[:3]) % mod] + dp[:2] + [sum(dp) % mod] + dp[3:-1]
        return int(sum(dp) % mod)

    # def checkRecord(self, n):
    #     dp = collections.Counter()
    #     dp[(0, 0)] = 1
    #     mod = 1e9 + 7
    #     for r in range(1, n+1):
    #         nxt = collections.Counter()
    #         for a in range(2):
    #             for l in range(3):
    #                 pre = dp[(a, l)] % mod
    #                 nxt[(a, 0)] += pre          # P
    #                 if not a:
    #                     nxt[(1, 0)] += pre      # A
    #                 if l+1 < 3:
    #                     nxt[(a, l+1)] += pre    # L
    #         dp = nxt
    #     return int(sum(dp.values()) % mod)

    def test1(self):
        self.assertEqual(8, self.checkRecord(2))

