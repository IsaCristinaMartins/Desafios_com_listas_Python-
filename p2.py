# 2 -Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa. 

vetorResposta = []

for i in range (0,10):
    aux = int(input(f"Digite o {i+1}° número:"))
    vetorResposta.append(aux)
print(f"os números digitados foram {vetorResposta [::-1]}")

