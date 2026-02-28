#=======================================================================================================
# Nama    : Muhammad Nabil Allatif
# NIM     : J0403251128
# Kelas   : TPL B2
#=======================================================================================================

#=======================================================================================================
# Materi Rekursif : Backtracking tanpa Pruning
#=======================================================================================================

def biner(n, hasil=""):
    # base case : jika panjang hasil = n
    if len(hasil) == n:
        print(hasil)
        return
    
    # choose + explore tambah "0"
    biner(n, hasil + "0")
    
    # choose + explore tambah "1"
    biner(n, hasil + "1")

print("=======Program Kombinasi Biner=======")
biner(3)