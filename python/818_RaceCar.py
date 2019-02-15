from unittest import TestCase
# https://leetcode.com/problems/race-car/


class RaceCar(TestCase):
    def racecar(self, target: 'int') -> 'int':
        cache = dict()

        def cal(k):
            return (1 << k) - 1

        def dp(v):
            if v not in cache:
                i = 1
                while cal(i) < v:
                    i += 1
                if cal(i) == v:
                    cache[v] = i
                else:
                    m = dp(cal(i) - v)
                    for j in range(i-1):
                        m = min(m, j + dp(v-cal(i-1)+cal(j)))
                    cache[v] = i + 1 + m
            return cache[v]
        return dp(target)

    def test1(self):
        self.assertEqual(2, self.racecar(3))

    def test2(self):
        self.assertEqual(5, self.racecar(6))

    def test3(self):
        self.assertEqual(28, self.racecar(943))

