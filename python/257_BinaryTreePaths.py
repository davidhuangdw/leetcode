from unittest import TestCase
from Definitions import TreeNode
# https://leetcode.com/problems/binary-tree-paths/


class BinaryTreePaths(TestCase):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        ret = []

        def dfs(node, path):
            if not node: return
            path = path + [node.val]
            if node.left is None and node.right is None:
                ret.append("->".join(map(str, path)))
            dfs(node.left, path)
            dfs(node.right, path)
        dfs(root, [])
        return ret

    def test1(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.right = TreeNode(5)
        root.right = TreeNode(3)
        self.assertEqual(["1->2->5", "1->3"], self.binaryTreePaths(root))
