class DompetDigital:
    def __init__(self, nama, pin, saldo):
        self.__nama = nama
        self.__pin = pin
        self.__saldo = saldo

    # Getter
    def get_nama(self):
        return self.__nama

    # Validasi PIN
    def verifikasi_pin(self, pin):
        return pin == self.__pin

    # Menampilkan saldo
    def cek_saldo(self):
        print(f"Saldo {self.__nama}: Rp{self.__saldo}")

    # Menambah saldo
    def tambah_saldo(self, jumlah):
        self.__saldo += jumlah
        print(f"Saldo berhasil ditambah.")
        print(f"Saldo sekarang: Rp{self.__saldo}")


# Membuat object
dompet = DompetDigital("Muhammad Nabil Azhar", "513649395237", 500000)

print("=== DOMPET DIGITAL ===")
print("Nama Pemilik:", dompet.get_nama())

# Bukti atribut private tidak bisa diakses langsung
# print(dompet.__saldo)
# print(dompet.__pin)

pin = input("\nMasukkan PIN: ")

if dompet.verifikasi_pin(pin):

    while True:

        print("\n===== MENU =====")
        print("1. Cek Saldo")
        print("2. Tambah Saldo")
        print("3. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            dompet.cek_saldo()

        elif pilihan == "2":
            jumlah = int(input("Masukkan jumlah saldo: "))
            dompet.tambah_saldo(jumlah)

        elif pilihan == "3":
            print("Terima kasih.")
            break

        else:
            print("Menu tidak tersedia.")

        lanjut = input("\nKembali ke menu? (y/n): ")

        if lanjut.lower() != "y":
            print("Terima kasih.")
            break

else:
    print("PIN salah! Akses ditolak.")
