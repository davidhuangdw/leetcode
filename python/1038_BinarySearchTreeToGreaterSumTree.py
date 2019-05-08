from unittest import TestCase
# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree
from Definitions import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BinarySearchTreeToGreaterSumTree(TestCase):
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def subSum(node, gs):
            if not node: return 0
            rs = subSum(node.right, gs)
            s = subSum(node.left, node.val+rs+gs) + node.val + rs
            node.val += rs + gs
            return s
        subSum(root, 0)
        return root

    # # in-order iter
    # def bstToGst(self, root: TreeNode) -> TreeNode:
    #     pre, node, st = 0, root, []
    #     while node or st:
    #         if node:
    #             st.append(node)
    #             node = node.right
    #         else:
    #             p = st.pop()
    #             pre = p.val = p.val + pre
    #             node = p.left
    #     return root

    def test1(self):
        root = TreeNode.build_from_layerorder([4,1,6,0,2,5,7,None,None,None,3,None,None,None,8])

        self.assertEqual([30,36,21,36,35,26,15,None,None,None,33,None,None,None,8],
                         TreeNode.to_layerorder(self.bstToGst(root)))

