
class Person:
    def __init__(
        self,
        nama,
        umur,
        nim=None,
        id_karyawan=None,
        mata_kuliah=None
    ):
        self.nama = nama
        self.umur = umur


class Student(Person):
    def __init__(
        self,
        nama,
        umur,
        nim,
        id_karyawan=None,
        mata_kuliah=None
    ):
        super().__init__(
            nama,
            umur,
            nim,
            id_karyawan,
            mata_kuliah
        )
        self.nim = nim


class Employee(Person):
    def __init__(
        self,
        nama,
        umur,
        nim=None,
        id_karyawan=None,
        mata_kuliah=None
    ):
        super().__init__(
            nama,
            umur,
            nim,
            id_karyawan,
            mata_kuliah
        )
        self.id_karyawan = id_karyawan


class Assistant(Student, Employee):
    def __init__(
        self,
        nama,
        umur,
        nim,
        id_karyawan,
        mata_kuliah
    ):
        super().__init__(
            nama,
            umur,
            nim,
            id_karyawan,
            mata_kuliah
        )
        self.id_karyawan = id_karyawan
        self.mata_kuliah = mata_kuliah

    def tampilkan_data(self):
        print("\n=== DATA ASISTEN MAHASISWA ===")
        print(f"Nama: {self.nama}")
        print(f"Umur: {self.umur}")
        print(f"NIM: {self.nim}")
        print(f"ID Karyawan: {self.id_karyawan}")
        print(f"Mata Kuliah yang Dibantu: {self.mata_kuliah}")


# Program Utama
print("==========================================")
print("     SISTEM INFORMASI MAHASISWA")
print("==========================================")

nama = input("Masukkan nama: ")
umur = int(input("Masukkan umur: "))
nim = input("Masukkan NIM: ")
id_karyawan = input("Masukkan ID Karyawan: ")
mata_kuliah = input("Masukkan mata kuliah yang dibantu: ")

asisten = Assistant(
    nama,
    umur,
    nim,
    id_karyawan,
    mata_kuliah
)

asisten.tampilkan_data()

