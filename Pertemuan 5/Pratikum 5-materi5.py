#=======================================================================================================
# Nama    : Muhammad Nabil Allatif
# NIM     : J0403251128
# Kelas   : TPL B2
#=======================================================================================================

#=======================================================================================================
# Materi Rekursif : Backtracking dengan Pruning
#=======================================================================================================

def biner_batas(n, batas, hasil="", jumlah_1=0):
    # pruning : jika jumlah_1 > batas, hentikan
    if jumlah_1 > batas:
        return
    
    # base case : jika panjang hasil = n
    if len(hasil) == n:
        print(hasil)
        return
    
    # pilih "0"
    biner_batas(n, batas, hasil + "0", jumlah_1)
    
    # pilih "1"
    biner_batas(n, batas, hasil + "1", jumlah_1 + 1)

print("=======Program Biner dengan Batas=======")
biner_batas(4, 2)