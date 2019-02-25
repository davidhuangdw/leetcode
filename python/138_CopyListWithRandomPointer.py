from unittest import TestCase
# https://leetcode.com/problems/copy-list-with-random-pointer


"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""

class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

    def asList(self):
        cur, lst = self, []
        while cur:
            lst.append((cur.val, cur.next and cur.next.val, cur.random and cur.random.val))
            cur = cur.next
        return lst


class CopyListWithRandomPointer(TestCase):
    def copyRandomList(self, head: 'Node') -> 'Node':
        # zip:
        src = head
        head = Node(0, src, None)
        while src:
            copy = Node(src.val, src.next, None)
            src.next = copy
            src = copy.next

        # random:
        src = head.next
        while src:
            src.next.random = src.random and src.random.next
            src = src.next.next

        # unzip:
        copy_tail = copy_head = Node(0, None, None)
        src = head.next
        while src:
            copy_tail.next = src.next   # append copy_node
            copy_tail = copy_tail.next
            src.next = src.next.next
            src = src.next
        return copy_head.next

    def test1(self):
        b = Node(2, None, None)
        b.random = b
        a = Node(1, b, b)
        self.assertEqual([(1,2,2,), (2, None, 2)], self.copyRandomList(a).asList())
        

