# ==========================================================
# nama : Muhammad Nabil Allatif
# NIM : J0403251128
# kelas : TPL B2
# ==========================================================


# ==========================================================
# LATIHAN 4: BST Tidak Seimbang
# ==========================================================



# Node penyimpan data BST
class Node:
    def __init__(self, data):
        self.data  = data
        self.left  = None   # cabang kiri
        self.right = None   # cabang kanan


# Insert biasa — tidak ada penyeimbangan otomatis
def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)

    return root


# Preorder: cetak Root dulu, baru kiri, lalu kanan
def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


# Tampilkan bentuk visual tree (indentasi = kedalaman)
def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None:
        print(" " * level + f"{posisi}: {root.data}")
        tampil_struktur(root.left,  level + 1, "L")
        tampil_struktur(root.right, level + 1, "R")


# --- Program Utama ---
root = None
data_list = [10, 20, 30]   # urut naik → tree pasti miring ke kanan

for data in data_list:
    root = insert(root, data)

print("Preorder BST:")
preorder(root)

print("\n\nStruktur BST:")
tampil_struktur(root)

# Output:
# Preorder BST:
# 10 20 30
#
# Struktur BST:
# Root: 10
#  R: 20
#   R: 30

# -----------------------------------------------------------
# KESIMPULAN
# -----------------------------------------------------------
# - Tree miring ke kanan karena data masuk urut dari kecil ke besar.
# - Pencarian jadi lambat (O(n)) — mirip cari data satu per satu.
# - BST tidak otomatis seimbang, perlu algoritma khusus (misal AVL).
# -----------------------------------------------------------