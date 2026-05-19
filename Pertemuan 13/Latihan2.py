# ==========================================================
# nama  : Muhammad Nabil Allatif
# NIM   : J0403251128
# kelas : TPL B2
# ==========================================================

# ==========================================================
# Latihan 2 :  Implementasi Algoritma Kruskal
# ==========================================================

# Daftar edge: (bobot, node1, node2)
# Kruskal membutuhkan bobot di posisi pertama agar bisa diurutkan
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Langkah 1: Urutkan semua edge dari bobot terkecil ke terbesar
# Ini adalah inti dari strategi greedy Kruskal
edges.sort()

mst = []          # Menyimpan edge-edge yang masuk ke MST
total_weight = 0  # Akumulasi total bobot MST

# Set untuk mencatat node yang sudah terhubung ke MST
connected = set()

for weight, u, v in edges:
    # Cek apakah edge ini membentuk cycle:
    # Jika KEDUA node sudah ada di connected, berarti akan terbentuk cycle -> skip
    # Jika minimal satu node belum ada, edge aman untuk ditambahkan
    if u not in connected or v not in connected:
        mst.append((u, v, weight))  # Tambahkan edge ke MST
        total_weight += weight       # Tambahkan bobotnya ke total
        connected.add(u)             # Tandai node u sudah terhubung
        connected.add(v)             # Tandai node v sudah terhubung

print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

print("Total bobot =", total_weight)

# Jawaban Analisis:
# 1. Edge mana yang dipilih pertama kali?
#    Edge C-D dengan bobot 1, karena merupakan edge dengan bobot terkecil
#    dan C serta D belum ada di set connected.
#
# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu?
#    Strategi greedy Kruskal: memilih edge terkecil lebih dulu menjamin
#    total bobot MST akan minimum. Jika edge besar dipilih dulu,
#    total bobot bisa lebih besar dari yang seharusnya.
#
# 3. Berapa total bobot MST yang dihasilkan?
#    Total = 1 (C-D) + 2 (A-C) + 3 (B-D) = 6
#
# 4. Mengapa edge tertentu tidak dipilih?
#    Edge A-B (bobot 4) dan A-D (bobot 5) tidak dipilih karena saat
#    keduanya diproses, semua node yang terlibat sudah ada di connected,
#    sehingga menambahkannya akan membentuk cycle.