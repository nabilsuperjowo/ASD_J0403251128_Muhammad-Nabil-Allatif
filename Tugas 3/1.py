class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None 

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def display_forward(self):
        print("\nTraversing forward:")
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    def display_backward(self):
        print("\nTraversing backward:")
        temp = self.tail
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.prev
        print("null")
        
    def delete_node(self, key):
        temp = self.head

        while temp and temp.data != key:
            temp = temp.next

        if temp is None:
            print("Data tidak ditemukan")
            return

        if temp == self.head:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None

        elif temp == self.tail:
            self.tail = temp.prev
            self.tail.next = None

        else:
            temp.prev.next = temp.next
            temp.next.prev = temp.prev

        temp = None

dll = DoublyLinkedList()
dll.insert_at_end(3)
dll.insert_at_end(5)
dll.insert_at_end(13)
dll.insert_at_end(2)

dll.display_forward()
dll.display_backward()

dll.delete_node(2)

dll.display_forward()
dll.display_backward()
