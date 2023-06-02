# 5 -Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
#    Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

numeros_basico = []
num_impar = []
num_par = []

#Para captar os números e coloca-los no vetor
for i in range (0,20):
    j = int (input (f"Digite 20 números inteiros, {i+1}° número, e receberá a separação por ímpar e par"))
    numeros_basico.append(j)

#Para diferenciar par e coloca-los no vetor
for a in range (len(numeros_basico)):
    if numeros_basico[a] %2 == 0:
        num_par.append(numeros_basico[a])
  #O restante devem ser ímpares, coloca-los no vetor  
    else:         
        num_impar.append(numeros_basico[a])

#imprimir os 3 vetores
print(f"Esses são os números escolhidos: {numeros_basico}")
print(f"Esses são os números ímpares: {num_impar}")
print(f"Esses são os númeors pares: {num_par}")

    

