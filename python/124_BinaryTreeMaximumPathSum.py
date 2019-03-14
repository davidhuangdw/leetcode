from unittest import TestCase
# https://leetcode.com/problems/binary-tree-maximum-path-sum
from Definitions import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BinaryTreeMaximumPathSum(TestCase):
    def maxPathSum(self, root: 'TreeNode') -> 'int':
        res = MIN = float("-inf")

        def dfs(node):
            nonlocal res
            if not node: return MIN
            l, r, v = dfs(node.left), dfs(node.right), node.val
            res = max(res, v + max(0, l) + max(0, r))
            return node.val + max(0, l, r)
        dfs(root)
        return res

    def test1(self):
        root = TreeNode.build_from_preorder([1,2,3])
        self.assertEqual(6, self.maxPathSum(root))

    def test2(self):
        root = TreeNode.build_from_layerorder([-10,9,20,None,None,15,7])
        self.assertEqual(42, self.maxPathSum(root))


        

