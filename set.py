my_set = {"apel", "manggis", "pisang"}
#set gabisa di indeks karna ke acak terus urutannya
print(type(my_set))

a = set() #untuk inisiasi set kosong
print(type(a))

for x in my_set:
    print(x)


print("apel" in my_set)
print("melon" in my_set)

my_set.add("melon")
print(my_set)

my_set.remove("manggis")
print(my_set)

my_set2 = {1, 2, 3, 4, 5, 1, 4}
print(my_set2)

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(A|B) #buat gabung data
print(A & B) #buat irisan (data yg sama apa aja)
print(A - B)