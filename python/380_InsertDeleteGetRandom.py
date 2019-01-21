from unittest import TestCase
# https://leetcode.com/problems/insert-delete-getrandom-o1/
import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.values = []
        self.index = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if self.index.get(val) is not None:
            return False
        self.index[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if self.index.get(val) is None:
            return False
        i = self.index.pop(val)
        last = self.values.pop()
        if val != last:
            self.index[last] = i
            self.values[i] = last
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.values)


class Tests(TestCase):
    def test1(self):
        randomSet = RandomizedSet()
        self.assertTrue(randomSet.insert(1))
        self.assertFalse(randomSet.remove(2))
        self.assertTrue(randomSet.insert(2))
        self.assertIn(randomSet.getRandom(), [1,2])
        self.assertTrue(randomSet.remove(1))
        self.assertFalse(randomSet.insert(2))
        self.assertIn(randomSet.getRandom(), [2])
        self.assertIn(randomSet.getRandom(), [2])
