from unittest import TestCase
# https://leetcode.com/problems/validate-binary-search-tree
from Definitions import TreeNode


class ValidateBinarySearchTree(TestCase):
    def isValidBST(self, root: 'TreeNode') -> 'bool':
        def dfs(node, low, high):
            if not node: return True
            if not low < node.val < high: return False
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
        return dfs(root, float("-inf"), float("inf"))

    # # recursive by previous value
    # def isValidBST(self, root: 'TreeNode') -> 'bool':
    #     pre = float("-inf")
    #
    #     def dfs(node):
    #         nonlocal pre
    #         if not node: return True
    #         if not (dfs(node.left) and pre < node.val): return False
    #         pre = node.val
    #         return dfs(node.right)
    #     return dfs(root)


    # # by in-order using previous vlaue:
    # def isValidBST(self, root: 'TreeNode') -> 'bool':
    #     inorders, pre = [], float("-inf")
    #     while root or inorders:
    #         if root:
    #             inorders.append(root)
    #             root = root.left
    #         else:
    #             par = inorders.pop()
    #             if not pre < par.val: return False
    #             pre, root = par.val, par.right
    #     return True

    # # by in-order top-down using lower/higher bound:
    # def isValidBST(self, root: 'TreeNode') -> 'bool':
    #     cur, inorders, low, high = root, [], float("-inf"), float("inf")
    #     while cur or inorders:
    #         if cur:
    #             if not low < cur.val < high: return False
    #             inorders.append([cur, low, high])
    #             cur, high = cur.left, cur.val
    #         else:
    #             node, low, high = inorders.pop()
    #             low = node.val
    #             cur = node.right
    #     return True

    # # by post-order bottom-up:
    # def isValidBST(self, root: 'TreeNode') -> 'bool':
    #     cur, pars, last = root, [], None
    #     while cur or pars:
    #         if cur:
    #             pars.append([cur, cur.val, cur.val])
    #             cur = cur.left
    #         else:
    #             node, low, high = pars[-1]
    #             if node.right and last != node.right:
    #                 cur = node.right
    #             else:
    #                 pars.pop()
    #                 last = node
    #                 if not pars: break
    #                 p = pars[-1][0]
    #                 if not(high < p.val if node == p.left else p.val < low):
    #                     return False
    #                 if node == p.left:
    #                     pars[-1][1] = low
    #                 else:
    #                     pars[-1][2] = high
    #     return True

    def test1(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        self.assertEqual(True, self.isValidBST(root))

    def test2(self):
        root = TreeNode(5)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(6)
        self.assertEqual(False, self.isValidBST(root))

