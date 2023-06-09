#Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As  perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?" 
#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve
# ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Casocontrário, ele será classificado como "Inocente".

resposta_sim=[]
resposta_nao=[]
perguntas=[
    "Telefonou para a vítima?", 
    "Esteve no local do crime?", 
    "Mora perto da vítima?",
    "Devia para a vítima?", 
    "Já trabalhou com a vítima?"
    ]

for i in range(0,1):
    aux = str(input(f"Responda as seguintes afirmações para averiguação de sua participação no crime. As respostas serão avaliadas em sim (S) ou não (N). Pronto(a)? Resposta: S ou N"))
    if aux == "s":
        print(f"Ok, vamos ás perguntas. Responda (S) para sim ou (N para não)")
    else: 
        print(f"Tudo bem, retorne quando estiver pronto(a)")
        exit()
        
for j in range(0,5):
    aux1 = str(input({perguntas[j]}))
    if aux1 == "s":
        resposta_sim.append(aux1)
    else:       
        resposta_nao.append(aux1)

if len(resposta_sim) == 2:
    print(f"Você foi considerada uma pessoa suspeita! Fica esperto!")
elif len(resposta_sim) == 3 or len(resposta_sim) == 4:
    print(f"Você foi considerado(a) Cúmplice! Vamos te pegar!")
elif len(resposta_sim) == 5:
    print(f"Você foi considerad0(a) o Assassino!! Seu bandindinho safado, eu tenho seu CPF!")
else: 
    print(f"Você só tava no canto errado na hora errada mas, se liga e melhore!")
            

