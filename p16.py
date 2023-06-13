# Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas 
# vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 
# mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando um array de
# contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de
#    valores:
#    $200 - $299
#    $300 - $399
#    $400 - $499
#    $500 - $599
#    $600 - $699
#    $700 - $799
#    $800 - $899
#    $900 - $999
#    $1000 em diante

# salario = 200 + ((0,09(venda_semana)) 

comissao = 9 * [0]
venda_semana = 0

def salario(venda):
    pagamento = 200 + (0.09 * (venda))
    return pagamento

for i in range (0,10): #aqui diz respeito a qnt de vendedores (são 10)
    venda = int (input(f"Digite a venda da semana do {i + 1}° vendedor"))
    venda_semana = salario(venda)
    if venda_semana > 200 and venda_semana < 299:
        comissao[0] = comissao[0]>+1
    elif 300 < venda_semana < 399:
        comissao[1] +=1
    elif 400 < venda_semana <499:
        comissao[2] +=1
    elif 500 < venda_semana < 599:
        comissao[3]+=1
    elif 600 < venda_semana < 699:
        comissao[4]+=1
    elif 700< venda_semana < 799:
        comissao[5]+=1
    elif 800 < venda_semana < 899:
        comissao[6]+=1
    elif 900 < venda_semana < 999:
        comissao[7]+=1
    elif venda_semana >= 1000:
        comissao[8]+=1

print(f"{comissao[0]} vendedores receberam entre 200-299 reais,\
       {comissao[1]} vendedores receberam entre 300-399 reais, \
       {comissao[2]} vendedores receberam entre 400-499 reais, \
        {comissao[3]} vendedores receberam entre 500-599 reais,\
         {comissao[4]} vendedores receberam entre 600-699 reais,\
          {comissao[5]} vendedores receberam entre 700-799 reais,\
           {comissao[6]} vendedores receberam entre 800-899 reais,\
            {comissao[7]} vendedores receberam entre 900-999 reais e\
             {comissao[8]} vendedores receberam valor maior ou igual a 1.000")


