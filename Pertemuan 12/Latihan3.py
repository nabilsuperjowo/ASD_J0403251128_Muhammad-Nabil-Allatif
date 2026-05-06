# ==========================================================
# nama  : Muhammad Nabil Allatif
# NIM   : J0403251128
# kelas : TPL B2
# ==========================================================


# ==========================================================
# Latihan 3 : Implementasi Algoritma Bellman-Ford
# ==========================================================

# representasi weighted graph dengan bobot negatif
# kasus: jalur A -> C -> B = 4 + (-2) = 2, lebih kecil dari A -> B = 5
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}


def bellman_ford(graph, start):
    # fungsi untuk mencari jarak terpendek dari node start ke semua node lain

    # inisialisasi semua jarak dengan tak hingga
    distances = {node: float('inf') for node in graph}

    # jarak dari node awal ke dirinya sendiri adalah 0
    distances[start] = 0

    # lakukan relaksasi sebanyak (jumlah node - 1) kali
    for _ in range(len(graph) - 1):

        # periksa semua edge yang ada di dalam graph
        for node in graph:
            for neighbor, weight in graph[node].items():

                # jika jarak ke node sudah diketahui dan ditemukan jarak lebih kecil,
                # lakukan update (relaksasi edge)
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    return distances


# menjalankan bellman-ford dari node 'A'
hasil = bellman_ford(graph, 'A')

print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)


# ==========================================================
# Jawaban Analisis :
#
# 1. Berapa bobot langsung dari A ke B?
#    5 (edge langsung A -> B)
#
# 2. Berapa total bobot jalur A -> C -> B?
#    A -> C = 4, C -> B = -2, total = 4 + (-2) = 2
#
# 3. Jalur mana yang menghasilkan jarak lebih kecil menuju B?
#    A -> C -> B dengan total 2, lebih kecil dari langsung A -> B = 5
#
# 4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif?
#    Karena Bellman-Ford tidak mengunci jarak seperti Dijkstra.
#    Ia merelaksasi semua edge berulang kali sehingga bobot negatif
#    tetap bisa memperbarui jarak dengan benar
#
# 5. Apa yang dimaksud dengan proses relaksasi edge?
#    Proses memeriksa apakah jarak ke suatu node bisa diperbarui (dikurangi)
#    dengan melewati node lain. Jika distances[node] + weight < distances[neighbor],
#    maka distances[neighbor] diperbarui
#
# 6. Apa perbedaan utama Bellman-Ford dan Dijkstra?
#    Dijkstra : greedy, lebih cepat, tidak bisa menangani bobot negatif
#    Bellman-Ford : relaksasi berulang, lebih lambat, bisa menangani bobot negatif
# ==========================================================