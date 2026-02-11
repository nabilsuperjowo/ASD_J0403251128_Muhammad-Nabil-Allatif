class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def display(self):
        
        if self.head is None:
            print("kosong")
            return
        
        temp = self.head
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    def merge(self, other_list):
        if self.head is None:
            self.head = other_list.head
            self.tail = other_list.tail
        elif other_list.head is not None:
            self.tail.next = other_list.head
            self.tail = other_list.tail




list1 = SinglyLinkedList()
input1 = input("Masukkan elemen untuk Linked List 1 (pisahkan dengan spasi): ")
for data in input1.split():
    list1.insert_at_end(int(data))

list2 = SinglyLinkedList()
input2 = input("Masukkan elemen untuk Linked List 2 (pisahkan dengan spasi): ")
for data in input2.split():
    list2.insert_at_end(int(data))

print("\nLinked List 1:", end=" ")
list1.display()

print("Linked List 2:", end=" ")
list2.display()

list1.merge(list2)

print("Linked List setelah digabungkan:", end=" ")
list1.display()