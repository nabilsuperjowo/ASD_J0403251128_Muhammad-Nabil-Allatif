#=======================================================================
#nama : Muhammad Nabil Allatif
#NIM : J0403251128
#kelas : TPL B2
#latihan 1 : Membuat binary search tree
#=======================================================================

#class node digunakan untuk dasar dari tree

from logging import root


class Node: 
    def __init__(self, data): 
        self.data = data    #menyimpan nilai node
        self.left = None    #child kiri
        self.right = None   #child kanan
        
#membuat root
root = Node("A")
        
#membuat child level 1
root.left = Node("B")
root.right = Node("C")

#membuat child level 2
root.left.left = Node("D")

#menampilkan isi node
print("Data pada root : ", root.data)
print("Data child kiri root : ", root.left.data)
print("Data child kanan root : ", root.right.data)
print("Data child kiri dari B : ", root.left.left.data)
print("Data child kanan dari B : ", root.left.right.data)

#membuat child level 3
root.left.left.left = Node("E")
root.left.left.right = Node("F")

#membuat child level 4
root.left.left.left.left = Node("G")

#menampilkan isi node
print("Data pada root : ", root.data)
print("Data child kiri root : ", root.left.data)
print("Data child kanan root : ", root.right.data)
print("Data child kiri dari B : ", root.left.left.data)
print("Data child kanan dari B : ", root.left.right.data)
print("Data child kiri dari D : ", root.left.left.left.data)
print("Data child kanan dari D : ", root.left.left.right.data)
print("Data child kiri dari E : ", root.left.left.left.left.data)
print("Data child kanan dari E : ", root.left.left.left.right.data)
print("Data child kiri dari F : ", root.left.left.right.left.data)
print("Data child kanan dari F : ", root.left.left.right.right.data)
print("Data child kiri dari G : ", root.right.left.data)
print("Data child kanan dari G : ", root.right.right.data)



#penjelasan :
#1. Node adalah sebuah kelas yang digunakan untuk membuat struktur data pohon (tree).
#2. Setiap node memiliki atribut data yang menyimpan nilai node, serta atribut left dan right yang menyimpan referensi ke child kiri dan child kanan dari node tersebut.
#3. Dalam contoh di atas, kita membuat sebuah pohon dengan root node "A",
#   - Node "A" memiliki child kiri "B" dan child kanan "C".
#   - Node "B" memiliki child kiri "D" dan tidak memiliki child kanan.
#   - Node "D" memiliki child kiri "E" dan child kanan "F".
#   - Node "E" memiliki child kiri "G" dan tidak memiliki child kanan.
#4. Kita kemudian menampilkan isi dari setiap node dalam pohon, termasuk data pada node tersebut serta referensi ke child kiri dan child kanan, yang dapat bernilai None jika tidak ada child yang ditambahkan.
