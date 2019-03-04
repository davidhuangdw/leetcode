from unittest import TestCase
# https://leetcode.com/problems/longest-univalue-path
from Definitions import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class LongestUnivaluePath(TestCase):
    def longestUnivaluePath(self, root: 'TreeNode') -> 'int':
        mx = 0

        def dfs(node):
            nonlocal mx
            if not node: return 0
            l, r, res = dfs(node.left), dfs(node.right), 0
            l = l+1 if node.left and node.left.val == node.val else 0
            r = r+1 if node.right and node.right.val == node.val else 0
            mx = max(mx, l+r)
            return max(l, r)
        dfs(root)
        return mx

    # # post-order iterative:
    # def longestUnivaluePath(self, root: 'TreeNode') -> 'int':
    #     cur, pars, last_pop, res = root, [], None, 0
    #     while cur or pars:
    #         if cur:
    #             pars.append([cur, 0, 0])
    #             cur = cur.left
    #         else:
    #             p, l, r = pars[-1]
    #             if not p.right or last_pop == p.right:
    #                 pars.pop()
    #                 res, last_pop = max(res, l+r), p
    #                 pp = pars and pars[-1][0]
    #                 if pp and pp.val == p.val:          # let child update parent
    #                     i = 1 if p == pp.left else 2
    #                     pars[-1][i] = 1 + max(l, r)
    #             else:
    #                 cur = p.right
    #     return res

    def test1(self):
        r = TreeNode(5)
        r.left = TreeNode(4)
        r.left.left = TreeNode(4)
        r.left.right = TreeNode(4)
        r.right = TreeNode(5)
        r.right.right = TreeNode(1)
        self.assertEqual(2, self.longestUnivaluePath(r))


        

