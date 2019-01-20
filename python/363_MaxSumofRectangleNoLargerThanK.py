from unittest import TestCase
# https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/


class MaxSumofRectangleNoLargerThanK(TestCase):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not (matrix and matrix[0]): return None
        n, m = len(matrix), len(matrix[0])
        if n > m:
            matrix = list(zip(*matrix))
            n, m = m, n
        ret = float("-inf")

        def merge(sums):
            nonlocal ret
            if len(sums) <= 1:
                return sums
            hf = len(sums) >> 1
            left = merge(sums[:hf])
            right = merge(sums[hf:])
            i, j = 0, 0
            sorted = []
            for l in left:
                while i < len(right) and right[i] - l <= k:
                    i += 1
                if i-1 >= 0:
                    ret = max(ret, right[i-1] - l)
                while j < len(right) and right[j] <= l:
                    sorted.append(right[j])
                    j += 1
                sorted.append(l)
            return sorted + right[j:]
        for i in range(n):
            cols = [0] * m
            for j in range(i, n):
                sums = [0]
                for c in range(m):
                    cols[c] += matrix[j][c]
                    sums.append(sums[-1] + cols[c])
                merge(sums)
        return ret

    def test1(self):
        self.assertEqual(2, self.maxSumSubmatrix([[1,0,1],[0,-2,3]], 2))



