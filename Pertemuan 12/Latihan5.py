# ==========================================================
# nama  : Muhammad Nabil Allatif
# NIM   : J0403251128
# kelas : TPL B2
# ==========================================================


# ==========================================================
# Latihan 5 : Studi Kasus Shortest Path Antar Kota
# Algoritma  : Dijkstra
# ==========================================================

import heapq

# representasi weighted graph hubungan antar kota
# bobot menunjukkan jarak antar kota
graph = {
    'Bogor':   {'Jakarta': 5, 'Depok': 2},
    'Depok':   {'Jakarta': 2, 'Bandung': 6},
    'Jakarta': {'Bandung': 7},
    'Bandung': {}
}


def dijkstra(graph, start):
    # fungsi untuk mencari jarak terpendek dari kota start ke semua kota lain

    # inisialisasi semua jarak dengan tak hingga
    distances = {node: float('inf') for node in graph}

    # jarak dari kota awal ke dirinya sendiri adalah 0
    distances[start] = 0

    # priority queue menyimpan pasangan (jarak, node)
    priority_queue = [(0, start)]

    while priority_queue:
        # ambil kota dengan jarak terkecil saat ini
        current_distance, current_node = heapq.heappop(priority_queue)

        # lewati jika jarak yang diambil sudah lebih besar dari yang tercatat
        if current_distance > distances[current_node]:
            continue

        # periksa semua kota yang terhubung dari kota saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # jika ditemukan jarak yang lebih kecil, perbarui jaraknya
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # masukkan ke priority queue untuk diproses nanti
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# node awal adalah Bogor
start_node = 'Bogor'

# menjalankan dijkstra dari kota Bogor
hasil = dijkstra(graph, start_node)

print(f"Jarak terpendek dari {start_node}:")
for kota, jarak in hasil.items():
    print(f"{start_node} -> {kota} = {jarak}")


# ==========================================================
# Jawaban Analisis :
#
# 1. Node awal yang digunakan apa?
#    Bogor
#
# 2. Node mana yang memiliki jarak paling kecil dari node awal?
#    Depok dengan jarak 2 (langsung Bogor -> Depok)
#
# 3. Node mana yang memiliki jarak paling besar dari node awal?
#    Bandung dengan jarak 8 (melalui Bogor -> Depok -> Bandung = 2 + 6 = 8)
#
# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus ini.
#    - Mulai dari Bogor dengan jarak 0, semua kota lain diinisialisasi tak hingga
#    - Proses Bogor: update Depok = 2, Jakarta = 5
#    - Proses Depok (jarak terkecil = 2): update Jakarta = min(5, 2+2) = 4, Bandung = 8
#    - Proses Jakarta (jarak = 4): update Bandung = min(8, 4+7) = 8 (tidak berubah)
#    - Proses Bandung (jarak = 8): tidak ada tetangga, selesai
#    - Hasil akhir: Bogor=0, Depok=2, Jakarta=4, Bandung=8
# ==========================================================