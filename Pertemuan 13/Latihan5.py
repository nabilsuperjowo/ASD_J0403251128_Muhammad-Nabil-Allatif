# ==========================================================
# nama  : Muhammad Nabil Allatif
# NIM   : J0403251128
# kelas : TPL B2
# ==========================================================

# ==========================================================
# Latihan 5 : Buat Program MST dengan Kasus Baru
# ==========================================================


# Kasus 2: Jaringan Komputer
# RouterA - RouterB = 3
# RouterA - RouterC = 2
# RouterB - RouterD = 5
# RouterC - RouterD = 1
# RouterB - RouterC = 4

# Daftar edge: (bobot, node1, node2)
# Bobot di posisi pertama agar bisa diurutkan oleh edges.sort()
edges = [
    (3, 'RouterA', 'RouterB'),
    (2, 'RouterA', 'RouterC'),
    (5, 'RouterB', 'RouterD'),
    (1, 'RouterC', 'RouterD'),
    (4, 'RouterB', 'RouterC')
]

# Langkah 1: Urutkan semua edge dari bobot terkecil ke terbesar
edges.sort()

mst = []          # Menyimpan edge-edge yang masuk ke MST
total_weight = 0  # Akumulasi total bobot MST

# Set untuk mencatat node yang sudah terhubung ke MST
connected = set()

for weight, u, v in edges:
    # Cek apakah edge ini membentuk cycle:
    # Jika KEDUA node sudah ada di connected, akan terbentuk cycle -> skip
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
# 1. Kasus apa yang dipilih?
#    Kasus 2 - Jaringan Komputer: menghubungkan RouterA, RouterB,
#    RouterC, RouterD dengan total biaya koneksi minimum.
#
# 2. Algoritma apa yang digunakan?
#    Algoritma Kruskal, karena data sudah berbentuk daftar edge
#    sehingga mudah diurutkan dan diproses satu per satu.
#
# 3. Edge mana saja yang dipilih dalam MST?
#    RouterC - RouterD (bobot 1), RouterA - RouterC (bobot 2),
#    RouterA - RouterB (bobot 3). Total 3 edge untuk 4 node (n-1 = 3).
#
# 4. Berapa total bobot MST?
#    Total = 1 + 2 + 3 = 6
#
# 5. Mengapa edge tertentu tidak dipilih?
#    RouterB - RouterC (bobot 4): saat diproses, RouterB dan RouterC
#    sudah terhubung lewat RouterA, sehingga akan membentuk cycle.
#    RouterB - RouterD (bobot 5): saat diproses, RouterB dan RouterD
#    sudah terhubung lewat RouterA - RouterC - RouterD, cycle juga.