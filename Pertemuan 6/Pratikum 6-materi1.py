#=======================================================================================================
# Nama    : Muhammad Nabil Allatif
# NIM     : J0403251128
# Kelas   : TPL B2
#=======================================================================================================

#=======================================================================================================
# Latihan 5 : Generator PIN
#=======================================================================================================

def insertion_sort(data):
    #loop mulai dari data 2 (index array 1) sampai akhir
    for i in range(1, len(data)):
        
        key = data[i] #simpan nilai yang disisipkan
        j = i - 1 #index elemen terakhir di bagian kiri
        
        #geser elemen yang lebih besar dari key ke kanan
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j] #geser elemen ke kanan
            j -= 1
            #sisipkan key ke posisi yang benar
        data[j + 1] = key
    return data

angka = [7,8,5,2,4,6]
print("hasil Sorting", insertion_sort(angka))