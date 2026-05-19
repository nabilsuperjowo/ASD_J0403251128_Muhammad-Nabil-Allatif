# ==========================================================
# nama  : Muhammad Nabil Allatif
# NIM   : J0403251128
# kelas : TPL B2
# ==========================================================

# ==========================================================
# Implementasi Prim
# ==========================================================

import heapq 

# Representasi graph menggunakan adjacency dictionary
# Format: { node: { tetangga: bobot, ... }, ... }
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

def prim(graph, start):
    """
    Fungsi untuk menjalankan algoritma Prim.
    Parameter:
        graph : dict - representasi adjacency graph
        start : str  - node awal untuk membangun MST
    Return:
        mst          : list of (u, v, weight) - edge-edge MST
        total_weight : int - total bobot MST
    """

    # Set untuk menyimpan node yang sudah dikunjungi
    visited = set([start])

    # Priority queue: menyimpan (bobot, node_asal, node_tujuan)
    edges = []

    # Masukkan semua edge dari node awal ke priority queue
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []          # List edge hasil MST
    total_weight = 0  # Total bobot MST

    # Proses selama masih ada edge di priority queue
    while edges:
        # Ambil edge dengan bobot terkecil
        weight, u, v = heapq.heappop(edges)

        # Lewati jika node tujuan sudah dikunjungi (akan membentuk cycle)
        if v not in visited:
            visited.add(v)               # Tandai node sebagai dikunjungi
            mst.append((u, v, weight))   # Tambahkan edge ke MST
            total_weight += weight        # Akumulasikan bobot

            # Tambahkan edge-edge dari node baru ke priority queue
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst, total_weight


# Jalankan algoritma Prim mulai dari node 'A'
mst, total = prim(graph, 'A')

# Tampilkan hasil MST
print("Minimum Spanning Tree:")
for edge in mst:
 print(edge)
print("Total bobot =", total)