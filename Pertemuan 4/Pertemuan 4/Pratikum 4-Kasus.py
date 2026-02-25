#=======================================================================================================
# Nama    : Muhammad Nabil Allatif
# NIM     : J0403251118
# Kelas   : TPL B2
#=======================================================================================================

#=======================================================================================================
# Studi kasus : Sistem Antrian layanan Akademik
# Impelementasi Queue =>
# Enqueue : Memindahkan pointer ke rear (nambah data baru dari belakang)
# Dequeue : Memindahkan pointer ke front (menghapus data dari depan)
# Front -> A -> B -> C -> Real
#=======================================================================================================

#1) mendefinisikan node (Unit dasar linked list)
from platform import node


class Node:
    def __init__(self, nim, nama):
        self.nim = nim #menyimpan NIM Mahasiswa
        self.nama = nama #menyimpan Nama Mahasiswa
        self.next = None #pointer ke node berikutnya

#2) Mendefinisikan queue, terdiri dari front dan rear
class queaAkademik:
    def __init__(self):
        self.front = None #Node paling depan
        self.rear = None #Node paling belakang

    def is_empty(self):
        #Ketika queue kosong maka front = rear none
        return self.front is None
    
    #menambahkan data baru ke bagian belakang (rear)
    def enqueue(self, nim, nama):
        nodeBaru = Node(nim, nama)
        #Jika data baru masuk daru queue yang kosong maka data baru front = rear
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        #Jika queue tidak kosong, maka data baru
        self.rear.next = nodeBaru
        self.rear = nodeBaru
        
    def dequeue(self):
        #jika natrian kosong tidak ada data yang bisa dihapus
        if self.is_empty():
            print("Antrian kosong, tidak ada data yang bisa dihapus")
            return None
        
        # lihat data yang akan di hapus
        node_hapus = self.front #menyinpan data yang akan dihapus
        #geser pointer ke depan
        self.front = self.front.next
       
        #jika setelah dihapus antrian menjadi kosong, maka rear juga harus di set ke none
        if self.front is None:
            self.rear = None
        return node_hapus #mengembalikan data yang dihapus

    def tampilkan(self):
        print("Daftar Antrian Layanan Akademik:")
        current = self.front
        no = 1
        while current is not None: 
            print(f"{no}. NIM: {current.nim}, Nama: {current.nama}")
            current = current.next
            no += 1
        
# Program utama
def main():
    
    #intisiai queue akademik
    Q = queaAkademik()
    
    while True:
        print("\nMenu:")
        print("1. Tambah Mahasiswa")
        print("2. Layani Mahasiswa")
        print("3. Tampilkan Mahasiswa dalam Antrian")
        print("4. Keluar")
        
        pilihan = input("Pilih menu (1-4): ")
        
        if pilihan == '1':
            nim = input("Masukkan NIM: ")
            nama = input("Masukkan Nama: ")
            Q.enqueue(nim, nama)
            print("Antrian berhasil ditambahkan.")
        
        elif pilihan == '2':
            node_hapus = Q.dequeue()
            if node_hapus is not None:
                print(f"Antrian dengan NIM {node_hapus.nim} dan Nama {node_hapus.nama} telah dilayani.")
        
        elif pilihan == '3':
            Q.tampilkan()
        
        elif pilihan == '4':
            print("Terima kasih! Program selesai.")
            break
        
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang benar.")
# Menjalankan program utama
if __name__ == "__main__":
    main()
    