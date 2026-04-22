# ==========================================================
# nama : Muhammad Nabil Allatif
# NIM : J0403251128
# kelas : TPL B2
# ==========================================================

# ==========================================================
# LATIHAN 5: Rotasi Kiri pada BST Tidak Seimbang
# ==========================================================


class Node:
    def __init__(self, data):
        self.data  = data
        self.left  = None
        self.right = None


# Preorder: Root → Kiri → Kanan
def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


# Tampilkan susunan tree dengan indentasi
def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None:
        print(" " * level + f"{posisi}: {root.data}")
        tampil_struktur(root.left,  level + 1, "L")
        tampil_struktur(root.right, level + 1, "R")


# Rotasi kiri: angkat child kanan (y) jadi root baru
def rotate_left(x):
    y  = x.right   # y = calon root baru
    T2 = y.left    # simpan subtree kiri y sementara

    y.left  = x    # x turun jadi anak kiri y
    x.right = T2   # bekas subtree kiri y dipasang ke kanan x

    return y        # y sekarang jadi root


# --- Program Utama ---

# Buat tree miring ke kanan secara langsung
root = Node(10)
root.right = Node(20)
root.right.right = Node(30)

print("Preorder sebelum rotasi:")
preorder(root)

print("\n\nStruktur sebelum rotasi:")
tampil_struktur(root)

# Lakukan rotasi kiri
root = rotate_left(root)

print("\nPreorder sesudah rotasi:")
preorder(root)

print("\n\nStruktur sesudah rotasi:")
tampil_struktur(root)

# Output:
# Preorder sebelum rotasi:
# 10 20 30
#
# Struktur sebelum rotasi:
# Root: 10
#  R: 20
#   R: 30
#
# Preorder sesudah rotasi:
# 20 10 30
#
# Struktur sesudah rotasi:
# Root: 20
#  L: 10
#  R: 30

# -----------------------------------------------------------
# KESIMPULAN
# -----------------------------------------------------------
# - Rotasi kiri mengangkat child kanan naik satu level jadi root baru.
# - Tree yang tadinya rantai lurus berubah jadi lebih seimbang.
# - Teknik ini jadi dasar algoritma penyeimbang otomatis seperti AVL.
# -----------------------------------------------------------