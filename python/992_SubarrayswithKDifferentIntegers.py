from unittest import TestCase
# https://leetcode.com/problems/subarrays-with-k-different-integers/
import collections


class MultiSet:
    def __init__(self):
        self.size = 0
        self.cnt = collections.defaultdict(lambda : 0)

    def add(self, v):
        self.cnt[v] += 1
        if self.cnt[v] == 1:
            self.size += 1

    def remove(self, v):
        self.cnt[v] -=1
        if self.cnt[v] == 0:
            self.size -= 1


class SubarrayswithKDifferentIntegers(TestCase):
    def subarraysWithKDistinct(self, A: 'List[int]', K: 'int') -> 'int':
        sj, sk = MultiSet(), MultiSet()
        i, j, k, n, res = 0, 0, 0, len(A), 0
        while i < n:
            while sj.size < K and j < n:
                sj.add(A[j])
                j += 1
            if sj.size < K:
                break
            while sk.size <= K and k < n:
                sk.add(A[k])
                k += 1
            res += k - j + (1 if sk.size == K else 0)
            sj.remove(A[i])
            sk.remove(A[i])
            i += 1
        return res

    def test1(self):
        self.assertEqual(7, self.subarraysWithKDistinct([1,2,1,2,3], 2))

    def test2(self):
        self.assertEqual(3, self.subarraysWithKDistinct([1,2,1,3,4], 3))

