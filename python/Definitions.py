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
