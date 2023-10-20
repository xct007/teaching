"""
Contoh penggunaan statement kondisional dalam bahasa Python.

Contoh 1: Statement If
Contoh 2: Statement If-else
Contoh 3: Statement If-elif-else
Contoh 4: Nested If
Contoh 5: Short Hand If
Contoh 6: Short Hand If-else
Contoh 7: Statement And
Contoh 8: Statement Or
Contoh 9: Statement Not
Contoh 10: Statement Pass
Contoh 11: Statement Break
Contoh 12: Statement Continue
Contoh 13: Statement Else
Contoh 14: Statement Try Except
Contoh 15: Statement Raise
Contoh 16: Statement Finally
Contoh 17: Statement User Input
"""

""" Contoh 1: Statement If
Mengecek apakah angka lebih besar dari 5
"""
if 7 > 5:
    print("7 lebih besar dari 5")

""" Contoh 2: Statement If-else
Mengecek apakah angka adalah bilangan genap atau ganjil
"""
angka = 8
if angka % 2 == 0:
    print("Angka adalah bilangan genap")
else:
    print("Angka adalah bilangan ganjil")

""" Contoh 3: Statement If-elif-else
Mengecek nilai dari angka
"""
angka = 7
if angka > 10:
    print("Lebih besar dari 10")
elif angka > 5:
    print("Lebih besar dari 5 tetapi tidak lebih dari 10")
else:
    print("5 atau kurang")

""" Contoh 4: Nested If
Mengecek beberapa kondisi bersarang
"""
if angka > 5:
    print("Lebih besar dari 5")
    if angka > 10:
        print("Juga lebih besar dari 10")

""" Contoh 5: Short Hand If
Mengecek satu kondisi tanpa else
"""
if angka > 5:
    print("Lebih besar dari 5")

""" Contoh 6: Short Hand If-else
Mengecek satu kondisi dengan else dalam satu baris
"""
print("Genap") if angka % 2 == 0 else print("Ganjil")

""" Contoh 7: Statement And
Mengecek lebih dari satu kondisi menggunakan and
"""
if angka > 5 and angka < 10:
    print("Angka di antara 5 dan 10")

""" Contoh 8: Statement Or
Mengecek lebih dari satu kondisi menggunakan or
"""
if angka < 5 or angka > 10:
    print("Angka kurang dari 5 atau lebih dari 10")

""" Contoh 9: Statement Not
Menggunakan not untuk mengecek kebalikan dari suatu kondisi
"""
if not angka < 5:
    print("Angka tidak kurang dari 5")

""" Contoh 10: Statement Pass
Placeholder untuk menyatakan belum ada kode yang dijalankan
"""
if angka > 5:
    pass

""" Contoh 11: Statement Break
Keluar dari loop jika kondisi terpenuhi
"""
for i in range(5):
    if i == 3:
        break
    print(i)

""" Contoh 12: Statement Continue
Melanjutkan ke iterasi berikutnya dalam loop
"""
for i in range(5):
    if i == 3:
        continue
    print(i)

""" Contoh 13: Statement Else
Bagian ini dijalankan jika kondisi pada if atau loop tidak terpenuhi
"""
for i in range(3):
    print(i)
else:
    print("Loop selesai")

""" Contoh 14: Statement Try Except
Menangani exception atau error yang mungkin terjadi
"""
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Tidak bisa dibagi dengan nol")

""" Contoh 15: Statement Raise
Memicu exception sesuai kebutuhan
"""
try:
    raise ValueError("Ini adalah ValueError")
except ValueError as e:
    print(e)

""" Contoh 16: Statement Finally
Bagian ini akan dijalankan, ada atau tidak ada exception
"""
try:
    print("Hello")
finally:
    print("Finally, saya dijalankan")

""" Contoh 17: Statement User Input
Menerima masukan dari user
"""
nama = input("Masukkan nama Anda: ")
print(f"Halo, {nama}")
