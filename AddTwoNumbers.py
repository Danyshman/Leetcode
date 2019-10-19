class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None


def AddTwoNumbers(l1, l2):
    num1 = ''
    num2 = ''
    while l1 or l2:
        if l1:
            num1 = str(l1.val) + num1
            l1 = l1.next
        if l2:
            num2 = str(l2.val) + num2
            l2 = l2.next
    res = str(int(num1)+ int(num2))[::-1]
    temp = begin = ListNode(res[0])
    for i in range(1,len(res)):
        temp.next = ListNode(res[i])
        temp = temp.next
    return begin


l1 = ListNode(2)
l1a = ListNode(4)
l1.next = l1a
l1b = ListNode(3)
l1a.next = l1b


l2 = ListNode(5)
l2a = ListNode(6)
l2.next = l2a
l2b = ListNode(4)
l2a.next = l2b

ans = AddTwoNumbers(l1, l2)
print(ans.val)
print(ans.next.val)
print(ans.next.next.val)