#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
#Depois disso, mostre a listagem de números gerados 
# e também indique o menor e o maior valor que estão na tupla.


#Reslução:
from cores import(Negrito, Reset, Vermelho, Amarelo, Azul, Magenta)

numero = str(input(F"\n {Negrito}Digite o 1º número: {Reset}"))
while not numero.isdigit():
    print(f"{Vermelho}Valor inválido!! necessário ser número{Reset}")
    numero = str(input(F"\n {Negrito}Digite o 1º número: {Reset}"))

numero2 = str(input(F"\n {Negrito}Digite o 2º número: {Reset}"))
while not numero2.isdigit():
    print(f"{Vermelho}Valor inválido!! necessário ser número{Reset}")
    numero2 = str(input(F"\n {Negrito}Digite o 2º número: {Reset}"))

numero3 = str(input(F"\n {Negrito}Digite o 3º número: {Reset}"))
while not numero3.isdigit():
    print(f"{Vermelho}Valor inválido!! necessário ser número{Reset}")
    numero3 = str(input(F"\n {Negrito}Digite o 3º número: {Reset}"))

numero4 = str(input(F"\n {Negrito}Digite o 4º número: {Reset}"))
while not numero4.isdigit():
    print(f"{Vermelho}Valor inválido!! necessário ser número{Reset}")
    numero4 = str(input(F"\n {Negrito}Digite o 4º número: {Reset}"))

numero5 = str(input(F"\n {Negrito}Digite o 5º número: {Reset}"))
while not numero5.isdigit():
    print(f"{Vermelho}Valor inválido!! necessário ser número{Reset}")
    numero5 = str(input(F"\n {Negrito}Digite o 5º número: {Reset}"))

numeros = (numero, numero2, numero3, numero4, numero5)
inteiros = int(numeros)
tupla = (numeros)

print(f"\n {Magenta}{tupla}{Reset}")
print(f"\n {Amarelo}Menor número = {(min(tupla))}{Reset}")
print(f"{Azul}Maior número = {(max(tupla))}{Reset} \n")