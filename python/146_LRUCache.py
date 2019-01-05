from unittest import TestCase
# https://leetcode.com/problems/lru-cache/


class Node:
    def __init__(self, key=None, value=None, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

    def remove(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
        self.prev = self.next = None
        return self

    def insert(self, node):
        node.next = self.next
        node.prev = self
        if self.next:
            self.next.prev = node
        self.next = node
        return node


class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.count = 0
        self.hash = {}
        self.head = Node()
        self.tail = Node()
        self.head.insert(self.tail)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self.hash.get(key)
        if node:
            self.move_to_head(node)
            return node.value
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        node = self.hash.get(key)
        if node:
            node.value = value
        else:
            self.hash[key] = self.head.insert(Node(key, value))
            self.count += 1
            if self.count > self.capacity:
                self.pop()
        self.get(key)

    def last(self):
        return self.tail.prev if self.count > 0 else None

    def pop(self):
        if self.count > 0:
            node = self.last()
            del self.hash[node.key]
            node.remove()
            self.count -= 1
            return node
        else:
            return None

    def move_to_head(self, node):
        if self.head.next != node:
            node.remove()
            self.head.insert(node)
        return node


# test:
def to_list(cache):
    list = []
    node = cache.head.next
    while node:
        list.append(node.value)
        node = node.next
    return list[:-1]    # remove tail


class RunTest(TestCase):
    def test1(self):
        c = LRUCache(2)
        c.put(1, 100)
        c.put(2, 200)
        self.assertEqual([200, 100], to_list(c))
        self.assertEqual(100, c.get(1))
        self.assertEqual([100, 200], to_list(c))
        c.put(3, 300)
        self.assertEqual([300, 100], to_list(c))
        c.put(3, 200)
        self.assertEqual([200, 100], to_list(c))
        c.put(3, 300)
        self.assertEqual([300, 100], to_list(c))
        c.put(4, 400)
        self.assertEqual([400, 300], to_list(c))
        self.assertEqual(-1, c.get(1))
        self.assertEqual(300, c.get(3))
        self.assertEqual(400, c.get(4))
