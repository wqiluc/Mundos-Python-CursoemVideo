#Faça um programa que leia um número qualquer e mostre o seu fatorial.

#Reslução:

from cores import(Negrito, Reset, AmareloClaro)
from math import factorial

numero = int(input(f"\n {Negrito}Digite um valor para analisarmos seu fatorial: {Reset}"))
constante = numero
fatorial = factorial(numero)

while fatorial:
    while constante > 0:
        print(constante , end=" ")
        constante -= 1

    print(f"\n {AmareloClaro}O fatorial do número: {numero} é = {factorial(numero)}{Reset}")
    break