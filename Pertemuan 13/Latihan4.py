# ==========================================================
# nama  : Muhammad Nabil Allatif
# NIM   : J0403251128
# kelas : TPL B2
# ==========================================================

# ==========================================================
# Latihan 4 : Jaringan Kabel Antar Gedung
# ==========================================================    

import heapq 

# Representasi weighted graph antar gedung kampus
# Bobot = biaya pemasangan kabel (satuan juta rupiah)
graph = {
    'GedungA': {'GedungB': 4, 'GedungC': 2, 'GedungD': 5},
    'GedungB': {'GedungA': 4, 'GedungD': 3},
    'GedungC': {'GedungA': 2, 'GedungD': 1},
    'GedungD': {'GedungA': 5, 'GedungB': 3, 'GedungC': 1}
}

# Implementasi algoritma Prim
# Membangun MST bertahap dari satu node awal ke tetangga terdekat
def prim(graph, start):
    visited = set([start])  # Tandai node awal sebagai sudah dikunjungi

    edges = []  # Priority queue: (bobot, asal, tujuan)

    # Masukkan semua koneksi dari gedung awal ke heap
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []          # Menyimpan koneksi kabel yang dipilih
    total_weight = 0  # Total biaya pemasangan kabel

    while edges:
        # Ambil koneksi dengan biaya terkecil dari heap
        weight, u, v = heapq.heappop(edges)

        # Lewati jika gedung tujuan sudah terhubung (mencegah cycle)
        if v not in visited:
            visited.add(v)               # Tandai gedung sudah terhubung
            mst.append((u, v, weight))   # Catat kabel yang dipasang
            total_weight += weight        # Akumulasi total biaya

            # Tambahkan koneksi baru dari gedung yang baru bergabung
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst, total_weight

# Jalankan Prim mulai dari GedungA
mst, total = prim(graph, 'GedungA')

print("Jaringan kabel minimum:")
for edge in mst:
    print(edge)

print("Total biaya minimum =", total, "juta rupiah")

# Jawaban Analisis:
# 1. Algoritma apa yang digunakan?
#    Algoritma Prim, karena graph direpresentasikan sebagai adjacency
#    dictionary yang sangat cocok dengan cara kerja Prim.
#
# 2. Edge mana saja yang dipilih?
#    GedungA - GedungC (biaya 2), GedungC - GedungD (biaya 1),
#    GedungD - GedungB (biaya 3)
#
# 3. Berapa total biaya minimum?
#    Total = 2 + 1 + 3 = 6 juta rupiah
#
# 4. Mengapa MST cocok digunakan pada kasus ini?
#    Karena tujuannya menghubungkan SEMUA gedung dengan biaya MINIMUM
#    tanpa redundansi. Jika ada cycle, berarti ada kabel terpasang
#    sia-sia yang hanya menambah biaya tanpa manfaat tambahan.