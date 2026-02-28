#=======================================================================================================
# Nama    : Muhammad Nabil Allatif
# NIM     : J0403251128
# Kelas   : TPL B2
#=======================================================================================================

#=======================================================================================================
# Latihan 4 : Backtracking Dasar
#=======================================================================================================

def kombinasi(n, hasil=""):
    # base case : jika panjang hasil = n
    if len(hasil) == n:
        print(hasil)
        return
    
    # choose + explore tambah "A"
    kombinasi(n, hasil + "A")
    
    # choose + explore tambah "B"
    kombinasi(n, hasil + "B")

print("=======Program Kombinasi Huruf=======")
kombinasi(2)