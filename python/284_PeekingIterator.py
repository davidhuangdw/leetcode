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
        self.prefetch = self.iterator.next() if self.iterator.hasNext() else None
        # self.pk = [self.iterator.next()] if self.iterator.hasNext() else None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.prefetch if self.prefetch else None

    def next(self):
        """
        :rtype: int
        """
        ret = self.prefetch
        self.fetch()
        return ret

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.prefetch is not None


