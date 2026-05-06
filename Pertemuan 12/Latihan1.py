# ==========================================================
# nama  : Muhammad Nabil Allatif
# NIM   : J0403251128
# kelas : TPL B2
# ==========================================================


# ==========================================================
# Latihan 1 : Weighted Graph dan Perhitungan Jalur
# ==========================================================

# representasi weighted graph menggunakan nested dictionary
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

# menghitung total bobot dua kemungkinan jalur dari A ke D
jalur_1 = graph['A']['B'] + graph['B']['D']  # A -> B -> D
jalur_2 = graph['A']['C'] + graph['C']['D']  # A -> C -> D

print("Jalur 1: A -> B -> D =", jalur_1)
print("Jalur 2: A -> C -> D =", jalur_2)

# bandingkan dan tampilkan jalur terpendek
if jalur_1 < jalur_2:
    print("Jalur terpendek adalah A -> B -> D")
else:
    print("Jalur terpendek adalah A -> C -> D")


# ==========================================================
# Jawaban Analisis :
#
# 1. Berapa total bobot jalur A -> B -> D?
#    A -> B = 4, B -> D = 5, total = 9
#
# 2. Berapa total bobot jalur A -> C -> D?
#    A -> C = 2, C -> D = 1, total = 3
#
# 3. Jalur mana yang dipilih sebagai jalur terpendek?
#    A -> C -> D dengan total bobot 3
#
# 4. Mengapa jalur terpendek tidak selalu ditentukan dari jumlah edge yang paling sedikit?
#    Karena pada weighted graph setiap edge punya bobot berbeda.
#    Jalur terpendek ditentukan dari total bobot terkecil, bukan jumlah edge.
#    Contoh: 3 edge dengan bobot 1+1+1=3 lebih baik dari 2 edge dengan bobot 5+5=10
# ==========================================================