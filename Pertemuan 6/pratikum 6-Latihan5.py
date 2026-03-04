#=======================================================================================================
# Nama    : Muhammad Nabil Allatif
# NIM     : J0403251128
# Kelas   : TPL B2
#=======================================================================================================

def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:    #1
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

# Soal:
# 1. Lengkapi kondisi agar menjadi ascending.
# 2. Jelaskan fungsi result.extend()

# jawab
# 1. left[i] <= right[j]
# 2. berfunsi menggabungkan isi dari 2 list dari daftar data ,jadi data left misal [1,2,3] dan data right[4,5,6] maka extend akan menggabungkannya menjadi [1,2,3,4,5,6]
