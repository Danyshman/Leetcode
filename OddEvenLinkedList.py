class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head: ListNode):
        if head is None or head.next is None or head.next.next is None:
            return head
        even = head.next
        odd_head = head
        even_head = even
        while even_head.next and even_head:
            odd_head.next = odd_head.next.next
            odd_head = odd_head.next
            even.next = even.next.next
            even = even.next
        odd_head.next = even_head
        return head


