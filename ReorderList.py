class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        if head is None or head.next is None:
            return
        arr = []
        node = head
        while node:
            arr.append(node.val)
            node = node.next
        start, end = 0, len(arr)-1
        node = head
        index = 1
        while start <= end:
            if start == end:
                node.val = arr[start]
                break
            elif index % 2 == 1:
                node.val = arr[start]
                start += 1
                node = node.next
                index += 1
            elif index % 2 == 0:
                node.val = arr[end]
                end -= 1
                node = node.next
                index += 1


