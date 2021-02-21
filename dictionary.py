pelanggan = {
    "nama" : "Astuti",
    "umur" : 20
}

pelanggan_2 = {
    "nama" : "Joko",
    "umur" : 23
}
# print(pelanggan)

print("Nama : {}".format(pelanggan["nama"]))
print("Umur : {}".format(pelanggan["umur"]))

#change value of dictionary
pelanggan["umur"] = 21

#loop through dict
for x in pelanggan:
    print(x) #key
    print(pelanggan[x]) #value
    print(pelanggan_2[x])

daftar_pelanggan = []
daftar_pelanggan.append(pelanggan)
daftar_pelanggan.append(pelanggan_2)

print(daftar_pelanggan)

for pelanggan in daftar_pelanggan:
    print("Nama : {}".format(pelanggan['nama']))
    print("Umur : {}".format(pelanggan['umur']))