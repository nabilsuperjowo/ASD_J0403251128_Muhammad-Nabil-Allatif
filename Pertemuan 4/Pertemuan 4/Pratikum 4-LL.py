#==============================================
#Nama    : Muhammad Nabil Allatif
#NIM     : J0403251128
#kelas   : TPL B2
#==============================================

#==============================================
#Implementasi Dasar : Node pada linked list
#==============================================

#membuat class Node (merupakan unit dasar dari linked list)
class Node:
    def __init__(self, data):     #konstruktor adalah sebuah metode khusus yang digunakan untuk menginisialisasi objek dari sebuah kelas. Dalam contoh di atas, konstruktor adalah metode __init__ yang digunakan untuk mengatur nilai awal dari atribut data dan next pada objek Node yang dibuat.
        self.data = data #menyimpan nilai/data      
        self.next = None #pointer ke note berikutnya    #instantiasi adalah proses pembuatan objek dari sebuah kelas. Dalam contoh di atas, ketika kita membuat objek Node dengan memberikan nilai data, konstruktor __init__ akan dipanggil secara otomatis untuk menginisialisasi atribut data dengan nilai yang diberikan dan mengatur next ke None. 
 
#1) membuat Node satu per satu 
nodeA = Node("A") #membuat objek Node dengan data "A" dan next diatur ke None
nodeB = Node("B") #membuat objek Node dengan data "B" dan next diatur ke None
nodeC = Node("C") #membuat objek Node dengan data "C" dan next diatur ke None

# 2) Menghubungkan Node : A -> B -> C -> None
nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = None

# 3) Menentukan Node pertama(head)
head = nodeA

# 4) Traversal : menelusuri dari head sampai none
current = head
while current is not None:
    print(current.data) #menampilkan data pada node saat ini
    current = current.next #pindah ke node berikutnya

#=========================================================
#Implementasi Dasar : Linked List + Insert Awal
#=========================================================

class linkedList:
    def __init__(self):
        self.head = None #awalnya kosong

    def insert_awal(self, data): # PUSH
        #1) buat node baru
        nodeBaru = Node(data) #panggil class node
        
        #2) node baru menunjuk ke head lama
        nodeBaru.next = self.head 
        
        #3) head pindah ke node baru
        self.head = nodeBaru
        
    def tampilkan(self): #impelentasi traversal
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next
    def hapus_awal(self): #pop dala stack
        data_terhapus = self.head.data
        #menggeser head ke node berikutnya
        self.head = self.head.next
        print("Data yang dihapus:", data_terhapus)
            
     
     
     
print("===List Baru===")
ll = linkedList() #instansiasi objek ke class linked list
ll.insert_awal("x")
ll.insert_awal("B")
ll.insert_awal("a")
ll.tampilkan()
ll.hapus_awal()
ll.tampilkan()
     
                