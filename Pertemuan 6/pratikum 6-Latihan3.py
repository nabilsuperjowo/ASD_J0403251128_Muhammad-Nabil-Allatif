#=======================================================================================================
# Nama    : Muhammad Nabil Allatif
# NIM     : J0403251128
# Kelas   : TPL B2
#=======================================================================================================

# Buat program dengan menggunakan algoritma insertion sort
# Tracing dengan data = [5, 2, 4, 6, 1, 3]

def insertion_sort(data):
    for i in range(1, len(data)):
        
        key = data[i]
        j = i - 1
        
        print("Iterasi ke-:",i)
        print("nilai Key:", key)
        print("Bagian kiri (terurut):", data[:i])
        print("Bagian kanan (belum terurut):", data[i:])
        
        #geser elemen yang lebih besar dari key ke kanan
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j] #geser elemen ke kanan
            j -= 1
            #sisipkan key ke posisi yang benar
        data[j + 1] = key
        print("setelah disisipkan:", data)
        print("-"*50)
    return data

data = [5, 2, 4, 6, 1, 3]
print("hasil Sorting ascending", insertion_sort(data))


# soal
# 1. Tuliskan isi list setelah iterasi i = 1.
# 2. Tuliskan isi list setelah iterasi i = 3.
# 3. Berapa kali pergeseran terjadi pada iterasi i = 4?

# jawab
# 1. 
# Iterasi ke-: 1
# nilai Key: 2
# Bagian kiri (terurut): [5]
# Bagian kanan (belum terurut): [2, 4, 6, 1, 3]
# setelah disisipkan: [2, 5, 4, 6, 1, 3]

# 2.
# Iterasi ke-: 3
# nilai Key: 6
# Bagian kiri (terurut): [2, 4, 5]
# Bagian kanan (belum terurut): [6, 1, 3]
# setelah disisipkan: [2, 4, 5, 6, 1, 3]

# 3. ada 4 pergeseran yang terjad di i - 4 yaitu data 6,5,4,2 yang bergeser ke kanan 