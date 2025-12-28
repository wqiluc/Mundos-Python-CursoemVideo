#Faça um programa que leia nome e peso de várias pessoas, 
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas;
# B) A lista de pessoas mais pesadas; e
# C) A lista de pessoas mais leves.

#Reslução:
from cores import(Negrito,Reset,Amarelo,Azul, Vermelho)
info_pessoas = [ ]

while True:
    nome = str(input(f"\n {Negrito}Digite o nome da pessoa: {Reset}")).upper().strip()
    while not nome.isalpha():
        print(f"{Vermelho}Termo Inválido!! ❌ Digite UM NOME (string){Reset}")
        nome = str(input(f"\n {Negrito}Digite o nome da pessoa: {Reset}")).upper().strip()
    peso = str(input(f"\n {Negrito}Digite o peso - (Kg): {Reset}"))
    while not peso.replace(".", "").isdigit():
        print(f"{Vermelho}Termo Inválido!! ❌ Digite O PESO (float){Reset}")
        peso = str(input(f"\n {Negrito}Digite o peso - (Kg): {Reset}"))
    peso = float(peso)

    info_pessoas.append([nome, peso])

    opcao = str(input(f"\n {Negrito}Deseja Continuar? [S / N] {Reset}")).upper()
    while opcao not in "SN":
         print(f"{Vermelho}Termo Inválido!! ❌ Digite APENAS [S / N] {Reset}")
         opcao = str(input(f"{Negrito}Deseja Continuar? [S / N] {Reset}")).upper()
    if opcao=="N":
        break
    else:
        continue

menor_peso = min(peso[1] for peso in info_pessoas)
maximo_peso = max(peso[1] for peso in info_pessoas)

print(f"\n {Amarelo} {len(info_pessoas)} Pessoa(as) foi(foram) cadastrada(as) {Reset}")
print(f"{Azul} Pessoa mais leve = {menor_peso:.2f}Kg  {Reset}")
for peso in info_pessoas:
    if peso[1] == menor_peso:
        print(f" - {peso[0]}")
print(f"{Azul} Pessoa mais pesada = {maximo_peso:.2f}Kg {Reset}")
for peso in info_pessoas:
    if peso[1] == maximo_peso:
        print(f" - {peso[0]}")