class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        checked = set()
        node1 = headA
        node2 = headB
        if node1 is None or node2 is None:
            return None
        while node1 or node2:
            if node1 is not None:
                if node1 in checked:
                    return node1
                else:
                    checked.add(node1)
                    node1 = node1.next
            if node2 is not None:
                if node2 in checked:
                    return node2
                else:
                    checked.add(node2)
                    node2 = node2.next
        return None