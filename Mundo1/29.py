#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, 
# mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite.

#Resolução:
from time import sleep
from cores import (
Negrito, Reset, MagentaClaro, Vermelho, Verde, AmareloClaro)

velocidade = int(input(f"\n{Negrito}\nDigite a velocidade do veículo(em Km/h): {Reset}"))
limitevelocidade = 80
multa = (velocidade-80) * 7
print(f"{MagentaClaro}\nAnálisando sua velocidade... 🏎️\n{Reset}")
sleep(1)
if velocidade<=limitevelocidade:
    print(f"{Verde}Tudo certo! Dirija com Segurança✅{Reset}\n")
else:
    print(f"{Vermelho} Limite de velocidade atingido. ❌⚠️{Reset} \n {AmareloClaro}Você sofrerá uma multa de: R${multa},00{Reset}\n")        