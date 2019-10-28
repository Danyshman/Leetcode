# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        node = root
        len_list = 0
        while node:
            len_list += 1
            node = node.next
        ans = []
        node = root
        if k >= len_list:
            while k > 0:
                if node is not None:
                    next_node = node.next
                    node.next = None
                    ans.append(node)
                    node = next_node
                    k -= 1
                else:
                    ans.append(None)
                    k -=1
            return ans
        else:
            part_size = len_list // k
            remainder = len_list % k
            print(part_size, remainder, ans)
            node = root
            index = 1
            for i in range(remainder):
                node1 = node
                for j in range(part_size+1):
                    print(node.val)
                    if index == part_size + 1:
                        next_node = node.next
                        node.next = None
                        ans.append(node1)
                        index = 1
                        node = next_node
                    else:
                        if node is None:
                            return ans
                        node = node.next
                        index += 1
            for i in range(k - remainder):
                node1 = node
                for j in range(part_size):
                    if node is None:
                        return ans
                    if index == part_size:
                        next_node = node.next
                        node.next = None
                        ans.append(node1)
                        index = 1
                        node = next_node
                    else:
                        if node is None:
                            return ans
                        node = node.next
                        index += 1
            return ans