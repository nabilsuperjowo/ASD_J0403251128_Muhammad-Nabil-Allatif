#=========================================================
#Pratikum 1 : Konsep ADT dan FILE Handling
#Latihan Dasar 1A : Membaca seluruh isi file
#=========================================================

#membuka file dengan mode read ("r")
with open("data_mahasiswa.txt", "r" , encoding="utf-8" ) as file:
    isi_file = file.read()
print(isi_file)

print("===Hasil Read===")
print("Tipe Dara:", type(isi_file))
print("jumlah Karakter", len(isi_file))
print("jumlah baris", isi_file.count("\n")+1)

#Membuka file per Baris
print("===Membaca File Per Baris===")
jumlah_baris = 0
with open("data_mahasiswa.txt", "r" , encoding="utf-8" ) as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris.strip() #untuk menghilangkan baris baru(spasi)
        print("Baris ke-", jumlah_baris)
        print("Isinya :", baris)

#=========================================================
#Pratikum 1 : Konsep ADT dan FILE Handling
#Latihan Dasar 2 : Parsing baris menjadi kolom data
#=========================================================

with open("data_mahasiswa.txt","r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")
        print("NIM:", nim, "| Nama:", nama, " Nilai: ", nilai)


#=========================================================
#Pratikum 1 : Konsep ADT dan FILE Handling
#Latihan Dasar 3 : Membaca File dan Menyimpan ke List 
#=========================================================

data_list = [] # list untuk menampung data mahasiswa

with open("data_mahasiswa.txt","r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()

        nim, nama, nilai = baris.split(",")
        #Simpan sebagai list " [nim,nama,nilai]"
        data_list.append([nim,nama,int(nilai)])

print("==== Data Mahasiswa dalam LIST====")
print (data_list)

print("==== Jumlah Record dalam LIST====")
print ("Jumlah Record", len(data_list))

print("====Menampilkan Dara Record Tertentu====")
print("Contoh Record pertama: ", data_list[0])

#=========================================================
#Pratikum 1 : Konsep ADT dan FILE Handling
#Latihan Dasar 4 : Membaca File dan Menyimpan ke Dictionary 
#==========================================================

data_dict = {} #buat variabel untuk Dictionary
with open("data_mahasiswa.txt","r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")

        #Simpan sebagai mahasiswa ke dictionary dengan KEY NIM
        data_dict[nim] = {                  #KEY
            "nama": nama,                   #Values
            "nilai": int(nilai)             #values
        }
print("===Dara Mahasiswa dalam Dictionary===")
print(data_dict)