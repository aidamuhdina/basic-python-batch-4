nama_buah = []
def tambah_nama_buah(nama):
    nama_buah.append(nama)
    print_nama_buah()

def print_nama_buah():
    for buah in nama_buah:
        print(buah)
    print("-------")

tambah_nama_buah("jeruk")
tambah_nama_buah("semangka")
tambah_nama_buah("melon")


print(nama_buah)
# nama_buah.append("jeruk")
# nama_buah.append("apel")
# nama_buah.append("sirsak")

# print(nama_buah)

# for buah in nama_buah:
#     print(buah)

# nama_buah.append("salak")