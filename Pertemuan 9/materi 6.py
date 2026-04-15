#=======================================================================
#nama : Muhammad Nabil Allatif
#NIM : J0403251128
#kelas : TPL B2
#materi 6 : struktur Organisasi Perusahaan
#=======================================================================

#class node digunakan untuk dasar dari tree

from logging import root


class Node: 
    def __init__(self, data): 
        self.data = data    #menyimpan nilai node
        self.left = None    #child kiri
        self.right = None   #child kanan
        
def preorder(node):
    if node is not None:           #jika node tidak kosong
        print(node.data, end=" ") #menampilkan data node
        preorder(node.left)       #mengunjungi child kiri
        preorder(node.right)      #mengunjungi child kanan
        
#Membuat tree struktur organisasi perusahaan
root = Node("Direktur")

#child level 1
root.left = Node("Manajer A")
root.right = Node("Manajer B")

#child level 2
root.left.left = Node("Staff1")
root.left.right = Node("Staff2")
root.right.right = Node("Staff3")

#menjalankan traversal preorder
print("struktur organisasi (preorder) : ")
preorder(root)

#penjelasan :
#1. Node adalah sebuah kelas yang digunakan untuk membuat struktur data pohon (tree).
#2. Fungsi preorder adalah salah satu metode traversal pada tree yang mengunjungi node dalam urutan Root > left > right. Pada contoh di atas, hasil preorder akan menampilkan urutan node sebagaiberikut: Direktur Manajer A Staff1 Staff2 Manajer B Staff3
#3. Traversal adalah proses mengunjungi setiap node dalam struktur data pohon (tree) dengan cara tertentu, seperti preorder, inorder, atau postorder. Traversal digunakan untuk mengakses dan memproses data dalam tree sesuai dengan urutan yang diinginkan.
