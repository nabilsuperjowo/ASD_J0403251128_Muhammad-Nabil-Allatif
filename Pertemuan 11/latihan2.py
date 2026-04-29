# ==========================================================
# nama : Muhammad Nabil Allatif
# NIM : J0403251128
# kelas : TPL B2
# Latihan 2
# ==========================================================

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def dfs(graph, node, visited):
    """Depth-First Search – menelusuri graph sedalam mungkin."""
    visited.add(node)
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

visited = set()
print("DFS dari A:")
dfs(graph, 'A', visited)
# Output: A B D E C F

print()   # baris baru

#PERBANDINGAN CEPAT  –  BFS vs DFS pada graph yang sama

from collections import deque

def bfs(graph, start):
    visited_b = set()
    queue     = deque([start])
    visited_b.add(start)
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited_b:
                visited_b.add(neighbor)
                queue.append(neighbor)

print("BFS dari A  :")
bfs(graph, 'A')
# Output: A B C D E F

print()

# ============================================================
#  JAWABAN PERTANYAAN ANALISIS
# ============================================================

# ------------------------------------------------------------
# 1. Mengapa DFS masuk ke node terdalam terlebih dahulu? 
#DFS menggunakan strategi rekursi (atau stack eksplisit).Setiap kali DFS mengunjungi sebuah node, ia LANGSUNG
#memanggil dirinya sendiri (rekursi) untuk menjelajahineighbor PERTAMA node tersebut sebelum kembali ke nodesebelumnya. 
#Akibatnya, DFS terus menuruni satu cabanghingga tidak ada lagi neighbor yang belum dikunjungi
#(node terdalam / leaf), baru kemudian backtrack ke node induk dan menjelajahi cabang berikutnya. Itulah sebabnya urutan 
#DFS di graph ini adalah:
#A → B → D (terdalam cabang B) → backtrack ke B → E (terdalam cabang B) → backtrack ke A → C → F (terdalam cabang C)

# 2. Apa yang terjadi jika urutan neighbor diubah?
#Urutan kunjungan DFS langsung berubah mengikuti urutan neighbor dalam adjacency list.  Contoh:
#  Jika graph['A'] = ['C', 'B']  (C didahulukan):
#   DFS menghasilkan:  A → C → F → B → D → E
#  Jika graph['B'] = ['E', 'D']  (E didahulukan):
#   DFS menghasilkan:  A → B → E → D → C → F
#
#DFS TIDAK menjamin urutan yang tetap; ia semata-mata mengikuti neighbor pertama yang tersedia di tiap node.
#Hal ini berbeda dengan BFS yang tetap mengunjungi seluruh
#node satu level sebelum turun ke level berikutnya — meskipun urutan dalam satu level juga dipengaruhi susunan adjacency list.

# ------------------------------------------------------------
# 3. Bandingkan hasil DFS dengan BFS pada graph yang sama
#    Graph:  A → [B, C],  B → [D, E],  C → [F]
#

#     Aspek     DFS               BFS                      
#     Output     A B D E C F      A B C D E F              
#     Urutan     Cabang B tuntas  Level 1 (B,C) dulu,      
#               sebelum cabang C  baru Level 2 (D,E,F)     
#     Struktur  Stack / Rekursi   Queue (FIFO)             
#     Jalur     Tidak terpendek   Selalu terpendek         
#     Memori     O(kedalaman)     O(lebar level terbesar)  
#     Cocok     Eksplorasi,       Jalur terpendek,         
#     untuk     topologi, maze    level-order traversal    

#DFS menyelesaikan satu cabang secara penuh sebelum berpindah ke cabang lain  → lebih hemat memori pada graph yang dalam dan sempit.
#BFS mengunjungi semua node level demi level → lebihmudah menemukan jalur terpendek, tetapi butuh memorilebih besar pada graph yang lebar.
#Keduanya menghasilkan SEMUA node terkunjungi, hanya berbeda URUTAN kunjungannya.
# ------------------------------------------------------------