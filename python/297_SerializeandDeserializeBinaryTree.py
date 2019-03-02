from unittest import TestCase
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
from Definitions import TreeNode
import collections

def preorder(node):
    return [node.val] + preorder(node.left) + preorder(node.right) if node else []


class SerializeandDeserializeBinaryTree(TestCase):
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        ret = []
        def ser(node):
            if node:
                ret.append(str(node.val))
                ser(node.left)
                ser(node.right)
            else:
                ret.append('n')
        ser(root)
        return ",".join(ret)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def dec(s):
            return None if s == 'n' else TreeNode(int(s))
        it = iter(data.split(","))

        def des():
            node = dec(next(it))
            if node:
                node.left = des()
                node.right = des()
            return node
        return des()

    # # iterative DFS:
    # def serialize(self, root):
    #     res, rights = [], []
    #     cur = root
    #     while cur or rights:
    #         if cur:
    #             res.append(str(cur.val))
    #             rights.append(cur.right)
    #             cur = cur.left
    #         else:
    #             res.append('n')
    #             cur = rights.pop()
    #     return ",".join(res + ['n'])
    #
    # def deserialize(self, data):
    #     def dec(s):
    #         return None if s == 'n' else TreeNode(int(s))
    #     it = iter(data.split(','))
    #     root = node = dec(next(it))
    #     n, i, rights = len(data), 1, []
    #     while node or rights:
    #         if node:
    #             rights.append(node)
    #             node.left = dec(next(it))
    #             node = node.left
    #         else:
    #             node = rights.pop()
    #             node.right = dec(next(it))
    #             node = node.right
    #     return root

    # # iterative BFS:
    # def serialize(self, root):
    #     que, res = collections.deque([root]), []
    #     while que:
    #         node = que.popleft()
    #         if node:
    #             res.append(str(node.val))
    #             que.append(node.left)
    #             que.append(node.right)
    #         else:
    #             res.append('n')
    #     return ",".join(res)
    #
    # def deserialize(self, data):
    #     def dec(s):
    #         return None if s == 'n' else TreeNode(int(s))
    #     it, que = iter(data.split(",")), collections.deque()
    #     root = dec(next(it))
    #     if root:
    #         que.append(root)
    #     while que:
    #         node = que.popleft()
    #         node.left = dec(next(it))
    #         node.right = dec(next(it))
    #         if node.left:
    #             que.append(node.left)
    #         if node.right:
    #             que.append(node.right)
    #     return root

    def test1(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.right.left = TreeNode(4)
        root.right.left = TreeNode(5)
        self.assertEqual(preorder(root), preorder(self.deserialize(self.serialize(root))))

    def test2(self):
        root = None
        self.assertEqual(None, self.deserialize(self.serialize(root)))



