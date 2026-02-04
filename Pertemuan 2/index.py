#==================================================
#Pratikum 2:konsep AFT dan FILE handling (studio)
#Latihan 1: Membuat fungsi load data
#==================================================


nama_file = "data_mahasiswa.txt"

#Membuat fungsi membaca data mahasiswa
def baca_data_mahasiswa(nama_file) :
    data_dict = {} #buat variabel untuk Dictionary
    with open("data_mahasiswa.txt","r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            
            parts = baris.split(",")
            if len(parts) != 3:
                continue
            nim, nama, nilai_str = baris.split(",")
            nilai_int = int(nilai_str)
            
            
        #Simpan sebagai mahasiswa ke dictionary dengan KEY NIM
            data_dict[nim] = {                  #KEY
                "nama": nama,                   #Values
                "nilai": nilai_int             #values
        }
    return data_dict

#memanggil fungsi baca_data_mahasiswa
# buka_data = baca_data_mahasiswa(nama_file)
# print("jumlah data terbaca ", len(buka_data))

#==================================================
#Pratikum 2:konsep AFT dan FILE handling (studio)
#Latihan 1: Membuat fungsi menampilkan data
#==================================================

def tampilkan_data(data_dict):

    if len(data_dict) == 0:
        print("data kosong")
        return
    
    #Membuat Header Tabel
    print("\n=== Daftar Mahasiswa ===")
    print(f"{'NIM' : <10} | {'nama':<12} | {'nilai':>5}")
    print("=" * 36) #membuat garis header
    '''
    untuk tampilan yang rapi, atur f-string formating
        {'NIM': <10} artinya:
        tampilkan nim <= rata kiri dengan lebar 10 karakter
        {'NAMA': <12} artinya:
        tampilkan nim <= rata kiri dengan lebar 12 karakter
        {'NILAI': >5} artinya:
        tampilkan nim >= rata kanan dengan lebar 5 karakter
    '''
    for nim in sorted(data_dict):
        nama=data_dict[nim]["nama"]
        nilai=data_dict[nim]["nilai"]
        print(f"{nim:<10} | {nama: <12} | {nilai:>1}")
        
#memanggil fungsi menampilkan 
# tampilkan_data(buka_data)

#==================================================
#Pratikum 2:konsep AFT dan FILE handling (studio)
#Latihan 3: Membuat fungsi mencari data
#==================================================

def cari_data(data_dict) :
    #mencari data mahasiswa berdasarkan NIM
    nim_cari = input("masukkan NIM yang ingin di cari: ").strip()
    
    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]
        
        print("\n=== Data Mahasiswa Ditemukan===")
        print(f"NIM      : {nim_cari}")
        print(f"Nama     : {nama}")
        print(f"Nilai    : {nilai}")
    else:
        print("\nData tidak Ditemukan")
# cari_data(buka_data)
        
#==================================================
#Pratikum 2:konsep AFT dan FILE handling (studio)
#Latihan 4: Membuat fungsi update nilai
#==================================================

def update_nilai(data_dict):
    nim = input("Masukkan NIM Mahasiswa yang akan diupdate nilainya :").strip()
    
    if nim not in data_dict:
        print("NIM tidak ditemukan, update dibatalkan")
        return
    try:
        nilai_baru = int(input("masukkan nilai baru (0-100) :").strip())
    except ValueError:
        print("nilai harus berupa angka. Update dibatalkan")
        return
    
    if nilai_baru < 0 or nilai_baru >100 :
        print("Nilai harus antara 0 sampai 100.Update dibatalkan")
    
    nilai_lama = data_dict[nim]["nilai"]
    data_dict[nim]["nilai"] = nilai_baru #fungsi utama, memasukkan nilai baru ke dictionary
    
    print(f"Update Berhasil. Nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}")
    
# update_nilai(buka_data)  
# tampilkan_data(buka_data)

#===============================================================
#Pratikum 2:konsep AFT dan FILE handling (studio)
#Latihan 5: Membuat fungsi Menyimpan perubahan data ke file txt
#===============================================================

def simpan_data(nama_file,data_dict):
    with open(nama_file,"w", encoding="utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim},{nama},{nilai}\n")

# simpan_data(nama_file,buka_data)
# print("data Berhasil di SImpan")

#===============================================================
#Pratikum 2:konsep AFT dan FILE handling (studio)
#Latihan 5: Membuat fungsi Menyimpan perubahan data ke file txt
#===============================================================

def main():
    
    #menjalankan fungsi 1 load data
    buka_data = baca_data_mahasiswa(nama_file)
    
    while True:
        print("\n===== Menu Program Manajemen Data Mahasiswa =====")
        print("1. Tampilkan Data Mahasiswa")
        print("2. Cari Data Mahasiswa")
        print("3. Update Nilai Mahasiswa")
        print("4. Simpan Data ke File")
        print("0. Keluar Program")
        
        pilihan = input("Masukkan pilihan (1-5) : ").strip()
        
        if pilihan == "1":
            tampilkan_data(buka_data)
        elif pilihan == "2":
            cari_data(buka_data)
        elif pilihan == "3":
            update_nilai(buka_data)
        elif pilihan == "4":
            simpan_data(nama_file,buka_data)
            print(f"Data berhasil disimpan ke file {nama_file}.")
        elif pilihan == "0":
            print("Keluar dari program. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

main()
    