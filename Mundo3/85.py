#Crie um programa onde o usuário possa digitar sete valores numéricos e 
# cadastre-os em uma lista única que mantenha separados os valores 
# pares e ímpares. 
#No final, 
# mostre os valores pares e ímpares em ordem crescente.

#Reslução:
from cores import(Negrito,Reset,Vermelho,Verde, Magenta)
numeros_lista = [ ]
pares = [ ]
impares = [ ]

for sequencia in range(1,8):
        numero = str(input(f"\n {Negrito}Digite o {sequencia}º número: {Reset}"))
        while not numero.isdigit():
          print(f"\n {Vermelho}Termo Inválido. Digite apenas NÚMEROS (int) {Reset}") 
          numero = str(input(f"\n {Negrito}Digite o {sequencia}º número: {Reset}"))
        numero = int(numero)
        if numero not in numeros_lista:
            print(f"\n {Verde}Número {numero} adicionado a lista! ✅ {Reset}")
            numeros_lista.append(numero)
        else:
            print(f"\n {Vermelho}Termo Duplicado! ❌ Digite apenas números inteiros! {Reset}")
            print(f"\n {Vermelho} Encerrando . . . {Reset}")
            numeros_lista.clear()
            break
        
for numero in numeros_lista:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f"\n {Magenta}Lista inteira = {numeros_lista}{Reset}")
print(f"\n {Magenta}Lista dos números pares = {pares}{Reset}")
print(f"\n {Magenta}Lista dos números ímpares = {impares}{Reset}")