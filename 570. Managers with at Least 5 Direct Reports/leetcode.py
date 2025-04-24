n = 7
bina = []
for i in range(n+1):
     bina.append(str(bin(i)))
print(bina)
for j in bina:
    print(j)
    for k in range(len(j)):
        print(j[::])