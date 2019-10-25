class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        if head is None:
            return []
        elif head.next is None:
            return [0]

        ans = []
        temp = []
        index = 0
        while head:
            ans.append(0)
            while len(temp) > 0 and temp[-1][1] < head.val:
                ans[temp.pop()[0]] = head.val
            temp.append((index, head.val))
            index += 1
            head = head.next
        return ans
