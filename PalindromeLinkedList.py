# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True
        if head.next.next is None and head.val != head.next.val:
            return False
        elif head.next.next is None and head.val == head.next.val:
            return True
        length = 0
        node = head
        while node:
            node = node.next
            length += 1
        if length % 2 != 0:
            node = head
            left_part = node
            for i in range(length // 2 - 1):
                node = node.next
            right_part = node.next.next
            node.next = None
            return self.check_palindrome(left_part, self.reverse(right_part))

        else:
            node = head
            left_part = node
            for i in range(length // 2 - 1):
                node = node.next
            right_part = node.next
            node.next = None
            return self.check_palindrome(left_part, self.reverse(right_part))

    def check_palindrome(self, left, right):
        while left and right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

    def reverse(self, head):
        if head is None or head.next is None:
            return head
        prev = None
        cur = head
        next = head.next
        while next:
            cur.next = prev
            prev = cur
            cur = next
            next = next.next
        cur.next = prev
        head = cur
        return head


