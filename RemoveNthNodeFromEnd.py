# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head or not head.next:
            return None
        list_dict = dict()
        index = 1
        node = head
        while node:
            list_dict[index] = node
            node = node.next
            index += 1
        index -= 1
        if index-n < 1:
            return head.next
        list_dict[index-n].next = list_dict[index-n+1].next
        return head
