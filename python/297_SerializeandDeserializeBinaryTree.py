from unittest import TestCase
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
from Definitions import TreeNode

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
        arr = data.split(",")
        n = len(arr)

        i = 0
        def des():
            nonlocal i
            node = TreeNode(int(arr[i])) if i < n and arr[i] != 'n' else None
            i += 1
            if node:
                node.left = des()
                node.right = des()
            return node
        return des()

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



