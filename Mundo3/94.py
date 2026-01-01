#Crie um programa que leia nome, sexo e idade de várias pessoas, 
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
#No final, mostre: 
# A) Quantas pessoas foram cadastradas; ✅
# B) A média de idade; ✅
# C) Uma lista com as mulheres ✅; e 
# D) Uma lista de pessoas com idade acima da média.✅

#Reslução:
from cores import(Negrito,Reset,Azul,Vermelho,Amarelo)
info_pessoas = { }
pessoas = [ ]
mulheres = [ ]
acumulador_pessoas = 0
acumulador_idade = 0
soma_idade = 0

while True:
    nome = str(input(f"\n {Negrito}Digite o nome da pessoa: {Reset}")).upper().strip()
    acumulador_pessoas+=1
    gênero = str(input(f"\n {Negrito}Digite o gênero da pesoa: [M / F] {Reset}")).upper().strip()
    while gênero not in "MF":
        print(f"{Vermelho}Termo Inválido!!❌ Digite apenas [M / F]{Reset}")
        gênero = str(input(f"\n {Negrito}Digite o gênero da pesoa: [M / F] {Reset}")).upper().strip()
    idade = int(input(f"{Negrito}Digte a idade da pessoa: {Reset}"))
    soma_idade+=idade
    acumulador_idade+=1
    
    pessoas.append([nome,gênero,idade])
    
    if gênero == "F":
        mulheres.append(pessoas.copy())
        info_pessoas["mulheres"] = mulheres
        mulheres.append(pessoas.copy())
        print(f"\n {Amarelo}{pessoas.copy()}{Reset} \n")
    else:
        print(f"{Vermelho}HOMENS FORA DA LISTA ❌{Reset}")
        pessoas.clear() 
        continue
    opcao = str(input(f"{Negrito}Deseja continuar? [S / N]{Reset}")).upper().strip()
    while (opcao not in "SN"):
        print(f"{Vermelho}Termo Inválido!!❌ Digite apenas [S / N]{Reset}")
        opcao = str(input(f"{Negrito}Deseja continuar? [S / N]{Reset}")).upper().strip()
    if (opcao == "N"):
        break

media = soma_idade / acumulador_idade

print(f"\n {Negrito} Há um total de: {acumulador_pessoas} pessoa(as) registrada(as) {Reset}")
print(f"\n {Negrito}A média das idades do grupo é: {media}{Reset}")

for pessoas in pessoas:
     if pessoas[2] > media:
          print(f"\n{Amarelo}Pessoas com idade acima da média ({media:.2f}) 🌟 {Reset}")
          print(pessoas.copy())