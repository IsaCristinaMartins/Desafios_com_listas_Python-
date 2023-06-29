# Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita uma
# grande quantidade de organizações:
print(f"Qual o melhor Sistema Operacional para uso em servidores?")
print(f"1- Windows Server")
print(f"2- Unix")
print(f"3- Linux")
print(f"4- Netware")
print(f"5- Mac OS")
print(f"6- Outro. ")


contador = [0] * 7
m=-1
porcentagem=[]

while m != 0:
    m = int (input(f"Digite o melhor sistema operacional, pra encerrar digite 0 "))
    if m == 0:
        break
    if m < 0 or m > 6:
        print (f"Você digitou uma opção errada")        
        continue
    elif m>=1 or m<=6:
        contador[m] += 1
        continue

def soma():
    aux2= sum(contador)  
    return aux2

def cal_porcentagem(v):
    calculo = [x/sum(v) for x in v]
    return calculo 

v = cal_porcentagem(contador)

for elem in v:
    print("{:.2f}%".format(100 * elem))
#print(f"{porcentagem}")