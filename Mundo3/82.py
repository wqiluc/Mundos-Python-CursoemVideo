#Crie um programa que vai ler vários números e colocar em uma lista. 
# depois disso, crie duas listas extras que vão conter apenas os valores 
# pares e os valores ímpares digitados, respectivamente. 
#Ao final, mostre o conteúdo das três listas geradas.

#Reslução:
from cores import(Negrito,Reset,Verde,Vermelho, Amarelo)
lista_geral = [ ]
lista_par = [ ]
lista_impar = [ ]

while True:
    numero = int(input(f"\n {Negrito}Digite um número: {Reset}"))
    if numero not in lista_geral:
        lista_geral.append(numero)
        print(f"\n {Verde}Número adicionado! ✅{Reset}")
    else:
        print(f"{Vermelho}Número já adicionado! ❌ Duplicado. . .{Reset}")
        if numero % 2 == 0:
            lista_par.append(numero)
        else:
            lista_impar.append(numero)
    opcao = str(input(f"\n {Negrito}Deseja continuar? [S / N] {Reset}")).upper()
    while not opcao in "SN":
        print(f"\n {Vermelho}Termo Inválido!! Digite apenas [S / N]{Reset}")
        opcao = str(input(f"\n {Negrito}Deseja continuar? [S / N] {Reset}")).upper()
    if (opcao=="N"):
        break

print(f"\n {Amarelo}Lista geral = {lista_geral}{Reset}")
print(f"\n {Amarelo}Lista Par = {lista_par}{Reset}")
print(f"\n {Amarelo}Lista Ímpar = {lista_impar}{Reset}")