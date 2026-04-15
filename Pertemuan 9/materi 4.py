#=======================================================================
#nama : Muhammad Nabil Allatif
#NIM : J0403251128
#kelas : TPL B2
#latihan 1 : Membuat inorder traversal
#=======================================================================

#class node digunakan untuk dasar dari tree

from logging import root


class Node: 
    def __init__(self, data): 
        self.data = data    #menyimpan nilai node
        self.left = None    #child kiri
        self.right = None   #child kanan
        
#Membuat fungsi inorder : left > Root > right
def inorder(node):
    if node is not None:           #jika node tidak kosong
        inorder(node.left)        #mengunjungi child kiri
        print(node.data, end=" ") #menampilkan data node
        inorder(node.right)       #mengunjungi child kanan
        
#membuat Tree
root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.left.left = Node("D")
root.left.right = Node("E")

#menampilkan hasil inorder
print("Hasil Traversal Inorder : ", end="")
inorder(root)


#penjelasan :
#inorder adalah salah satu metode traversal pada tree yang mengunjungi node dalam urutan left
# > Root > right. Pada contoh di atas, hasil inorder akan menampilkan urutan node sebagai berikut: D B E A C
#1. Node adalah sebuah kelas yang digunakan untuk membuat struktur data pohon (tree).
#2. Fungsi inorder adalah salah satu metode traversal pada tree yang mengunjungi node dalam urutan left > Root > right. Pada contoh di atas, hasil inorder akan menampilkan urutan node sebagai berikut: D B E A C
#3. Traversal adalah proses mengunjungi setiap node dalam struktur data pohon (tree) dengan cara tertentu, seperti preorder, inorder, atau postorder. Traversal digunakan untuk mengakses dan memproses data dalam tree sesuai dengan urutan yang diinginkan.
