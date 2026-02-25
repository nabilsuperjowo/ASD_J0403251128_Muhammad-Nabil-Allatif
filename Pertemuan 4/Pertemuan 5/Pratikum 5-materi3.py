#=======================================================================================================
# Nama    : Muhammad Nabil Allatif
# NIM     : J0403251128
# Kelas   : TPL B2
#=======================================================================================================

#=======================================================================================================
# Materi Rekursif : Menjumlahkan Elemen dalam List
#=======================================================================================================

def jumlah_list(data, index=0):
    #base case : jika list kosong, jumlahnya 0
    if index == len(data):
        return 0
    
    #recursive case : jumlah elemen pertama + jumlah sisa list
    return data[index] + jumlah_list(data, index + 1)
print("=======Program Jumlah List=======")
print(jumlah_list([1, 2, 3, 4, 5]))