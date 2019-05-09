from unittest import TestCase
# https://leetcode.com/problems/subtree-of-another-tree
from Definitions import TreeNode
import functools


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class SubtreeOfAnotherTree(TestCase):
    def isSubtree(self, s: 'TreeNode', t: 'TreeNode', exact=False) -> 'bool':
        if not t: return not exact or not s
        if not s: return False
        return (s.val == t.val and self.isSubtree(s.left, t.left, True) and self.isSubtree(s.right, t.right, True)) or \
               (not exact and (self.isSubtree(s.left, t) or self.isSubtree(s.right, t)))

    # # O(m+n) by compare 2 pre-orders, if using O(m+n) find_substring
    # def isSubtree(self, s: 'TreeNode', t: 'TreeNode') -> 'bool':
    #     ps, pt = self.preorder(s), self.preorder(t)
    #     # return pt in ps
    #     return self.kmp(ps, pt)
    #
    # def preorder(self, node):
    #     order, rem = [''], []
    #     while node or rem:
    #         if node:
    #             order.append(str(node.val))
    #             rem.append(node.right)
    #             node = node.left
    #         else:
    #             order.append('/')
    #             node = rem.pop()
    #     order.extend(['/', ''])
    #     return ".".join(order)
    #
    # def kmp(self, s, p):
    #     f, m = [-1], len(p)
    #     for i, c in enumerate(p):
    #         if i+1 >= m: break
    #         j = f[i]
    #         while j >= 0 and c != p[j]:
    #             j = f[j]
    #         f.append(j+1)
    #     # for i, j in enumerate(f):         # optimize
    #     #     if j >= 0 and p[j] == p[i]: f[i] = f[j]
    #     j = 0
    #     for c in s:
    #         while j >= 0 and p[j] != c:
    #             j = f[j]
    #         j += 1
    #         if j == m: return True
    #     return False

    def test1(self):
        s = TreeNode.build_from_layerorder([3, 4, 5, 1, 2])
        t = TreeNode.build_from_layerorder([4, 1, 2])
        self.assertEqual(True, self.isSubtree(s, t))

    def test2(self):
        s = TreeNode.build_from_layerorder([3, 4, 5, 1, 2, None, None, None, 0])
        t = TreeNode.build_from_layerorder([4, 1, 2])
        self.assertEqual(False, self.isSubtree(s, t))

    def test3(self):
        s = TreeNode.build_from_layerorder([2])
        t = TreeNode.build_from_layerorder([12])
        self.assertEqual(False, self.isSubtree(s, t))




        

