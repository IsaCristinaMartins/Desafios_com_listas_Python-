# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. 
# Imprima a idade e a altura na ordem inversa a ordem lida.

idade=[]
altura=[]


for i in range (0,5):
    aux = int (input(f"Coloque a idade da {i+1}° pessoa"))
    idade.append(aux)
    aux2 = int (input(f"Agora, coloque a altura da {i+1}° pessoa"))
    altura.append(aux2)

print(f"As idades no modo inverso são {idade[::-1]}")
print(f"As alturas no modo inverso são {altura[::-1]}")
