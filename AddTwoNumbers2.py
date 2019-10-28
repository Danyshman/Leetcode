class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        if l1 is None and l2 is None:
            return None
        elif l1 is None:
            return l2
        elif l2 is None:
            return l1
        first_num = ''
        second_num = ''
        while l1 or l2:
            if l1 is not None:
                first_num += str(l1.val)
                l1 = l1.next
            if l2 is not None:
                second_num += str(l2.val)
                l2 = l2.next
        third_num = str(int(first_num) + int(second_num))
        res_node = head = ListNode(0)
        for i in third_num:
            new_node = ListNode(int(i))
            res_node.next = new_node
            res_node = new_node
        return head.next
