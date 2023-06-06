#1 - Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

print("Ola, você irá digitar 5 números inteiros aleatórios")



vetorResposta=[]

for i in range (0,5):
    aux = int (input (f"Digite o {i+1}° número:"))
    vetorResposta.append(aux)

print(f"Os números no modo inverso são {vetorResposta[::-1]}")