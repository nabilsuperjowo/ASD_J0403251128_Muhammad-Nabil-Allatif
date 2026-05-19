# ==========================================================
# nama  : Muhammad Nabil Allatif
# NIM   : J0403251128
# kelas : TPL B2
# ==========================================================

# ==========================================================
# Implementasi Kruskal
# ==========================================================

# Daftar edge: (bobot, node1, node2)
# Setiap tuple berisi bobot edge dan dua node yang dihubungkan
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan edge berdasarkan bobot terkecil ke terbesar
# Ini adalah langkah pertama algoritma Kruskal
edges.sort()

mst = []           # List untuk menyimpan edge yang masuk MST
total_weight = 0   # Akumulator total bobot MST

# Set untuk menyimpan node-node yang sudah terhubung ke MST
connected = set()

# Iterasi setiap edge dari yang terkecil
for weight, u, v in edges:
    # Cek apakah edge ini akan membentuk cycle sederhana
    # Edge aman ditambahkan jika minimal satu nodenya belum terhubung
    if u not in connected or v not in connected:
        mst.append((u, v, weight))   # Tambahkan edge ke MST
        total_weight += weight        # Akumulasikan bobot
        connected.add(u)              # Tandai node u sudah terhubung
        connected.add(v)              # Tandai node v sudah terhubung

# Tampilkan hasil MST
print("Minimum Spanning Tree:")
for edge in mst:
 print(edge)
print("Total bobot =", total_weight)