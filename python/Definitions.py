import collections

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def as_list(self):
        ret = []
        node = self
        while node:
            ret.append(node.val)
            node = node.next
        return ret


    @staticmethod
    def build_from_list(*values):
        head = ListNode(0)
        for v in reversed(values):
            node = ListNode(v)
            node.next = head.next
            head.next = node
        return head.next


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    @staticmethod
    def from_array_list(*array_list):
        return list(map(lambda arr: Interval(*arr), array_list))

    @staticmethod
    def to_array_list(*interval_list):
        return list(map(lambda i: [i.start, i.end], interval_list))


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @staticmethod
    def build_from_layerorder(order):
        if not order: return None
        i, n, root = 1, len(order), TreeNode(order[0])
        que = collections.deque([root])
        while i < n:
            par = que.popleft()
            if order[i] is not None:
                par.left = l = TreeNode(order[i])
                que.append(l)
            if i+1 < n and order[i+1] is not None:
                par.right = r = TreeNode(order[i+1])
                que.append(r)
            i += 2
        return root

    @staticmethod
    def build_from_preorder(preorder):
        if not preorder: return None
        n = len(preorder)

        def dfs(i):
            if i >= n or preorder[i] is None: return None, i+1
            node = TreeNode(preorder[i])
            l, j = dfs(i+1)
            r, j = dfs(j)
            node.left = l
            node.right = r
            return node, j
        return dfs(0)[0]

