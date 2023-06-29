# Foi requisitado que você desenvolva um programa para registrar este levantamento. 
# O programa deverá receber um número indeterminado de entradas, 
# cada uma contendo: um número de identificação do mouse o tipo de defeito:
# necessita da esfera; necessita de limpeza; a.necessita troca do cabo ou conector; 
# a.quebrado ou inutilizado Uma identificação igual a zero encerra o programa. 
# Ao final o programa deverá emitir o seguinte relatório:

print(f"Escolha a situação do mouse:")
print(f"Situação:")
print(f"1- necessita da esfera ")
print(f"2- necessita de limpeza ")
print(f"3- necessita troca do cabo ou conector")
print(f"4- quebrado ou inutilizado")

mouse=["1- necessita de esfera", "2- necessita de limpeza", "3-necessita troca do cabo ou conector", "4-quebrado ou inutilizado"]
contador=[0,0,0,0]
ops=0

while True:
    m = int(input(f"Escolha a opção..."))
    if m == 0:
        print(f"Programa encerrado")
        break
    elif m >= 1 and m <= 4:
        contador[m-1]+=1
        continue
    elif m >= 5:
        print(f"Número errado, escolha entre 1-4")
        continue

print (f"Foram analisados {sum(contador)} mouse")
print(contador)

for j in range(0,4):
    print(f"{contador[j]} mouses, {mouse[j]}")
