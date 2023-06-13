# Em uma competição de salto em distância cada atleta tem direito a cinco saltos. 
# O resultado do atleta será determinado pela média dos cinco valores restantes. 
# Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta 
# em seus saltos e depois informe o nome, os saltos e a média dos saltos. 
# O programa deve ser encerrado quando não for informado o nome do atleta.
# A saída do programa deve ser conforme o exemplo abaixo:

distancia=[]
nome = 0
media=[]
nome_atleta=[]

def media_atleta():
    m=sum(distancia)/len(distancia)
    return m

while True:
    nome = (str(input("Digite o nome do atleta:")))
    if nome == "":
        break
    nome_atleta.append(nome)
    for i in range (0,5):
        salto = (int(input(f"Digite o {i+1} salto do atleta {nome}")))
        distancia.append(salto)

print(f"Atleta: {nome_atleta}")
print(f"Primeiro salto: {distancia[0]}m")
print(f"Segundo salto: {distancia[1]}m")
print(f"Terceiro salto: {distancia[2]}m")
print(f"Quarto salto: {distancia[3]}m")
print(f"Quinto salto: {distancia[4]}m")

print(f"Resultado final:")
print(f"Atleta: {nome_atleta}")
print(f"Saltos: {distancia[0]} - {distancia[1]} - {distancia[2]} - {distancia[3]} - {distancia[4]} ")
print(f"Média dos saltos: {media_atleta()}m")









