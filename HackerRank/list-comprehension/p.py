
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))
n = int(input("n: "))
clist = []
lx = []
ly = []
lz = []

for i in range(x+1):
    lx.append(i)
for j in range(y+1):
    ly.append(j)
for k in range(z+1):
    lz.append(k)
print(lz, ly, lz)

for i in lx:
    for j in ly:
        for k in lz:
            ls = [i, j, k]
            clist.append(ls)
flist = []            
print(clist)
for x in clist:
    if x[0] + x[1] + x[2] != n:
        flist.append(x)
print(flist)