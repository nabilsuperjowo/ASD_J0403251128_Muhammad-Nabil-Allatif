# ==========================================================
# nama : Muhammad Nabil Allatif
# NIM : J0403251128
# kelas : TPL B2
# ==========================================================

# ==========================================================
# LATIHAN 6: Rotasi Kanan pada BST Tidak Seimbang
# ==========================================================

class Node:
    def __init__(self, data):
        self.data  = data
        self.left  = None
        self.right = None

# Tampilkan susunan tree dengan indentasi
def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None:
        print(" " * level + f"{posisi}: {root.data}")
        tampil_struktur(root.left,  level + 1, "L")
        tampil_struktur(root.right, level + 1, "R")

# Rotasi kanan: angkat child kiri (y) jadi root baru
def rotate_right(x):
    y  = x.left    # y = calon root baru
    T2 = y.right   # simpan subtree kanan y sementara

    y.right = x    # x turun jadi anak kanan y
    x.left  = T2   # bekas subtree kanan y dipasang ke kiri x

    return y        # y sekarang jadi root

# --- Program Utama ---

# Buat tree miring ke kiri secara langsung
root = Node(30)
root.left = Node(20)
root.left.left = Node(10)


print("\n\nStruktur sebelum rotasi:")
tampil_struktur(root)

# Lakukan rotasi kanan
root = rotate_right(root)

print("\n\nStruktur sesudah rotasi:")
tampil_struktur(root)

# Output:
# Struktur sebelum rotasi:
# Root: 30
#  L: 20
#   L: 10
#
# Struktur sesudah rotasi:
# Root: 20
#  L: 10
#  R: 30

# -----------------------------------------------------------
# KESIMPULAN
# -----------------------------------------------------------
# - Rotasi kanan kebalikan dari rotasi kiri.
# - Child kiri naik satu level jadi root baru.
# - Tree yang condong ke kiri berubah jadi seimbang.
# - Langkah dasarnya sama dengan AVL Tree saat mendeteksi
#   ketidakseimbangan di sisi kiri.
# -----------------------------------------------------------