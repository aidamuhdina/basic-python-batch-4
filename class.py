class MyClass:
    x = 5

obj1 = MyClass()
obj2 = MyClass()

# print(obj1.x)
# print(obj2.x)

class Person:
    def __init__(self, name, age): #dikelas, fungsi disebut method
        self.name = name #method pertama pakai __init__ trs
        self.age = age #atribut

    def greeting(self):
        print("Hello my name is " +self.name)


# nama = input("nama : ")
# umur = input("umur : ")
#p1 = Person(nama, umur)

p1 = Person("Juju", 20)
# print(p1.name)
# print(p1.age)
p1.greeting()

p2 = Person("gigi", 22)
p2.greeting


