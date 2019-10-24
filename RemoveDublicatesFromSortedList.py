class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if (not head or head.next is None):
            return head
        node = head
        while node.next is not None:
            temp = node.next
            while (node.val == temp.val) and temp is not None:
                temp = temp.next
                if temp is None:
                    break
            node.next = node = temp
            if node is None:
                break
        return head