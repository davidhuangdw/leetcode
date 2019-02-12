from unittest import TestCase
# https://leetcode.com/problems/lfu-cache/


class Node:
    def __init__(self, key, value, freq=1):
        self.key = key
        self.value = value
        self.freq = freq
        self.prev = self.next = None

    def append(self, node):
        if self.next is not None:
            self.next.prev = node
        node.next = self.next
        node.prev = self
        self.next = node

    def remove(self):
        self.next.prev = self.prev
        self.prev.next = self.next


class LFUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.count = 0
        self.min = -1
        self.freq_map = dict()
        self.node_map = dict()

    def get_freq(self, freq):
        if freq not in self.freq_map:
            head = Node(-1, -1)
            tail = Node(-1, -1)
            head.append(tail)
            self.freq_map[freq] = (head, tail)
        return self.freq_map[freq]

    def remove_node(self, node):
        node.remove()
        del self.node_map[node.key]
        head, tail = self.get_freq(node.freq)
        if head.next == tail and self.min == node.freq:
            self.min += 1
        self.count -= 1

    def insert_node(self, node):
        head, tail = self.get_freq(node.freq)
        head.append(node)
        self.node_map[node.key] = node
        self.count += 1

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.node_map:
            return -1
        node = self.node_map[key]
        self.remove_node(node)

        node.freq += 1
        self.insert_node(node)
        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.capacity == 0:
            return
        if key in self.node_map:
            self.node_map[key].value = value
            return self.get(key)

        if self.count == self.capacity:
            head, tail = self.get_freq(self.min)
            self.remove_node(tail.prev)

        node = Node(key, value, 1)
        self.insert_node(node)
        self.min = 1


class Tests(TestCase):
    def test1(self):
        cache = LFUCache(0)
        cache.put(1, 1)
        self.assertEqual(-1, cache.get(1))

    def test2(self):
        cache = LFUCache(3)
        cache.put(2, 2)
        cache.put(1, 1)
        self.assertEqual(2, cache.get(2))
        self.assertEqual(1, cache.get(1))
        self.assertEqual(2, cache.get(2))
        cache.put(3, 3)
        cache.put(4, 4)
        self.assertEqual(-1, cache.get(3))
        self.assertEqual(2, cache.get(2))
        self.assertEqual(1, cache.get(1))
        self.assertEqual(4, cache.get(4))
        cache.put(2, 9)
        self.assertEqual(9, cache.get(2))
