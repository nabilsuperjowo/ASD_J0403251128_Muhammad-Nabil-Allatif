#=======================================================================================================
# Nama    : Muhammad Nabil Allatif
# NIM     : J0403251128
# Kelas   : TPL B2
#=======================================================================================================

def merge_sort(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)

# Soal:
# 1. Apa yang dimaksud dengan base case?
# 2. Mengapa fungsi memanggil dirinya sendiri?
# 3. Apa tujuan fungsi merge()?

# # jawab
# 1.bertujuan untuk menghentikan kode dalam fungsi rekursif.tanpa base case kode akan terus dimemanggil dirinya sendiri selamanya
# 2. rekursif memanggil dirinya sendiri untuk memecahkan masalah besar menjadi masalah masalah kecil yang lebih mudah di jalankan(kelola)
# 3. menggabungkan 2 list yang tidak terurut menjadi 1 list