from unittest import TestCase
# https://leetcode.com/problems/candy


class Candy(TestCase):
    def candy(self, ratings: 'List[int]') -> 'int':
        j, least, n, res = 0, 1, len(ratings), 0

        def cal(k):
            return int(k*(k+1)/2) + max(0, least-k)
        for i in range(1, n):
            if ratings[i] >= ratings[i-1]:
                res += cal(i-j)
                least = 1 if ratings[i] == ratings[i-1] else 2 if i-j > 1 else least+1
                j = i
        res += cal(n-j)
        return res

    def test1(self):
        self.assertEqual(5, self.candy([1,0,2]))

    def test2(self):
        self.assertEqual(8, self.candy([3,0,1,2]))

    def test3(self):
        self.assertEqual(4, self.candy([1,2,2]))


