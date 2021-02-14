a = int(input("Angka pertama : "))
b = int(input("Angka kedua : "))

if a>b:
    print("{} lebih besar daripada {}".format(a,b))
elif a==b:
     print("{} sama dengan {}".format(a,b))  
else:
    print("{} kurang dari {}".format(a,b))

num = int(input("Angka : "))
if num % 2 == 0:
    print("Angka {} adalah bilangan genap".format(num))
else:
    print("Angka {} adalah bilangan ganjil".format(num))