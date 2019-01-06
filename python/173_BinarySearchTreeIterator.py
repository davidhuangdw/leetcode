from unittest import TestCase
from Definitions import TreeNode
# https://leetcode.com/problems/binary-search-tree-iterator/


class BinarySearchTreeIterator:
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.middles = []
        self.parse(root)

    def parse(self, node):
        while node:
            self.middles.append(node)
            node = node.left

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        node = self.middles.pop()
        self.parse(node.right)
        return node.val

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return len(self.middles) > 0


class Tests(TestCase):
    def test1(self):
        root = TreeNode(7)
        root.left = TreeNode(3)
        root.right = TreeNode(15)
        root.right.left = TreeNode(9)
        root.right.right = TreeNode(20)

        iterator = BinarySearchTreeIterator(root)
        self.assertEqual(3, iterator.next())
        self.assertEqual(7, iterator.next())
        self.assertEqual(True, iterator.hasNext())
        self.assertEqual(9, iterator.next())
        self.assertEqual(15, iterator.next())
        self.assertEqual(20, iterator.next())
        self.assertEqual(False, iterator.hasNext())

