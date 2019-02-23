from unittest import TestCase
# https://leetcode.com/problems/odd-even-jump


class OddEvenJump(TestCase):
    def oddEvenJumps(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n, res = len(A), 1
        next_lower, next_higher, stack = [0]*n, [0]*n, []       # 0 is impossible
        for v, i in sorted((v, i) for i, v in enumerate(A)):
            while stack and stack[-1] < i:
                next_higher[stack.pop()] = i
            stack.append(i)

        stack = []
        for v, i in sorted((-v, i) for i, v in enumerate(A)):
            while stack and stack[-1] < i:
                next_lower[stack.pop()] = i
            stack.append(i)

        good = [(True, True)]*n
        for i in range(n-2, -1, -1):
            odd = next_higher[i] and good[next_higher[i]][1]
            even = next_lower[i] and good[next_lower[i]][0]
            if odd: res += 1
            good[i] = odd, even
        return res

    def test1(self):
        self.assertEqual(2, self.oddEvenJumps([10,13,12,14,15]))

    def test2(self):
        self.assertEqual(3, self.oddEvenJumps([2,3,1,1,4]))

    def test3(self):
        self.assertEqual(3, self.oddEvenJumps([5,1,3,4,2]))




