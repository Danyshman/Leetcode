# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        st = []
        ans = [0] * len(arr)
        for i in range(len(arr)):
            while st and arr[i] > arr[st[-1]]:
                ans[st.pop()] = arr[i]
            st.append(i)
        return ans