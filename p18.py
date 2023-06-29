# Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para 
# saber qual o melhor jogador após cada jogo. Para isto, faz-se necessário o desenvolvimento de um 
# programa, que será utilizado pelas telefonistas, para a computação dos votos. 
# Sua equipe foi contratada para desenvolver este programa, utilizando a 
# linguagem de programação C++. Para computar cada voto, a
# telefonista digitará um número, entre 1 e 23, correspondente ao número da camisa do 
# jogador. Um número de jogador igual zero, indica que a votação foi encerrada. 
# Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, 
# e voltando a pedir outro número. Após o final da votação, o programa deverá exibir:

contador = [0]*23
votos=0

while True:
    m = int (input(f"Digite o número do melhor jogador, pra encerrar digite 0  "))
    if m == 0:       
        break
    elif m < 0 or m > 23:
        print (f"Você digitou um número de camisa errado")        
        continue
    elif m>=1 or m<=23:    
        contador [m-1]+=1

def media():
    k=sum(contador)/len(contador)
    return k

def cal_porcentagem(v):
    calculo = [x/sum(v) for x in v]
    return calculo 

#print(f"{contador}")  --> print pra teste de leitura de votos.

print(f"Enquete: Quem foi o melhor jogador?")

#Aqui é a lista de votos que cada jogador recebeu
for h in range (0,23):
    print(f"Número de votos do jogador {h+1}º foi {contador[h]}")


#print (f"A média dos votos computados foram: {media()} votos")  --> teste de execução
print(f"Resultado da votação:")
print (f"Foram computados {sum(contador)} votos")  
print ("A porcentagem dos votos é: {:.2f}%".format(cal_porcentagem(contador)))  

