from unittest import TestCase
# https://leetcode.com/problems/couples-holding-hands/


class CouplesHoldingHands(TestCase):
    def minSwapsCouples(self, row: 'List[int]') -> int:
        index = dict()
        for i,v in enumerate(row):
            index[v] = i

        count = 0
        for i in range(0, len(row), 2):
            a, b = row[i], row[i+1]
            aa = row[i] ^ 1
            if aa != b:
                count += 1
                row[index[aa]] = b
                index[b] = index[aa]
        return count

    def test1(self):
        self.assertEqual(1, self.minSwapsCouples([0, 2, 1, 3]))

    def test2(self):
        self.assertEqual(0, self.minSwapsCouples([3, 2, 0, 1]))
