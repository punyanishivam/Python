# Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_elements(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp is not None:
            temp = temp.next
            temp.next = new_node

    def insert_after_item(self, data, key):
        new_node = Node(data)
        temp = self.head
        while temp is not None:
            if temp.next == key:
                break
            temp = temp.next
            if temp is None:
                print("Element not found")
            else:
                new_node.next = temp.next
                temp.next = new_node


ll = LinkedList()
node1 = Node(5)
node2 = Node(7)
node3 = Node(9)

ll.head = node1
node1.next = node2
node2.next = node3

ll.printElements()
