from unittest import TestCase
# https://leetcode.com/problems/peeking-iterator/


class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.fetch()

    def fetch(self):
        self.pk = [self.iterator.next()] if self.iterator.hasNext() else None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.pk[0] if self.pk else None

    def next(self):
        """
        :rtype: int
        """
        ret = self.pk[0]
        self.fetch()
        return ret


    def hasNext(self):
        """
        :rtype: bool
        """
        return self.pk is not None


