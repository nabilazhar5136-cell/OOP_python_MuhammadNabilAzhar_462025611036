class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

    # Instance Method 1
    def tampilkan_data(self):
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Jurusan: {self.jurusan}")

    # Instance Method 2
    def ganti_jurusan(self, jurusan_baru):
        self.jurusan = jurusan_baru
        print(f"{self.nama} sekarang berada di jurusan {self.jurusan}")

    # Static Method
    @staticmethod
    def informasi_universitas():
        print("Universitas memiliki berbagai program studi untuk mahasiswa.")


mahasiswa1 = Mahasiswa("Andi Saputra", "241001", "Teknik Informatika")
mahasiswa2 = Mahasiswa("Budi Santoso", "241002", "Sistem Informasi")

print("=== Data Mahasiswa 1 ===")
mahasiswa1.tampilkan_data()

print("\n=== Data Mahasiswa 2 ===")
mahasiswa2.tampilkan_data()

print("\n=== Mengubah Jurusan ===")
mahasiswa1.ganti_jurusan("Sistem Informasi")
mahasiswa2.ganti_jurusan("Teknik Informatika")

print("\n=== Static Method Melalui Class ===")
Mahasiswa.informasi_universitas()

print("\n=== Static Method Melalui Object ===")
mahasiswa1.informasi_universitas()