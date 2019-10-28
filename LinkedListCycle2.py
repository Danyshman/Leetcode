class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode):
        if head is None or head.next is None:
            return None
        d = dict()
        node = head
        while node:
            if 0 == d.get(node, 0):
                d[node] = node
                node = node.next
            else:
                return d[node]


