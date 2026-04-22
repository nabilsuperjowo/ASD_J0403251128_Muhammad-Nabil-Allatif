# ==========================================================
# nama : Muhammad Nabil Allatif
# NIM : J0403251128
# kelas : TPL B2
# Judul   : Latihan 1-3: Node BST, Insert, Traversal Inorder, dan Search
# Modul   : Modul 6 - Binary Search Tree (BST) dan AVL Tree
# ==========================================================


# ==========================================================
# LATIHAN 1: Membuat Node dan BST (Insert)
# ==========================================================
# Node = 1 kotak penyimpan data di dalam BST.
# Isi: nilai, cabang kiri, cabang kanan.
class Node:
    def __init__(self, data):
        self.data  = data   # nilai node
        self.left  = None   # cabang kiri (lebih kecil)
        self.right = None   # cabang kanan (lebih besar)


# Menyisipkan nilai ke BST secara rekursif.
# Kecil → kiri, Besar → kanan, Sama → diabaikan.
def insert(root, data):
    if root is None:
        return Node(data)   # posisi kosong, langsung buat node

    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)

    return root


# --- Program utama Latihan 1 ---
root = None
data_list = [50, 30, 70, 20, 40, 60, 80]

for data in data_list:
    root = insert(root, data)

print("=" * 40)
print("LATIHAN 1: BST berhasil dibuat")
print(f"Data yang dimasukkan: {data_list}")
# Bentuk tree:
#        50
#       /  \
#      30   70
#     / \  / \
#    20 40 60 80


# ==========================================================
# LATIHAN 2: Traversal Inorder (Sorting Otomatis)
# ==========================================================
# Urutan kunjungan: Kiri → Root → Kanan.
# Hasilnya otomatis terurut dari kecil ke besar karena sifat BST.

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


print("\n" + "=" * 40)
print("LATIHAN 2: Traversal Inorder (urutan terurut naik):")
print("Hasil inorder: ", end="")
inorder(root)
# Output: 20 30 40 50 60 70 80
print()


# ==========================================================
# LATIHAN 3: Searching (Pencarian Nilai)
# ==========================================================
# Pencarian di BST: tiap langkah langsung pilih kiri atau kanan.
# Jauh lebih cepat dibanding cek satu per satu.

def search(root, key):
    if root is None:
        return False        # sampai ujung, nilai tidak ada

    if root.data == key:
        return True
    elif key < root.data:
        return search(root.left, key)
    else:
        return search(root.right, key)


print("\n" + "=" * 40)
print("LATIHAN 3: Search BST")

for key in [40, 10, 80, 55]:
    hasil = search(root, key)
    if hasil:
        print(f"  Pencarian {key}: DITEMUKAN ✓")
    else:
        print(f"  Pencarian {key}: Tidak ditemukan ✗")

# -----------------------------------------------------------
# CATATAN SINGKAT

# - BST: kiri < root < kanan → pencarian cukup O(log n) di tree seimbang.
# - Inorder = hasil sudah terurut, tanpa sorting tambahan.
# - Duplikat tidak disimpan supaya struktur BST tetap bersih.
# -----------------------------------------------------------