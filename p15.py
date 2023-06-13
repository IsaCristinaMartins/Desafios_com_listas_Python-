# Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser
#armazenado). Após esta entrada de dados, faça: 
#Mostre a quantidade de valores que foram lidos;
#Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
#Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
#Calcule e mostre a soma dos valores;
#Calcule e mostre a média dos valores;
#Calcule e mostre a quantidade de valores acima da média calculada;
#Calcule e mostre a quantidade de valores abaixo de sete;
#Encerre o programa com uma mensagem;

nota=[]
acima_media=[]
soma=[]
media= 0
menor_qsete=[]
descarte=[]
aux = 0

while aux != -1:
    aux= int(input(f"Vai digitando as notas aí... Quando não quiser mais, coloca -1."))
    if aux >= 0:
        nota.append(aux)
    elif aux== -1:
        print(f"Pronto, você não poderá adicionar mais notas")
        break

def cal_soma():
    aux2= sum(nota)  
    return aux2

def cal_media():
    aux3= sum(nota)/len(nota)
    return aux3


asoma = cal_soma()
soma.append(asoma)
media = cal_media()

#valores acima da média
for h in range(0, len(nota)):
   
    if nota[h] > media:
        acima_media.append(nota[h])
    else:
        descarte.append(nota[h])

#valores abaixo de 7
for k in range (len(nota)):
    if nota[k]<7:
        menor_qsete.append(nota[k])
    else:
        descarte.append(nota[h])

        
# Mostre a quantidade de valores que foram lidos;
print(f"Essa é a quanitdade de valores que foram lidos {len(nota)}")

#Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
print(f"Essa é a ordem que as notas foram adicionadas: {nota}")

#Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
for k in range(0,len(nota)):
    print(f"Essa é a ordem inversa que as notas foram adicionadas, e posicionadas uma embaixo da outra: {nota[::-1]}")

#Calcule e mostre a quantidade de valores acima da média calculada;
print(f"Esses são os valores a cima da média {len(acima_media)} e esses foram os valores {acima_media}")

#Calcule e mostre a quantidade de valores abaixo de sete;
print(f"Esses são os valores abaixo de sete: {len(menor_qsete)}")

#Encerre o programa com uma mensagem;
print(f"Isso é tudo pessoal. FIM")

