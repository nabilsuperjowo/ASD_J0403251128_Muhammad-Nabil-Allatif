#=======================================================================
#nama : Muhammad Nabil Allatif
#NIM : J0403251128
#kelas : TPL B2
#latihan 1 : Membuat Node
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
        
#menampilkan isi node
print("Data pada root : ", root.data)
print("Data child kiri root : ", root.left)
print("Data child kanan root : ", root.right)

#penjelasan
#Node adalah struktur data yang digunakan untuk menyimpan data dan memiliki referensi ke node lainnya.
#Node memiliki tiga atribut utama: data, left, dan right.
#data: menyimpan nilai atau informasi yang ingin disimpan dalam node.
#left: referensi ke node anak kiri (child kiri).
#right: referensi ke node anak kanan (child kanan).
#Pada contoh di atas, kita membuat sebuah node dengan nilai "A" dan menyimpannya
#dalam variabel root. Kemudian kita menampilkan isi node root, yang mencakup data pada node tersebut serta referensi ke child kiri dan child kanan, yang saat ini masih bernilai None karena belum ada node anak yang ditambahkan.
