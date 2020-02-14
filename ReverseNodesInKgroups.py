# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k == 1:
            return head
        length = 0
        node = head
        while node:
            node = node.next
            length += 1
        if k > length:
            return head
        dummy = curr_end = ListNode(0)
        node = start = head
        count = 1
        while node:
            if count < k:
                node = node.next
                count += 1
            elif k == count:
                right = node.next
                node.next = None
                r_head, r_tail = self.reverse(start)
                curr_end.next = r_head
                curr_end = r_tail
                curr_end.next = right
                node = right
                start = right
                count = 1
        return dummy.next

    def reverse(self, head):
        if not head or not head.next:
            return head
        prev = None
        curr = head
        while curr.next:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        curr.next = prev
        return curr, head
            
        
