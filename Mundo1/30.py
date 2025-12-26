#Crie um programa que leia um número inteiro 
# e mostre na tela se ele é PAR ou ÍMPAR.

#Resolução:
from time import sleep
from cores import (
Negrito, Reset, AmareloClaro, Verde, Vermelho)


numero = int(input(f"{Negrito}\n Digite um número: {Reset}"))
print(f"{AmareloClaro} \n Análisando o número {numero}{Reset}...")

sleep(0.8)

if (numero%2==0):
    print(f"\n {Verde}É PAR!✅{Reset} \n")
else:
    print(f"\n {Vermelho}É ÍMPAR❌{Reset} \n")