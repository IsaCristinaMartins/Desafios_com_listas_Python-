# O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, 
# caso sejam necessários, de forma a agilizar a execução do programa. 
# A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita através de uma
# função separada, que será chamada pelo programa principal. 
# O cálculo do percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal.

# usuario=["Alexandre", "Anderson", "Antonio", "Carlos", "Cesar", "Rosemary"]
# espaco=[456123789, 1245698456, 123456456, 9125758, 987458, 789456125]

arquivo = open('./teste_p23_python.txt', 'r')
espaco=[]
mb=[]
nomes=[]
relatorio = []

for texto in arquivo.readlines():
    a = texto.split()
    espaco.append(int(a[1]))
    nomes.append(str(a[0]))
 

arquivo.close()
print(espaco)

def calculo(n):
    aux = (n)/(1024 * 1024)
    return aux

for i in range(0,6):
   c = calculo(espaco[i])
   mb.append(c)

print(mb)

for k in range (0,6):
    h = ("{} utilizou o espaço de {:.2f} MB".format(nomes[k], mb[k]))
    j = f"{nomes[k]} utilizou o espaço de {mb[k]:.2f} MB"
    relatorio.append(j)

print(relatorio)

with open("relatorio.txt", "w") as arquivo:
   for i in relatorio:
      arquivo.write(i + "\n")

arquivo.close()

