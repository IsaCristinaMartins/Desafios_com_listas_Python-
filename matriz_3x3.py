# Fazer matriz 3x3 com 1 ou 2 for  com contador de 1 a 8

matriz = []
j = 0
for i in range (0,3):
    aux = []
    for a in range(0,3):
      aux.append(j + 1)
      j += 1
    matriz.append(aux)    
print(matriz)
