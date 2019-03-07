from unittest import TestCase
# https://leetcode.com/problems/clone-graph
import collections

"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class CloneGraph:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        root = Node(node.val, [])
        que, done = collections.deque([node]), {node: root}
        while que:
            node = que.popleft()
            copy = done[node]
            for ch in node.neighbors:
                if ch not in done:
                    done[ch] = Node(ch.val, [])
                    que.append(ch)
                copy.neighbors.append(done[ch])
        return root

