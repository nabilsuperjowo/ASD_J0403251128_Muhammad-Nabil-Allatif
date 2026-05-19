# ==========================================================
# nama  : Muhammad Nabil Allatif
# NIM   : J0403251128
# kelas : TPL B2
# ==========================================================

# ==========================================================
# Latihan 3 : Implementasi Algoritma Prim
# ==========================================================

import heapq

# Representasi graph sebagai adjacency dictionary
# Format: { node: { tetangga: bobot } }
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

def prim(graph, start):
    # Mulai dari node awal, langsung tandai sebagai sudah dikunjungi
    visited = set([start])

    edges = []  # Priority queue berisi (bobot, node_asal, node_tujuan)

    # Masukkan semua edge dari node awal ke dalam heap
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []          # Menyimpan edge-edge hasil MST
    total_weight = 0  # Akumulasi total bobot MST

    while edges:
        # Ambil edge dengan bobot terkecil dari heap
        weight, u, v = heapq.heappop(edges)

        # Lewati jika node tujuan sudah dikunjungi (mencegah cycle)
        if v not in visited:
            visited.add(v)               # Tandai node sebagai dikunjungi
            mst.append((u, v, weight))   # Tambahkan edge ke MST
            total_weight += weight        # Tambahkan bobot ke total

            # Masukkan edge-edge baru dari node yang baru bergabung
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst, total_weight

mst, total = prim(graph, 'A')

print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

print("Total bobot =", total)

# Jawaban Analisis:
# 1. Node awal apa yang digunakan?
#    Node 'A' digunakan sebagai titik awal pembangunan MST.
#
# 2. Edge mana yang dipilih pertama kali?
#    Edge A-C dengan bobot 2, karena dari node A edge terkecil
#    yang tersedia adalah A-C (2), lebih kecil dari A-B (4) dan A-D (5).
#
# 3. Bagaimana Prim menentukan edge berikutnya?
#    Prim menggunakan min-heap. Setiap node baru yang bergabung,
#    semua edge ke tetangga yang belum dikunjungi dimasukkan ke heap.
#    Lalu diambil edge dengan bobot terkecil dari heap.
#
# 4. Berapa total bobot MST yang dihasilkan?
#    Total = 2 (A-C) + 1 (C-D) + 3 (D-B) = 6
#
# 5. Apa perbedaan pendekatan Prim dan Kruskal?
#    Kruskal mengurutkan semua edge secara global lalu memilih dari
#    yang terkecil (fokus pada edge, cocok untuk sparse graph).
#    Prim mulai dari satu node lalu berkembang ke tetangga terdekat
#    (fokus pada node, cocok untuk dense graph).