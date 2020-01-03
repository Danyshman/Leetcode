class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode):
        node = head
        while node is not None and node.next is not None:
            temp = node.val
            node.val = node.next.val
            node.next.val = temp
            node = node.next.next
        return head
