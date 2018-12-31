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
