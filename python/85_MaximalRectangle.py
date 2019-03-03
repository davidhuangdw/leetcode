from unittest import TestCase
# https://leetcode.com/problems/maximal-rectangle


class MaximalRectangle(TestCase):
    def maximalRectangle(self, matrix: 'List[List[str]]') -> 'int':
        if not matrix: return 0
        n, m = len(matrix), len(matrix[0])
        cur, res = [0] * m, 0
        for i in range(n):
            st = []
            for j in range(m+1):
                if j < m:
                    cur[j] = cur[j]+1 if matrix[i][j] == '1' else 0
                while st and (j == m or cur[st[-1]] >= cur[j]):
                    h = cur[st.pop()]
                    res = max(res, h*(j-1-(st[-1] if st else -1)))
                st.append(j)
        return res

    def test1(self):
        matrix = [
            ["1","0","1","0","0"],
            ["1","0","1","1","1"],
            ["1","1","1","1","1"],
            ["1","0","0","1","0"]
        ]
        self.assertEqual(6, self.maximalRectangle(matrix))


        

