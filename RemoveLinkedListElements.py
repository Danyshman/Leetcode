# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int):
        while head and head.val == val:
            head = head.next
        prev=curr=head
        while curr:
            if curr.val == val:
                curr = curr.next
                prev.next = curr
            else:
                prev=curr
                curr=curr.next
        return head




