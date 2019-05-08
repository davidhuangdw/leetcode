from unittest import TestCase
# https://leetcode.com/problems/minimum-score-triangulation-of-polygon


class MinimumScoreTriangulationOfPolygon(TestCase):
    def minScoreTriangulation(self, A: 'List[int]') -> int:
        n = len(A)
        dp = [[0 for i in range(n)] for _ in range(n)]
        for d in range(2, n):
            for i in range(0, n-d):
                j = i+d
                dp[i][j] = min(A[i]*A[j]*A[k]+dp[i][k]+dp[k][j] for k in range(i+1,j))
        return dp[0][n-1]

    def test1(self):
        self.assertEqual(6, self.minScoreTriangulation([1,2,3]))

    def test2(self):
        self.assertEqual(144, self.minScoreTriangulation([3,7,4,5]))

    def test3(self):
        self.assertEqual(13, self.minScoreTriangulation([1,3,1,4,1,5]))

