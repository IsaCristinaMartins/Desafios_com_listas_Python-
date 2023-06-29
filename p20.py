# Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes do
# sindicato laboral, chegou-se a seguinte forma de cálculo:
# a.Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro; 
# a.O piso do abono será de 100 reais, isto é, aqueles funcionários cujo
# salário for muito baixo, recebem este valor mínimo; Neste momento, não se deve 
# ter nenhuma preocupação com colaboradores com tempo menor de casa, descontos, impostos 
# ou outras particularidades. Seu programa deverá permitir a digitação do salário de um número 
# indefinido (desconhecido) de salários. Um valor de salário igual a 0 (zero) encerra a digitação. 
# Após a entrada de todos os dados o programa deverá calcular o valor do abono concedido a cada colaborador,
# de acordo com a regra definida acima. Ao final, o programa deverá apresentar:

salario=[]
abono=0
m=-1
while True:
    m = int (input(f"Digite o valor do salário, pra encerrar digite 0 "))
    if m == 0:
        print (f"Encerrada digitação")
        break
    if m < 100:
        print (f"Funcionário com direito ao abono")
        aux1 = (m + 100) 
        salario.append(aux1) 
        abono += 1      
        continue
    elif m>=100:
        salario.append(m)
        continue

print(f"O salário de cada funcionário é: {salario}")
print(f"o número total de funcionário processados é: {len(salario)}")
print(f"O valor total a ser gasto é: {sum(salario)}")
print(f"o número de funcionário que recebeu abono foi: {abono}")
