# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not len(lists):
            return None
        head = ListNode(0)
        temp = head
        for i in range(len(lists)):
            if lists[i]:
                temp.next = lists[i]
                node = lists[i]
                while node and node.next:
                    node = node.next
                temp = node
        return self.merge_sort(head.next)
        
    def middle_node(self, head):
        if not head or not head.next:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        
    def merge(self, l1, l2):
        temp = ListNode(None)
        start = temp
            
        while l1 and l2:
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
                    
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        temp.next = l1 if l1 else l2
        return start.next
        
    def merge_sort(self, head):
        if not head or not head.next:
            return head
        middle_node = self.middle_node(head)
        second_half = middle_node.next
        middle_node.next = None
        return self.merge(self.merge_sort(head), self.merge_sort(second_half))
            
