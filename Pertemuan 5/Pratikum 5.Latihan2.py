#=======================================================================================================
# Nama    : Muhammad Nabil Allatif
# NIM     : J0403251128
# Kelas   : TPL B2
#=======================================================================================================

#=======================================================================================================
# Latihan 2 : Tracing Rekursi
#=======================================================================================================

def countdown(n):
    # base case : jika n = 0, berhenti
    if n == 0:
        print("Selesai")
        return
    
    print("Masuk :", n)   # stacking (masuk ke stack)
    countdown(n - 1)     # recursive call
    print("Keluar :", n)  # unwinding (keluar dari stack)

print("=======Program Tracing Countdown=======")
countdown(3)