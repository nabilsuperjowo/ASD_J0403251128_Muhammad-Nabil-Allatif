class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head

    def display(self):
        if self.head is None:
            print("List Kosong")
            return
        
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(kembali ke head)")

    def search(self, key):
        if self.head is None:
            print("Circular Linked List kosong. Tidak ada elemen yang bisa dicari.")
            return

        temp = self.head
        found = False
        
        while True:
            if temp.data == key:
                found = True
                break
            temp = temp.next
            if temp == self.head:
                break
        
        if found:
            print(f"Elemen {key} ditemukan dalam Circular Linked List.")
        else:
            print(f"Elemen {key} tidak ditemukan dalam Circular Linked List.")
            
cll = CircularSinglyLinkedList()
input_data = input("Masukkan elemen untuk Circular Singly Linked List (pisahkan dengan spasi): ")
for data in input_data.split():
    cll.insert_at_end(int(data))
cll.display()
search_key = int(input("Masukkan elemen yang ingin dicari: "))
cll.search(search_key)