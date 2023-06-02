#Faça um Programa que leia 4 notas, mostre as notas e a média na tela. 

vetorResposta = []

for i in range (0,4):
    nota = int(input(f"Digite a {i+1}° nota"))
    vetorResposta.append(nota)
print(f"As notas foram: {vetorResposta[0]}, {vetorResposta[1]}, {vetorResposta[2]}, {vetorResposta[3]}")
print(f"A média das notas foram {(vetorResposta[0] + vetorResposta[1] + vetorResposta[2] + vetorResposta[3]) / len(vetorResposta)}")