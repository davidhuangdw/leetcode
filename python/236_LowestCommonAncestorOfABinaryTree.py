from unittest import TestCase
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class LowestCommonAncestorOfABinaryTree(TestCase):
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = None

        def dfs(node, pre):
            nonlocal res
            if not node or pre >= 2: return 0
            cnt = int(node in (p, q))
            cnt += dfs(node.left, pre+cnt)
            cnt += dfs(node.right, pre+cnt)
            if cnt == 2 and not res:
                res = node
            return cnt
        dfs(root, 0)
        return res

    # # iterative: in-order
    # # 'lpar' is the latest node whose left partial subtree(include itself) has extractly 1 node
    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #     cur, inorders, found, lpar = root, [], 0, None
    #     while cur or inorders:
    #         if cur:
    #             inorders.append((cur, found))
    #             cur = cur.left
    #         else:
    #             node, pre = inorders.pop()
    #             found += node in (p, q)
    #             if found >= 1 and not pre:
    #                 lpar = node
    #             if found == 2: return lpar
    #             cur = node.right

    def test1(self):
        root = TreeNode(3)
        root.right = TreeNode(1)
        common = root.left = TreeNode(5)
        p = root.left.left = TreeNode(6)
        root.left.right = TreeNode(2)
        q = root.left.right.right = TreeNode(4)
        self.assertEqual(common, self.lowestCommonAncestor(root, p, q))

    def test2(self):
        root = TreeNode(3)
        common = p = root.right = TreeNode(1)
        root.right.left = TreeNode(0)
        q = root.right.right = TreeNode(8)
        root.left = TreeNode(5)
        self.assertEqual(common, self.lowestCommonAncestor(root, p, q))



