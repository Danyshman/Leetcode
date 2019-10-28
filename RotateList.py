class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int):
        if head is None or head.next is None:
            return head
        node = head
        arr = []
        while node:
            arr.append(node.val)
            node = node.next
        while k >= len(arr):
            k -= (k//len(arr))*len(arr)
        for i in range(k):
            arr.insert(0, arr[-1])
            arr = arr[:-1]
        node = head
        i = 0
        while node:
            node.val = arr[i]
            i += 1
        return head
