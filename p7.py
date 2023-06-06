# Faça um Programa que leia um vetor de 5 
# números inteiros, mostre a soma, a multiplicação e os números.
num = []

for i in range(0,5):
    aux = int(input(f"Digite 5 números e receba a soma, mutiplicação deles. {i+1}º número"))
    num.append(aux)

def calculos():
    soma = sum(num)
    return soma

def multiplicacao(i):
    calculo = (num[i] * num[i+1])
    return calculo

p=1
for b in range (0,5):
   p = p * num[b]

print(p)
 



   
  





