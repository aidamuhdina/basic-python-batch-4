kontak = []

def tambah_kontak():
    nama = input("Nama : ")
    nomor = input("Nomor : ")
    kontak.append({"nama":nama, "nomor":nomor})
    print("Kontak berhasil ditambahkan.")

def list_kontak():
    print("\nDaftar Kontak:")
    for info in kontak:
        print("Nama : {}".format(info["nama"]))
        print("Nomor : {}\n".format(info["nomor"]))
    

print("Selamat datang!")
while True:
    print('''
    ---Menu---
    1. Daftar kontak
    2. Tambah kontak
    3. Keluar
    ''')
    perintah = input("Pilih menu : ")
    
    if perintah == "1":
        if kontak == []:
            print("Kontak kosong!")
        else:
            list_kontak()
    elif perintah == "2":
        tambah_kontak()
    elif perintah == "3":
        print("Program selesai, sampai jumpa!")
        break
    else:
        print("Menu tidak tersedia.")