#=======================================================================================================
# Nama    : Muhammad Nabil Allatif
# NIM     : J0403251128
# Kelas   : TPL B2
#=======================================================================================================

#=======================================================================================================
# Latihan 5 : Generator PIN
#=======================================================================================================

def buat_pin(panjang, hasil=""):
    # base case : jika panjang hasil = panjang PIN
    if len(hasil) == panjang:
        print("PIN :", hasil)
        return
    
    # explore angka 0,1,2
    for angka in ["0", "1", "2"]:
        buat_pin(panjang, hasil + angka)

print("=======Program Generator PIN=======")
buat_pin(3)



#Mencegah angka yang sama 
#if angka not in hasil: