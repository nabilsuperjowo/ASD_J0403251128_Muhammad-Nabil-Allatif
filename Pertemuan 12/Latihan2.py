# ==========================================================
# nama  : Muhammad Nabil Allatif
# NIM   : J0403251128
# kelas : TPL B2
# ==========================================================


# ==========================================================
# Latihan 2 : Implementasi Algoritma Dijkstra
# ==========================================================

import heapq

# representasi weighted graph dengan bobot positif
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}


def dijkstra(graph, start):
    # fungsi untuk mencari jarak terpendek dari node start ke semua node lain

    # inisialisasi semua jarak dengan tak hingga
    distances = {node: float('inf') for node in graph}

    # jarak dari node awal ke dirinya sendiri adalah 0
    distances[start] = 0

    # priority queue menyimpan pasangan (jarak, node)
    priority_queue = [(0, start)]

    while priority_queue:
        # ambil node dengan jarak terkecil saat ini
        current_distance, current_node = heapq.heappop(priority_queue)

        # lewati jika jarak yang diambil sudah lebih besar dari yang tercatat
        if current_distance > distances[current_node]:
            continue

        # periksa semua tetangga dari node yang sedang diproses
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # jika ditemukan jarak yang lebih kecil, perbarui jaraknya
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # masukkan tetangga ke priority queue untuk diproses nanti
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# menjalankan dijkstra dari node 'A'
hasil = dijkstra(graph, 'A')

print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)


# ==========================================================
# Jawaban Analisis :
#
# 1. Berapa jarak terpendek dari A ke B?
#    4 (langsung A -> B)
#
# 2. Berapa jarak terpendek dari A ke C?
#    2 (langsung A -> C)
#
# 3. Berapa jarak terpendek dari A ke D?
#    3 (melalui A -> C -> D = 2 + 1 = 3)
#
# 4. Mengapa jarak A ke D lebih kecil melalui C dibandingkan melalui B?
#    A -> C -> D = 2 + 1 = 3, sedangkan A -> B -> D = 4 + 5 = 9
#    Bobot melalui C jauh lebih kecil meskipun jumlah edge sama
#
# 5. Apa fungsi priority_queue dalam algoritma Dijkstra?
#    Untuk selalu memproses node dengan jarak terkecil terlebih dahulu
#    sehingga jarak yang sudah ditemukan dijamin merupakan yang terpendek
#
# 6. Mengapa Dijkstra tidak cocok untuk graph dengan bobot negatif?
#    Dijkstra menggunakan asumsi greedy: jarak yang sudah dipilih tidak akan berubah.
#    Jika ada bobot negatif, asumsi itu bisa salah dan hasil menjadi tidak akurat
# ==========================================================