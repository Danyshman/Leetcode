def detectLoop(head):
    slow = head
    fast = head
    while slow and fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next
    return False