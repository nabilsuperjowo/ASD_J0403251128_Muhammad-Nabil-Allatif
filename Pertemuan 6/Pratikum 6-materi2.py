#=======================================================================================================
# Nama    : Muhammad Nabil Allatif
# NIM     : J0403251128
# Kelas   : TPL B2
#=======================================================================================================

#=======================================================================================================
# Insertion Sort dengan tracing
#=======================================================================================================

def insertion_sort(data):
    #melihat data awal
    print("Data Awal:", data)
    print("="*50)
            
    #loop mulai dari data 2 (index array 1) sampai akhir
    for i in range(1, len(data)):
        
        
        key = data[i] #simpan nilai yang disisipkan
        j = i - 1 #index elemen terakhir di bagian kiri
        
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

angka = [7,8,5,2,4,6]
print("hasil Sorting", insertion_sort(angka))