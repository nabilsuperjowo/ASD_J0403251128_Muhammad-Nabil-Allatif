# ==========================================================
# nama  : Muhammad Nabil Allatif
# NIM   : J0403251128
# kelas : TPL B2
# ==========================================================


# ==========================================================
# Materi 1 : Implementasi Dijkstra
# ==========================================================

# modul heapq digunakan untuk membuat priority queue (min-heap)
# agar selalu memproses node dengan jarak terkecil terlebih dahulu
import heapq

# representasi weighted graph menggunakan nested dictionary
# format: { node: { tetangga: bobot } }
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}


def dijkstra(graph, start):
    # fungsi untuk mencari jarak terpendek dari node start ke semua node lain
    
    # inisialisasi semua jarak dengan tak hingga (belum diketahui)
    distances = {node: float('inf') for node in graph}

    # jarak dari node awal ke dirinya sendiri adalah 0
    distances[start] = 0

    # priority queue menyimpan pasangan (jarak, node)
    # heapq akan selalu mengeluarkan elemen dengan jarak terkecil
    pq = [(0, start)]

    while pq:
        # ambil node dengan jarak terkecil saat ini
        current_distance, current_node = heapq.heappop(pq)

        # periksa semua tetangga dari node yang sedang diproses
        for neighbor, weight in graph[current_node].items():
            # hitung jarak baru menuju tetangga melalui node saat ini
            distance = current_distance + weight

            # jika ditemukan jarak yang lebih kecil, perbarui jaraknya
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # masukkan tetangga ke priority queue untuk diproses nanti
                heapq.heappush(pq, (distance, neighbor))

    return distances


# menjalankan dijkstra dari node 'A'
hasil = dijkstra(graph, 'A')
print(hasil)
