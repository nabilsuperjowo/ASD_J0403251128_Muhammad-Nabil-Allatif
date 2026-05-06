# ==========================================================
# nama  : Muhammad Nabil Allatif
# NIM   : J0403251128
# kelas : TPL B2
# ==========================================================


# ==========================================================
# Materi 2 : Implementasi Bellman-Ford
# ==========================================================

# representasi weighted graph dengan bobot negatif
# bellman-ford mampu menangani bobot negatif, berbeda dengan dijkstra
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}


def bellman_ford(graph, start):
    # fungsi untuk mencari jarak terpendek dari node start ke semua node lain


    # inisialisasi semua jarak dengan tak hingga (belum diketahui)
    distances = {node: float('inf') for node in graph}

    # jarak dari node awal ke dirinya sendiri adalah 0
    distances[start] = 0

    # bellman-ford melakukan relaksasi sebanyak (jumlah node - 1) kali
    # relaksasi adalah proses memperbarui jarak jika ditemukan jalur yang lebih kecil
    for _ in range(len(graph) - 1):

        # periksa semua edge yang ada di dalam graph
        for node in graph:
            for neighbor, weight in graph[node].items():

                # jika ditemukan jarak yang lebih kecil menuju neighbor, perbarui
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    return distances


# menjalankan bellman-ford dari node 'A'
hasil = bellman_ford(graph, 'A')
print(hasil)
