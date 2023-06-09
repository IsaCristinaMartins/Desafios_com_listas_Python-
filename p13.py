# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
# Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média
# anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

temp_media_mensal=[]
temp_media_anual=[]
nome_mes=["1- Janeiro", "2- Fevereiro", "3- Março", "4- Abril", "5- Maio", "6- Junho", "7- Julho", "8-Agosto", "9-Setembro", "10-Outubro", "11-Novembro", "12- Dezembro"]

for i in range(0,12):
    aux= int(input(f"Digite a temperatura média de cada mês"))
    temp_media_mensal.append(aux)

def cal_media_temp(j):
    aux2 = sum(temp_media_mensal)/len(temp_media_mensal)
    return aux2

for j in range (0,1):
    aux3 = cal_media_temp(j)
    temp_media_anual.append(aux3)

for h in range (0,12):
    if (temp_media_mensal[h]) > (temp_media_anual[0]):
        print(f"Esse mês {nome_mes[h]} teve a temperatura acima da média anual")
    else: 
        None

print(f"A média das temperaturas anual foi: {temp_media_anual}")
