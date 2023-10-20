"""
Contoh penggunaan class di Python.

Contoh 1: Class
Contoh 2: Object
Contoh 3: The __init__() Function
Contoh 4: Object Methods
Contoh 5: The self Parameter
Contoh 6: Modify Object Properties
Contoh 7: Delete Object Properties  
Contoh 8: Delete Objects
Contoh 9: The pass Statement
Contoh 10: Class and Object
Contoh 11: Inheritance
Contoh 12: Add Methods
Contoh 13: Add Properties
Contoh 14: The super() Function
Contoh 15: Iterators
Contoh 16: StopIteration

Jalankan contoh kode berikut satu-satu untuk menghindari terjadi error.
"""

""" Contoh 1: Class
Membuat kelas sederhana bernama Orang.
"""


class Orang:
    pass


""" Contoh 2: Object
Membuat objek dari kelas Orang.
"""
person1 = Orang()

""" Contoh 3: The __init__() Function
Menggunakan fungsi __init__() untuk menginisialisasi objek.
"""


class Orang:
    def __init__(self, nama, usia):
        self.nama = nama
        self.usia = usia


person1 = Orang("John", 30)

""" Contoh 4: Object Methods
Menambahkan metode ke kelas.
"""


class Orang:
    def salam(self):
        print(f"Halo, nama saya {self.nama}")


person1 = Orang("John", 30)
person1.salam()

""" Contoh 5: The self Parameter
Parameter self merujuk pada instance objek itu sendiri.
"""
# Diwakili oleh 'self' dalam metode salam()

""" Contoh 6: Modify Object Properties
Memodifikasi properti objek.
"""
person1.nama = "Alice"
person1.salam()

""" Contoh 7: Delete Object Properties  
Menghapus properti objek.
"""
del person1.usia

""" Contoh 8: Delete Objects
Menghapus objek itu sendiri.
"""
del person1

""" Contoh 9: The pass Statement
Placeholder jika tidak ada isi dari kelas atau metode.
"""


class Kosong:
    pass


""" Contoh 10: Class and Object
Kelas dengan objek dan metode.
"""
# Sudah diwakili oleh contoh sebelumnya.

""" Contoh 11: Inheritance
Pewarisan dari kelas lain.
"""


class Mahasiswa(Orang):
    pass


""" Contoh 12: Add Methods
Menambahkan metode ke kelas turunan.
"""


class Mahasiswa(Orang):
    def belajar(self):
        print(f"{self.nama} sedang belajar")


""" Contoh 13: Add Properties
Menambahkan properti ke kelas turunan.
"""


class Mahasiswa(Orang):
    def __init__(self, nama, usia, npm):
        super().__init__(nama, usia)
        self.npm = npm


""" Contoh 14: The super() Function
Menggunakan fungsi super untuk memanggil metode dari kelas induk.
"""
# Sudah diwakili oleh contoh sebelumnya.

""" Contoh 15: Iterators
Membuat iterator dalam kelas.
"""


class Bilangan:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


bilangan = Bilangan()
iterasi = iter(bilangan)

print(next(iterasi))
print(next(iterasi))

""" Contoh 16: StopIteration
Menghentikan iterasi.
"""


class BilanganTerbatas:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 3:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
