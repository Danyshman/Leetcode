def copyRandomList(head):
    original_dict = dict()
    new_arr = []
    index = 0
    node = head
    dummy = temp = Node(5)
    while node:
        temp.next = Node(node.val)
        temp = temp.next
        original_dict[index] = node
        next_node = node.next
        node.val = index
        node = next_node
        index += 1
    node = dummy.next
    while node:
        new_arr.append(node)
        node = node.next
    for key, value in original_dict.items():
        if original_dict[key].random:
            new_arr[key].random = new_arr[original_dict[key].random.val]
        else:
            new_arr[key].random = None
    node = head
    for i in range(len(new_arr)):
        node.val = new_arr[i].val
        node = node.next
    return new_arr[0]
