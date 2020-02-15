"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        list_dict = dict()
        node = head
        while node:
            list_dict[node] = Node(node.val)
            node = node.next
        node = head
        while node:
            if node.next != None:
                list_dict[node].next = list_dict[node.next]
            if node.random != None:
                list_dict[node].random = list_dict[node.random]
            node = node.next
        return list_dict[head]