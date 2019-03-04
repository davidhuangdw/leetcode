from unittest import TestCase
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii
import collections


class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class PopulatingNextRightPointersInEachNodeIi(TestCase):
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        que = collections.deque([(root, 0)])
        while que:
            node, h = que.popleft()
            if que and que[0][1] == h:
                que[0][0].next = node
            if node.right: que.append((node.right, h+1))
            if node.left: que.append((node.left, h+1))
        return root

    # # iterative O(1) space:
    # def connect(self, root: 'Node') -> 'Node':
    #     parent_head, dummy = root, Node(0, None, None, None)
    #     while parent_head:
    #         dummy.next = None   # dummy head for children layer
    #         parent, tail = parent_head, dummy
    #         while parent:
    #             for ch in (parent.left, parent.right):
    #                 if ch:
    #                     tail.next = ch
    #                     tail = tail.next
    #             parent = parent.next
    #         parent_head = dummy.next
    #     return root

    def test1(self):
        nodes = {}
        for v in range(1, 8):
            nodes[v] = Node(v, None, None, None)
        nodes[1].left = nodes[2]
        nodes[1].right = nodes[3]
        nodes[2].left = nodes[4]
        nodes[2].right = nodes[5]
        nodes[3].right = nodes[7]
        self.connect(nodes[1])
        self.assertEqual(None, nodes[1].next)
        self.assertEqual(nodes[3], nodes[2].next)
        self.assertEqual(None, nodes[3].next)
        self.assertEqual(nodes[5], nodes[4].next)
        self.assertEqual(nodes[7], nodes[5].next)
        self.assertEqual(None, nodes[7].next)


