class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        checked = set()
        if head is None:
            return False
        node = head
        while node:
            if node in checked:
                return True
            else:
                checked.add(node)
                node = node.next
        return False
