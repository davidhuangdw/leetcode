from unittest import TestCase
from Definitions import TreeNode
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/


class KthSmallestElementBST(TestCase):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def kth(node, m):
            if not node:
                return None, 0
            x, l = kth(node.left, m)
            if x is not None:
                return x, -1
            if l+1 == m:
                return node.val, -1
            x, r = kth(node.right, m-(l+1))
            return x, r+(l+1)
        return kth(root, k)[0]

    def test1(self):
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.left.right = TreeNode(2)
        root.right = TreeNode(4)
        self.assertEqual(1, self.kthSmallest(root, 1))

    def test2(self):
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.left.left = TreeNode(2)
        root.left.left.left = TreeNode(1)
        root.left.right = TreeNode(4)
        root.right = TreeNode(6)
        self.assertEqual(3, self.kthSmallest(root, 3))
