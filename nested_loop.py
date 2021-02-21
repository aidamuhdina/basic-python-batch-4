# for i in range(2):
#     print("i: {}".format(i))
#     for j in range(4):
#         print("j: {}".format(j))
#     print('------')

for baris in range(5):
    for kolom in range(5):
        print("{}.{}".format(baris+1,kolom+1),end=" ")
        #end = pembatas biar print kesamping, gak kebawah
    print()