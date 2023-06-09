#Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20
# elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b=[11, 22, 33, 44, 55, 66, 77, 88, 99, 12]
c=[]

for i in range (0,10):
    c.append(a[i])
    c.append(b[i])
print(c)