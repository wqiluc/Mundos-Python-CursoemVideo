#Refaça o DESAFIO 51.py, 
# lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão 
# usando a estrutura while.

#Reslução:
from cores import(Negrito, Reset)


numero = int(input(f"\n {Negrito}Digite o 1º termo da P.A: {Reset}"))
razao = int(input(f"\n {Negrito}Digite a razão da P.A: {Reset}"))

termo = numero
acumulador_casa = 1

while acumulador_casa <= 10:
    print(f"{termo}", end=" --> ")
    termo += razao
    acumulador_casa += 1
print("fim", end=" ")




  