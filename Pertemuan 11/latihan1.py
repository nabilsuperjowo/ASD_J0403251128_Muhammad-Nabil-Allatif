# ==========================================================
# nama : Muhammad Nabil Allatif
# NIM : J0403251128
# kelas : TPL B2
# Latihan 1 
# ==========================================================


from collections import deque
graph = {
    'Rumah'       : ['Sekolah', 'Toko'],
    'Sekolah'     : ['Perpustakaan'],
    'Toko'        : ['Pasar'],
    'Perpustakaan': [],
    'Pasar'       : []
}

def bfs(graph, start):
    """Breadth-First Search – menelusuri graph level demi level."""
    visited = set()
    queue   = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

print("BFS dari Rumah:")
bfs(graph, 'Rumah')
# Output: Rumah Sekolah Toko Perpustakaan Pasar

print()   # baris baru

# ============================================================
#  JAWABAN PERTANYAAN ANALISIS
# ============================================================


# ------------------------------------------------------------


# 1. Node mana yang dikunjungi pertama?
#Node yang dikunjungi pertama adalah 'Rumah' karena itu adalah node awal (start node) yang dimasukkan ke dalam queue. Setelah 'Rumah', BFS
#Setelah 'Rumah', urutan kunjungan adalah:
#Rumah → Sekolah → Toko → Perpustakaan → Pasar
#(level-by-level: Level 0 = Rumah, Level 1 = Sekolah & Toko,
#Level 2 = Perpustakaan & Pasar)

# 2. Mengapa BFS cocok untuk mencari jalur terdekat?
#BFS menjelajahi graph secara MELEBAR (level demi level).
#Artinya, BFS selalu mengunjungi semua node yang berjarak
#1 langkah dari start terlebih dahulu, kemudian 2 langkah,dst.  Akibatnya, saat BFS pertama kali mencapai sebuah 
# node tujuan, jalur yang ditemukan DIJAMIN merupakan jalur
#dengan jumlah edge (langkah) paling sedikit – yaitu jalurterpendek dalam graph berbobot-sama (unweighted graph).
#Sifat inilah yang tidak dimiliki DFS, karena DFS bisa
#mencapai tujuan melalui jalur yang jauh lebih panjang
#sebelum menemukan jalur yang lebih pendek.

# 3. Apa perbedaan urutan BFS jika struktur graph diubah?
#Urutan BFS SANGAT dipengaruhi oleh:
#a) Urutan neighbor dalam adjacency list  →  jika urutan tetangga dibalik 
# (misal 'Rumah': ['Toko','Sekolah']), urutan kunjungan Level 1 ikut terbalik: Rumah → Toko → Sekolah → Pasar → Perpustakaan
#b) Penambahan edge baru  →  node yang sebelumnya berada di Level 2 bisa berpindah ke Level 1 jika ada edge langsung dari 'Rumah'.  
#Contoh: menambahkan 'Pasar' ke tetangga 'Rumah' membuat 'Pasar' dikunjungi lebih awal daripada 'Perpustakaan'.
#c) Perubahan start node  →  seluruh urutan kunjunganberubah karena titik awal penjelajahan berbeda. 
# Intinya: BFS SELALU mempertahankan sifat level-order, tetapi node mana yang muncul pertama 
# di tiap level bergantung pada susunan adjacency list.
# ------------------------------------------------------------