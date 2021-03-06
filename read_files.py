r = open("resource/hello.txt","r")

#print(r.read())

temp2 = r.readlines()
#print(temp2)
a = []
for li in temp2:
    a.append(li.strip())

print(a)
r.close()