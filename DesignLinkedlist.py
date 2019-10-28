class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        node = self.head
        indexes = 0
        while node:
            if indexes == index:
                return node.val
            else:
                indexes += 1
                node = node.next
        return - 1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        temp = self.head
        new_node = Node(val)
        self.head = new_node
        new_node.next = temp

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = self.head
        while node.next:
            node = node.next
        new_node = Node(val)
        node.next = new_node


    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index <= 0:
            self.addAtHead(val)
            return
        node = self.head
        i = 0
        prev = self.head
        while node:
            if i == index:
                new_node = Node(val)
                prev.next = new_node
                new_node.next = node
                return
            else:
                prev = node
                node = node.next
                i += 1
        if i == index:
            new_node = Node(val)
            prev.next = new_node


    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if self.head is not None and index == 0:
            self.head = self.head.next
            return
        elif self.head is None and index == 0:
            return
        i = 0
        node = self.head
        prev = self.head
        while node:
            if index == i:
                prev.next = node.next
                break
            else:
                prev = node
                node = node.next
                i += 1
    def printList(self):
        node = self.head
        result = ''
        while node:
            result += str(node.val)
            node = node.next
        print(result)



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
obj = MyLinkedList()
obj.addAtIndex(0,1)
print(obj.get(0))
print(obj.get(1))
# obj.printList()
