#Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine 
# quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.


idade=[]
altura=[]
media_altura=[]
apresentacao=[]
descarte=[]

def cal_media():
  calculo =  sum(altura)/len(altura)
  return calculo


for i in range (0,1):
  aux = cal_media()
  media_altura.append(aux)

for j in range(0,30):
  if idade[j] > 13 and altura[j] < media_altura[0]:
    apresentacao.append(j)
  else: 
    descarte.append(j)

print(len(apresentacao))  

#Programa testado com 5 alturas e idades!!!
    

