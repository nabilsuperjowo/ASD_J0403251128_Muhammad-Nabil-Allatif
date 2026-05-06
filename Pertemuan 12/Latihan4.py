# ==========================================================
# nama  : Muhammad Nabil Allatif
# NIM   : J0403251128
# kelas : TPL B2
# ==========================================================


# ==========================================================
# Latihan 4 : Studi Kasus Jalur Terpendek Antar Lokasi Kampus
# Algoritma  : Dijkstra
# ==========================================================

import heapq

# representasi graph lokasi kampus
# bobot menunjukkan waktu tempuh dalam menit antar lokasi
graph = {
    'Gerbang':      {'Perpustakaan': 6, 'Kantin': 2},
    'Perpustakaan': {'Lab': 3},
    'Kantin':       {'Lab': 4, 'Aula': 7},
    'Lab':          {'Aula': 1},
    'Aula':         {}
}


def dijkstra(graph, start):
    # fungsi untuk mencari waktu tempuh terpendek dari lokasi start ke semua lokasi lain

    # inisialisasi semua jarak dengan tak hingga
    distances = {node: float('inf') for node in graph}

    # jarak dari lokasi awal ke dirinya sendiri adalah 0
    distances[start] = 0

    # priority queue menyimpan pasangan (jarak, node)
    priority_queue = [(0, start)]

    while priority_queue:
        # ambil lokasi dengan waktu tempuh terkecil saat ini
        current_distance, current_node = heapq.heappop(priority_queue)

        # lewati jika jarak yang diambil sudah lebih besar dari yang tercatat
        if current_distance > distances[current_node]:
            continue

        # periksa semua lokasi yang terhubung dari lokasi saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # jika ditemukan waktu tempuh yang lebih kecil, perbarui
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # masukkan ke priority queue untuk diproses nanti
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# menjalankan dijkstra dari Gerbang Kampus
hasil = dijkstra(graph, 'Gerbang')

print("Jarak terpendek dari Gerbang Kampus:")
for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "menit")


# ==========================================================
# Jawaban Analisis :
#
# 1. Lokasi mana yang paling dekat dari Gerbang?
#    Kantin, dengan waktu tempuh 2 menit (langsung Gerbang -> Kantin)
#
# 2. Berapa waktu tempuh terpendek dari Gerbang ke Aula?
#    7 menit, melalui Gerbang -> Kantin -> Lab -> Aula = 2 + 4 + 1 = 7
#    (lebih kecil dari Gerbang -> Kantin -> Aula = 2 + 7 = 9)
#
# 3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan.
#    Tidak selalu. Contohnya ke Aula, jalur langsung Gerbang -> Kantin -> Aula = 9 menit,
#    sedangkan melewati Lab lebih kecil yaitu 7 menit.
#    Jalur dengan lebih banyak node bisa lebih cepat jika total bobotnya lebih kecil.
#
# 4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini?
#    Karena semua bobot (waktu tempuh) bernilai positif.
#    Dijkstra bekerja optimal dan lebih cepat dari Bellman-Ford pada kasus seperti ini
# ==========================================================