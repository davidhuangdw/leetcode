from unittest import TestCase
# https://leetcode.com/problems/min-stack/


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.mins = []
        self.values = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if len(self.mins) == 0 or x <= self.mins[-1]:
            self.mins.append(x)
        self.values.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.mins[-1] == self.values.pop():
            self.mins.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.values[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.mins[-1]


class Tests(TestCase):
    def test1(self):
        s = MinStack()
        s.push(-2)
        s.push(0)
        s.push(-3)
        self.assertEqual(-3, s.getMin())
        s.pop()
        self.assertEqual(0, s.top())
        self.assertEqual(-2, s.getMin())
