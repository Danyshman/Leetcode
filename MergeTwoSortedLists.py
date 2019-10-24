class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode):
        head = ans = ListNode(0)
        node1 = l1
        node2 = l2
        while node1 or node2:
            if node1 == None:
                ans.next = node2
            elif node2 == None:
                ans.next = node1
            elif node1.val > node2.val:
                ans.next = ans = ListNode(node2.val)
                node2 = node2.next
            else:
                ans.next = ans = ListNode(node1.val)
                node1 = node1.next
        return head.next
