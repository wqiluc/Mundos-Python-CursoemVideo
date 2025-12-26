#Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final, mostre quantas pessoas ainda não atingiram a maioridade 
# e quantas já são maiores.

#Reslução:
acumulador_maioridade = 0
acumulador_menoridade = 0

from cores import(Negrito, Reset, Vermelho, Verde, Magenta, Azul, Amarelo)
from datetime import datetime
from time import sleep

maioridade = datetime.today().year - 18

print("\n", f"{Amarelo}==={Reset}"*20)
print(f"\n {Azul}GRUPO DE 7 PESSOAS{Reset}")
print("\n", f"{Amarelo}==={Reset}"*20)

for pessoas in range(1,8):
    ano = int(input(f"\n {Negrito}Em que ano a {pessoas}º pessoa nasceu? {Reset}"))
    if ano>=maioridade:
        acumulador_menoridade+=1
    else:
        acumulador_maioridade+=1
print(f"\n {Magenta} Análisando as idades... {Reset}")
sleep(2)

print(f"\n {Verde}Há {acumulador_maioridade} pessoas maiores de idade{Reset} \n")
print(f"\n {Vermelho}Há {acumulador_menoridade} pessoas menores de idade{Reset} \n")