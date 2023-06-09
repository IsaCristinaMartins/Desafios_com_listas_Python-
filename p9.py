#Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
novoa=[]
elementos=[]
                       
#calculando o quadrado dos números          
def quadrado(i):
    quad = (a[i]) * (a[i])
    return quad 

#looping para realizar o calculo de cada número no vetor 
for i in range (0,10):
    contagem = quadrado(i)
    novoa.append(contagem)

#calulando a soma dos números que foram elevados ao quadrado 

def calsoma(h):
    soma = sum(novoa) 
    return soma

for h in range(0,1):
    aux2 = calsoma(h)
    elementos.append(aux2)
    




print(f"esse é o vetor dos quadrados: {novoa}")
print(f"Esse é o vetor da soma dos quadrados dos elementos do vetor {elementos}")