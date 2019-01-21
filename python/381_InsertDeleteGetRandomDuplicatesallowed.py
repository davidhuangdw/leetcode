from unittest import TestCase
# https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/
import collections, random


class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.indexes = collections.defaultdict(set)
        self.values = []

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        ret = len(self.indexes[val]) == 0
        self.indexes[val].add(len(self.values))
        self.values.append(val)
        return ret

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if not self.indexes[val]:
            return False
        last = self.values.pop()
        self.indexes[last].remove(len(self.values))
        if last != val:
            i = self.indexes[val].pop()
            self.values[i] = last
            self.indexes[last].add(i)
        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return random.choice(self.values)


class Tests(TestCase):
    def test1(self):
        collection = RandomizedCollection()
        self.assertTrue(collection.insert(1))
        self.assertFalse(collection.insert(1))
        self.assertTrue(collection.insert(2))
        self.assertIn(collection.getRandom(), [1, 2])
        self.assertIn(collection.getRandom(), [1, 2])
        self.assertFalse(collection.remove(9))
        self.assertTrue(collection.remove(1))
        self.assertTrue(collection.remove(2))
        self.assertIn(collection.getRandom(), [1])

