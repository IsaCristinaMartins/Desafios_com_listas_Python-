# 4- Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes. 
palavra = []
vogais = []
consoantes = []

#Pedir palavra e armazenar em vetor
for i in range (1):
    a = str (input(f"Digite uma palavra que contenha, no máximo, 10 letras")) 
    palavra.append(a) 

#Analisar cada letra e sua semelhança com vogais. Vogais vai pro vetor vogal, consoante vetor consoante.  
    for b in a:
        if b == "a" or b =="e" or b == "i" or b =="o" or b== "u":
            vogais.append(b)
        else: 
            consoantes.append(b)
        

print(len(consoantes))
print(consoantes)