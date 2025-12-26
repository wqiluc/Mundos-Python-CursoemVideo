#Crie um programa que simule o funcionamento de um caixa eletrônico. 
#No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) 
# e o programa vai informar quantas cédulas de cada valor serão entregues. 

#OBS: considere que o caixa possui cédulas de:
# R$50, R$20, R$10 e R$1.

#Reslução:
acumulador_notade_50 = acumulador_notade_20 = acumulador_notade_10 = acumulador_notade_01 = 0

from cores import(Negrito,Reset, Vermelho,Verde)

while True:
    pergunta = str(input(f"\n {Negrito}Deseja continuar sacando? 💰 (S/N) {Reset}")).upper()
    if pergunta=="N":
        break
    while pergunta not in "SN":
        print(f"\n {Vermelho}VALOR INVÁLIDO!❌ digite um valor real{Reset} (em {Verde}R${Reset}) {Vermelho}pra sacar {Reset}")
        pergunta = str(input(f"\n {Negrito}Deseja continuar sacando? 💰 (S/N) {Reset}")).upper()
        continue
    saque = int(input(f"\n {Negrito}Digite um valor para sacar: {Reset}{Verde}R${Reset}{Negrito}{Reset}"))
    while saque<=0:
        print(f"\n {Vermelho}VALOR INVÁLIDO!❌ digite um valor real{Reset} (em {Verde}R${Reset}) {Vermelho}pra sacar {Reset}")
        saque = int(input(f"\n {Negrito}Digite um valor para sacar: {Reset}{Verde}R${Reset}{Negrito}{Reset}"))
        
    if saque >= 50:
        acumulador_notade_50 = saque // 50
        saque %= 50

    if saque >= 20:
        acumulador_notade_20 = saque // 20
        saque %= 20

    if saque >= 10:
        acumulador_notade_10 = saque // 10
        saque %= 10

    if saque >= 1:
        acumulador_notade_01 = saque

print(f"\n Cédulas de R$50:{Reset} {Verde}R$ {acumulador_notade_50}{Reset}")
print(f"\n Cédulas de R$20:{Reset} {Verde}R$ {acumulador_notade_20}{Reset}")
print(f"\n Cédulas de R$10:{Reset} {Verde}R$ {acumulador_notade_10}{Reset}")
print(f"\n Cédulas de R$1:{Reset} {Verde}R$ {acumulador_notade_01}{Reset}")
print(f"\n {Vermelho}Encerrando Sistema 💻❌ Obrigado por sacar! Volte sempre 😃💸 {Reset} \n")