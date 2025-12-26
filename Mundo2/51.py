#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
#No final, mostre os 10 primeiros termos dessa progressão.

#Reslução:
from cores import(Negrito, Reset, Amarelo)

inicio = int(input(f"\n {Negrito}Digite o termo Inicial da PA: {Reset}"))
progressao = int(input(f"\n {Negrito}Digite a progressão dessa PA: {Reset}"))
casas = inicio + (10-1) * progressao

for PA in range(inicio, casas+progressao, progressao):
    print(f"{Amarelo}{PA} -> {Reset}", end=" ")
print("Acabou")