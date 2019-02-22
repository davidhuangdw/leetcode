from unittest import TestCase
# https://leetcode.com/problems/fruit-into-baskets


class FruitIntoBaskets(TestCase):
    def totalFruit(self, tree: 'List[int]') -> 'int':
        a = b = tree[0]
        res = cur = same = 0
        for c in tree:
            if c == b:
                cur += 1
                same += 1
            elif c == a:
                cur += 1
                same = 1
                a, b = b, a
            else:
                cur = same + 1
                same = 1
                a, b = b, c
            res = max(res, cur)
        return res

    def test1(self):
        self.assertEqual(3, self.totalFruit([0,1,2,2]))

    def test2(self):
        self.assertEqual(5, self.totalFruit([3,3,3,1,2,1,1,2,3,3,4]))

