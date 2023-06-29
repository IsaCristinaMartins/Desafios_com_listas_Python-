# Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc).
# Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz 
# com um litro de combustível. Calcule e mostre:
# O modelo do carro mais econômico; 
# Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros
# e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela de exemplo. 
# O disposição das informações deve ser o mais próxima possível ao exemplo.
# Os dados são fictícios e podem mudar a cada execução do programa.

carros = ["Fusca", "GOL", "VECTRA", "PALIO", "SENTRA"]
consumo =[10, 12, 8, 11, 9]

quilometragem=-1
while True:
    quilometragem = int (input(f"Digite o valor da quilometragem"))
    break   

for k in range(0,5):
    print(
        f"O {carros[k]}, faz {consumo[k]} \
        por litro de gasolina. E para percorrer {quilometragem}, \
        vai precisar de {quilometragem/consumo[k]}"
    )