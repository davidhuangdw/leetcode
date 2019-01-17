from unittest import TestCase
# https://leetcode.com/problems/flatten-nested-list-iterator/

class NestedInteger(object):
    def __init__(self, val):
        self.val = val

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        return not isinstance(self.val, list)

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        return self.val

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        return self.val


class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = []
        self.stack.append((0, nestedList))
        self.cache = self.fetch()

    def fetch(self):
        """
        :rtype: int
        """
        s = self.stack
        while s:
            i, l = s.pop()
            if i >= len(l):
                continue
            s.append((i+1, l))
            if l[i].isInteger():
                return l[i].getInteger()
            s.append((0, l[i].getList()))
        return None

    def next(self):
        ret = self.cache
        self.cache = self.fetch()
        return ret

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.cache is not None


def flat(it):
    ret = []
    while it.hasNext():
        ret.append(it.next())
    return ret


def build(val):
    return NestedInteger(list(map(build, val)) if isinstance(val, list) else val)


class Tests(TestCase):

    def test1(self):
        it = NestedIterator(list(map(build, [[1,1],2,[1,1]])))
        self.assertEqual([1,1,2,1,1], flat(it))

    def test2(self):
        it = NestedIterator(list(map(build, [[1,[4,[6], [[]]]]])))
        self.assertEqual([1, 4, 6], flat(it))

