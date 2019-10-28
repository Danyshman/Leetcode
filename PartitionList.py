class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int):
        l1 = l1_head = ListNode(0)
        l2 = l2_head = ListNode(0)
        if head is None or head.next is None:
            return head
        node = head
        while node:
            if node.val < x:
                new_node = ListNode(node.val)
                l1.next = new_node
                l1 = new_node
            else:
                new_node = ListNode(node.val)
                l2.next = new_node
                l2 = new_node
            node = node.next
        l1.next = l2_head.next
        return l1_head.next
