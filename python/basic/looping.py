"""
Contoh penggunaan perulangan di Python.

Contoh 1: Basic Looping
Contoh 2: Looping with condition
Contoh 3: Looping with step
Contoh 4: Looping with break
Contoh 5: Looping with continue
Contoh 6: Nested Looping
"""

""" Contoh 1: Basic Looping
Perulangan dasar menggunakan for loop untuk menampilkan angka dari 1 hingga 5
"""
for i in range(1, 6):
    print(f"Angka: {i}")

""" Contoh 2: Looping with condition
Perulangan dengan kondisi menggunakan for loop dan if statement
"""
for i in range(1, 6):
    if i % 2 == 0:
        print(f"Angka genap: {i}")

""" Contoh 3: Looping with step
Perulangan dengan langkah (step) untuk menampilkan angka genap dari 2 hingga 10
"""
for i in range(2, 11, 2):
    print(f"Angka dengan langkah 2: {i}")

""" Contoh 4: Looping with break
Menggunakan break untuk menghentikan perulangan jika kondisi terpenuhi
"""
for i in range(1, 6):
    if i == 4:
        break
    print(f"Angka sebelum break: {i}")

""" Contoh 5: Looping with continue
Menggunakan continue untuk melewati iterasi perulangan jika kondisi terpenuhi
"""
for i in range(1, 6):
    if i == 3:
        continue
    print(f"Angka tanpa angka 3: {i}")

""" Contoh 6: Nested Looping
Perulangan bersarang (nested loop) untuk menampilkan kombinasi dari dua list
"""
warna = ["merah", "hijau", "biru"]
buah = ["apel", "jeruk", "mangga"]

for w in warna:
    for b in buah:
        print(f"Kombinasi: {w} {b}")
