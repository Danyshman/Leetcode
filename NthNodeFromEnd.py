def nth_from_end(head, n):
    length = 0
    node = head
    while node:
        node = node.next
        length += 1
    if n > length:
        return None
    for i in range(length-n):
        node = node.next
    return node.val
