# 6- Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor 
#      a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

#Pedir 4 notas de 10 alunos e armazenar no vetor
alunoi = []

j = 0
for i in range (0,10): #aqui diz respeito a qnt de alunos (são 10)
    aux2 = []
    for a in range(0,4): #aqui diz respeito a qnt de nota
        aux = int (input(f"Digite a {a+1}° notas do aluno"))
        aux2.append(j + 1)
        j += 1
    alunoi.append(aux2)
  
# Cada aluno calcular a média e armazenar no vetor

def cal_media(i):
    calculo =  sum(alunoi[i])/len(alunoi[i])
    return calculo

c=0
media = []
for b in range(0, 10):    
    valor = cal_media(b)
    media.append(valor)

#imprima o número de alunos com média maior ou igual a 7.0.
# percorrer o vetor atrás de nota maior que 7 e contar quantos tem 
passou = []
reprovou =[]
for b in media:    
    if b >=7:
      passou.append(b)
    else: 
      reprovou.append(b)

qnt = len(passou)

print(f"{qnt} alunos tiveram a média maior ou igual a 7")