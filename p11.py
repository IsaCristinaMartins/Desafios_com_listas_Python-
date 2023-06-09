# Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b=[11, 22, 33, 44, 55, 66, 77, 88, 99, 12]
c=[111, 222, 333, 444, 555, 666, 777, 888, 999, 191]
d=[]

for i in range (0,10):
    d.append(a[i])
    d.append(b[i])
    d.append(c[i])
print(d)