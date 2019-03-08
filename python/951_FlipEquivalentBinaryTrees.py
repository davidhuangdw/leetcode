from unittest import TestCase
# https://leetcode.com/problems/flip-equivalent-binary-trees


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class FlipEquivalentBinaryTrees(TestCase):
    def flipEquiv(self, root1: 'TreeNode', root2: 'TreeNode') -> 'bool':
        return bool(root2) and root1.val == root2.val and \
               ((self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) or
                (self.flipEquiv(root1.right, root2.left) and self.flipEquiv(root1.left, root2.right))) \
            if root1 else not root2

    # # iterative: pre-order
    # def flipEquiv(self, root1: 'TreeNode', root2: 'TreeNode') -> 'bool':
    #     def eqVal(a, b):
    #         return b and a.val == b.val if a else not b
    #     preorder = [(root1, root2)]
    #     while preorder:
    #         a, b = preorder.pop()
    #         if not eqVal(a, b):
    #             return False
    #         if not a:
    #             continue
    #         if eqVal(a.left, b.left):
    #             preorder.append((a.left, b.left))
    #             preorder.append((a.right, b.right))
    #         elif eqVal(a.left, b.right):
    #             preorder.append((a.left, b.right))
    #             preorder.append((a.right, b.left))
    #         else:
    #             return False
    #     return True

    def test1(self):
        r1 = TreeNode(1)
        r1.left = TreeNode(2)
        r1.right = TreeNode(3)

        r2 = TreeNode(1)
        r2.left = TreeNode(3)
        r2.right = TreeNode(2)
        self.assertEqual(True, self.flipEquiv(r1, r2))

