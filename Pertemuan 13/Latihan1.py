# ==========================================================
# nama  : Muhammad Nabil Allatif
# NIM   : J0403251128
# kelas : TPL B2
# ==========================================================

# ==========================================================
# Latihan 1 : Memahami Konsep Spanning Tree
# ==========================================================

# Daftar edge graph
# Menyimpan semua koneksi yang ada pada graph sebagai list of tuple
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]

# Contoh spanning tree
# Dipilih edge yang menghubungkan semua node tanpa membentuk cycle
# Spanning tree valid jika: semua node terhubung, tidak ada cycle, jumlah edge = n-1
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

# Menampilkan semua edge yang ada pada graph awal
print("Edge pada graph:")
for edge in edges:
    print(edge)

# Menampilkan edge-edge yang terpilih sebagai spanning tree
print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)

# Membandingkan jumlah edge graph awal vs spanning tree
# Spanning tree selalu punya lebih sedikit edge karena tidak boleh ada cycle
print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))

# Jawaban Analisis:
# 1. Apa perbedaan graph awal dan spanning tree?
#    Graph awal memiliki 5 edge dan mengandung cycle (contoh: A-C, C-D, A-D
#    membentuk siklus). Spanning tree hanya punya 3 edge (n-1 = 4-1 = 3),
#    menghubungkan semua node tanpa membentuk cycle sama sekali.
#
# 2. Mengapa spanning tree tidak boleh memiliki cycle?
#    Cycle berarti ada koneksi berlebih yang tidak diperlukan.
#    Dalam kasus nyata seperti jaringan kabel antar gedung,
#    cycle hanya membuang biaya tanpa menambah konektivitas.
#
# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
#    Spanning tree hanya butuh tepat (n-1) edge untuk menghubungkan
#    n node tanpa cycle. Edge lebih dari itu pasti akan membentuk cycle.