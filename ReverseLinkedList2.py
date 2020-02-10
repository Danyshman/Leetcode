def reverseBetween(head, m, n):
    if m == n or head.next is None:
        return head
    index = 1
    start_node = None
    sub_head = None
    prev = None
    node = head
    while node:
        if index == m:
            start_node = prev
            sub_head = node
        if n == index:
            if start_node:
                start_node.next = node
            else:
                head = node
            node.next = prev
            sub_head.next = node.next
            return head
        if index >= m:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
            index += 1
            continue
        prev = node
        node = node.next
        index += 1

