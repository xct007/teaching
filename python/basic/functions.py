"""
Contoh penggunaan fungsi

Contoh 1: Fungsi
Contoh 2: Fungsi Parameter
Contoh 3: Fungsi Default Parameter
Contoh 4: Fungsi Keyword Parameter
Contoh 5: Fungsi Arbitrary Parameter
Contoh 6: Fungsi Return Value
Contoh 7: Fungsi Recursion
Contoh 8: Fungsi Lambda
Contoh 9: Fungsi Array
Contoh 10: Fungsi Class
"""

""" Contoh 1: Fungsi
Fungsi sederhana untuk menyapa dunia.
"""


def sapa():
    print("Halo, Dunia!")


sapa()

""" Contoh 2: Fungsi Parameter
Fungsi dengan parameter untuk menyapa nama yang diberikan.
"""


def sapa_nama(nama):
    print(f"Halo, {nama}!")


sapa_nama("John")

""" Contoh 3: Fungsi Default Parameter
Fungsi dengan parameter default.
"""


def sapa_default(nama="Dunia"):
    print(f"Halo, {nama}!")


sapa_default()
sapa_default("Alice")

""" Contoh 4: Fungsi Keyword Parameter
Menggunakan keyword saat memanggil fungsi.
"""


def sapa_lengkap(nama_depan, nama_belakang):
    print(f"Halo, {nama_depan} {nama_belakang}!")


sapa_lengkap(nama_belakang="Doe", nama_depan="John")

""" Contoh 5: Fungsi Arbitrary Parameter
Fungsi dengan jumlah parameter yang tidak tetap.
"""


def sapa_semua(*nama):
    for n in nama:
        print(f"Halo, {n}!")


sapa_semua("John", "Alice", "Bob")

""" Contoh 6: Fungsi Return Value
Fungsi yang mengembalikan nilai.
"""


def tambah(a, b):
    return a + b


hasil = tambah(5, 3)
print(hasil)

""" Contoh 7: Fungsi Recursion
Fungsi yang memanggil dirinya sendiri.
"""


def faktorial(n):
    if n == 1:
        return 1
    else:
        return n * faktorial(n-1)


print(faktorial(5))

""" Contoh 8: Fungsi Lambda
Fungsi anonim atau fungsi lambda.
"""
def kuadrat(x): return x * x


print(kuadrat(4))

""" Contoh 9: Fungsi Array
Menggunakan fungsi untuk memanipulasi array.
"""


def cetak_array(arr):
    for i in arr:
        print(i, end=' ')


array = [1, 2, 3, 4, 5]
cetak_array(array)

""" Contoh 10: Fungsi dalam Class
Fungsi sebagai metode dalam sebuah kelas.
"""


class Matematika:
    def tambah(self, a, b):
        return a + b


matematika = Matematika()
print(matematika.tambah(10, 20))
