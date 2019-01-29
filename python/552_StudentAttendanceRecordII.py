from unittest import TestCase
# https://leetcode.com/problems/student-attendance-record-ii/


class StudentAttendanceRecordII(TestCase):
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

    def test1(self):
        self.assertEqual(8, self.checkRecord(2))

