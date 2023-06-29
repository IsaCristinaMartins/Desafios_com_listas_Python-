# Faça um programa que simule um lançamento de dados. 
# Lance o dado 100 vezes e armazene os resultados em um vetor .
# Depois, mostre quantas vezes cada valor foi conseguido. 
# Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios,
# simulando os lançamentos dos dados.
import random 


numeros = [1, 2, 3, 4, 5, 6]
m=0
dados=[]
contagem=[0, 0, 0, 0, 0, 0]

while m<=100:
   n = random.choice(numeros)
   dados.append(n)
   m+=1

for k in range (0,99):
    contagem [dados[k] - 1] +=1
      
print (dados)
print (contagem)
   


