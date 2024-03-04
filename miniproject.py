import os
os.system('cls')

from prettytable import PrettyTable

class Item:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok

class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def tambah_alat_sholat(self, item, pos=None):
        new_node = Node(item)

        if pos == "awal":
            new_node.next = self.head
            self.head = new_node
        elif pos == "akhir":
            if not self.head:
                self.head = new_node
            else:
                current = self.head
                while current.next:
                    current = current.next
                current.next = new_node
        elif pos == "antara":
            if not self.head or not self.head.next:
                print("Minimal dua node untuk menambah di antara.")
                return

            nama_sebelum = input("Masukkan nama alat sholat sebelum posisi baru: ")
            current = self.head
            while current.next and current.next.item.nama != nama_sebelum:
                current = current.next

            if current.next:
                new_node.next = current.next
                current.next = new_node
            else:
                print(f"Alat Sholat dengan nama {nama_sebelum} tidak ditemukan.")
        else:
            print("Posisi tidak valid.")

    def hapus_alat_sholat(self, pos=None, nama=None):
        if not self.head:
            print("Linked list kosong. Tidak ada yang dapat dihapus.")
            return False

        if pos == "awal":
            self.head = self.head.next
        elif pos == "akhir":
            current = self.head
            if not current.next:
                self.head = None
                return True
            while current.next.next:
                current = current.next
            current.next = None
        elif pos == "antara":
            if not self.head or not self.head.next:
                print("Minimal dua node untuk menghapus di antara.")
                return False

            if not nama:
                print("Nama alat sholat tidak boleh kosong.")
                return False

            nama_sebelum = input("Masukkan nama alat sholat sebelum posisi yang ingin dihapus: ")
            current = self.head

            # Menangani kasus penghapusan di awal
            if current.item.nama == nama_sebelum:
                self.head = self.head.next
                return True

            while current.next and current.next.item.nama != nama_sebelum:
                current = current.next

            if current.next:
                current.next = current.next.next
                return True
            else:
                print(f"Alat Sholat dengan nama {nama_sebelum} tidak ditemukan.")
                return False
        else:
            print("Posisi tidak valid.")
            return False

    def tampilkan_alat_sholat(self):
        table = PrettyTable(["Nama", "Harga", "Stok"])
        current = self.head
        while current:
            table.add_row([current.item.nama, current.item.harga, current.item.stok])
            current = current.next
        return str(table)

    def ubah_alat_sholat(self, nama, harga_baru, stok_baru):
        current = self.head
        while current:
            if current.item.nama == nama:
                current.item.harga = harga_baru
                current.item.stok = stok_baru
                return True
            current = current.next
        return False

# Contoh penggunaan
alat_sholat_list = LinkedList()

while True:
    print("Menu:")
    print("1. Tambah Alat Sholat")
    print("2. Tampilkan Alat Sholat")
    print("3. Ubah Alat Sholat")
    print("4. Hapus Alat Sholat")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == '1':
        nama = input("Masukkan nama alat sholat: ")
        harga = float(input("Masukkan harga alat sholat: "))
        stok = int(input("Masukkan stok alat sholat: "))
        # Tampilkan opsi untuk menentukan posisi
        print("Pilih posisi tambahan:")
        print("1. Di Awal")
        print("2. Di Akhir")
        print("3. Di Antara")
        posisi_pilihan = input("Pilih posisi (1-3): ")

        if posisi_pilihan == '1':
            alat_sholat_list.tambah_alat_sholat(Item(nama, harga, stok), pos="awal")
            print("Alat Sholat berhasil ditambahkan di awal.")
        elif posisi_pilihan == '2':
            alat_sholat_list.tambah_alat_sholat(Item(nama, harga, stok), pos="akhir")
            print("Alat Sholat berhasil ditambahkan di akhir.")
        elif posisi_pilihan == '3':
            alat_sholat_list.tambah_alat_sholat(Item(nama, harga, stok), pos="antara")
            print("Alat Sholat berhasil ditambahkan di antara.")
        else:
            print("Pilihan posisi tidak valid.")
    elif pilihan == '2':
        print(alat_sholat_list.tampilkan_alat_sholat())
    elif pilihan == '3':
        nama = input("Masukkan nama alat sholat yang ingin diubah: ")
        harga_baru = float(input("Masukkan harga baru alat sholat: "))
        stok_baru = int(input("Masukkan stok baru alat sholat: "))
        if alat_sholat_list.ubah_alat_sholat(nama, harga_baru, stok_baru):
            print("Alat Sholat berhasil diubah.")
        else:
            print(f"Alat Sholat dengan nama {nama} tidak ditemukan.")
    elif pilihan == '4':
        # Tampilkan opsi untuk menentukan posisi penghapusan
        print("Pilih posisi penghapusan:")
        print("1. Di Awal")
        print("2. Di Akhir")
        print("3. Di Antara")
        posisi_pilihan_hapus = input("Pilih posisi (1-3): ")
        
        if posisi_pilihan_hapus == '1':
            if alat_sholat_list.hapus_alat_sholat(pos="awal"):
                print("Alat Sholat di awal berhasil dihapus.")
            else:
                print("Alat Sholat di awal tidak ditemukan atau tidak dapat dihapus.")
        elif posisi_pilihan_hapus == '2':
            if alat_sholat_list.hapus_alat_sholat(pos="akhir"):
                print("Alat Sholat di akhir berhasil dihapus.")
            else:
                print("Alat Sholat di akhir tidak ditemukan atau tidak dapat dihapus.")
        elif posisi_pilihan_hapus == '3':
            nama_hapus = input("Masukkan nama alat sholat yang ingin dihapus: ")
            if alat_sholat_list.hapus_alat_sholat(pos="antara", nama=nama_hapus):
                print(f"Alat Sholat dengan nama {nama_hapus} berhasil dihapus.")
            else:
                print(f"Alat Sholat dengan nama {nama_hapus} tidak ditemukan atau tidak dapat dihapus.")
        else:
            print("Pilihan posisi tidak valid.")
    elif pilihan == '5':
        print("Terima kasih. Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih 1-5.")
