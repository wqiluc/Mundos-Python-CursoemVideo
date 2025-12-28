#Crie um programa que vai ler vários números e colocar em uma lista.  Depois disso, mostre:                
# A) Quantos números foram digitados.  
# B) A lista de valores, ordenada de forma decrescente. 
# C) Se o valor 5 foi digitado e está ou não na lista.

#Reslução:
from cores import(Negrito, Reset, Verde, Vermelho, Amarelo)
lista_valores = [ ]

while True:
    numero = int(input(f"\n {Negrito}Digite um número: {Reset}"))
    if numero not in lista_valores:
        print(f"{Verde} Valor adicionado! ✅ 🖖 {Reset}")
        lista_valores.append(numero)
    else:
        print(f"\n {Vermelho}VALORES DUPLICADOS! ❌{Reset}")
    opcao = str(input(f" {Negrito}quer continuar adicionando? [S / N] {Reset}")).upper()
    while opcao not in "SN":
        print(f"\n {Vermelho} TERMO INVÁLIDO! Digite APENAS S/N {Reset}")
        opcao = str(input(f" {Negrito}quer continuar adicionando? [S / N] {Reset}")).upper()
    if opcao=="N":
        break

print(f"\n {Amarelo}Termos na lista = {len(lista_valores)} {Reset}")
lista_valores.reverse
print(f"\n {Amarelo}Lista decrescente = {lista_valores.sort(reverse=True)} {Reset}")
if 5 in lista_valores:
    print(f"\n {Verde}O 5 ESTÁ presente na lista! ✅{Reset}")
else:
    print(f"\n {Vermelho}O 5 ESTÁ FORA da lista! ❌{Reset}")