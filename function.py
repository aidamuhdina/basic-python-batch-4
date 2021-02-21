def my_function():
    print("Halo semua")

#my_function()

#function with parameter
def halo(first_name, last_name):
    print("Halo "+first_name + " "+last_name)


# halo("nana","karima")
# halo("raditya","dika")
# halo("Aida","Muhdina")

#function with default parameter
def hai(first_name, last_name=""):
    print("Halo "+first_name + " "+last_name)

#hai("nana")

def my_function2(child3, child2, child1):
    print("The youngest child is "+child3)


# my_function2(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
# my_function2("Emil", "Tobias", "Linus")

#function return value
def tambah(x, y):
    tambah = x + y
    return tambah


jumlah = tambah(2,9)
print(jumlah)

def total():
    return 20


totals = total()
print(totals)