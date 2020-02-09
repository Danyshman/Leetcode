def getDecimalValue(head):
    if head is None:
        return -1
    str_num = ''
    node = head
    while node:
        str_num += node.val
        node = node.next
    return int(str_num, 2)


print(getDecimalValue('asd'))