#=======================================================================================================
# Nama    : Muhammad Nabil Allatif
# NIM     : J0403251128
# Kelas   : TPL B2
#=======================================================================================================

# def insertion_sort(data):
#     for i in range(1, len(data)):
#         key = data[i]
#         j = i - 1

#     while j >= 0 and ______________________:
#         data[j + 1] = data[j]
#         j -= 1

#     ______________________


# Soal:
# 1. Lengkapi kondisi agar menjadi sorting ascending.
# 2. Ubah agar menjadi descending

# Jawab
# 1.
def insertion_sort(data):
    for i in range(1, len(data)):
        
        key = data[i]
        j = i - 1
        
        #geser elemen yang lebih besar dari key ke kanan
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j] #geser elemen ke kanan
            j -= 1
            #sisipkan key ke posisi yang benar
        data[j + 1] = key
    return data

angka = [7,8,5,2,4,6]
print("hasil Sorting ascending", insertion_sort(angka))
# 2.
def insertion_sort_descending(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        # Mengubah tanda > menjadi <
        #geser elemen yang lebih besar dari key ke kanan
        while j >= 0 and data[j] < key: #geser elemen ke kiri
            data[j + 1] = data[j]
            j -= 1

            data[j + 1] = key

    return data
angka = [7,8,5,2,4,6]
print("hasil Sorting descending", insertion_sort_descending(angka))