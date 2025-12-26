#Melhore o DESAFIO 61.py, 
# perguntando para o usuário se ele quer mostrar mais alguns termos. 
#O programa encerrará quando ele disser que quer mostrar 0 termos.

#Reslução:
from cores import(Negrito, Reset, Vermelho)


numero = int(input(f"\n {Negrito}Digite o 1º termo da P.A: {Reset}"))
razao = int(input(f"\n {Negrito}Digite a razão da P.A: {Reset}"))

termo = numero
acumulador_casa = 1

while acumulador_casa <= 10:
    print(f"{termo}", end=" --> ")
    termo += razao
    acumulador_casa += 1
print("fim", end=" ")

opcao = int(input(f"\n {Negrito}Deseja mostrar mais termos? (1 - S/ 2 - N) {Reset}"))
novas_casas = 0

while opcao == 1:
    casas = int(input(f"\n {Negrito} Quantas casas quer mostrar ? {Reset}"))
    contador = 0
    while contador < casas:
        termo += razao
        print(f"{termo}", end=" --> ")
        contador += 1
        novas_casas += 1
    opcao = int(input(f"\n {Negrito}Deseja mostrar mais termos? (1 - S/ 2 - N) {Reset}"))

while opcao == 2:
    print(f"\n {Vermelho} Encerrando o Programa ... {Reset}")
    print(f"\n {Negrito}Total de casas mostradas: {novas_casas}{Reset}")
    break



