#=======================================================================================================
# Nama    : Muhammad Nabil Allatif
# NIM     : J0403251128
# Kelas   : TPL B2
#=======================================================================================================

#=======================================================================================================
# Materi Rekursif : Call stack
# Tracing bilangan (masuk-keluar)
# Input 3
# 3-2-1 | 1-2-3
#=======================================================================================================

def hitung(n):
    
    #base case : n = 0, maka berhenti
    if n == 0:
        print("Base case tercapai, berhenti")
        return
    print("Masuk hitung", n) #menunjukkan saat masuk ke fungsi dengan nilai n
    hitung(n-1) #memanggil fungsi hitung dengan n-1 (recursive case)
    print("Keluar hitung", n) #menunjukkan saat keluar dari

print("=======Program Call Stack=======")
hitung(3)