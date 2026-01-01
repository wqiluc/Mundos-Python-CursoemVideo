#Faça um programa que tenha uma função chamada maior(), 
# que receba vários parâmetros com valores inteiros. 
#Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

#Reslução:
from cores import (Negrito,Reset)
from random import randint

def maior(valores):
    print(f"{Negrito}O maior aleatório escolhido entre eles é = {max(valores)}{Reset}")

numeros = [randint(1,1000)]
print(" \n")
print(f"{Negrito}Dos números escolhidos de 1-100...{Reset}")
maior(valores=numeros)
print(" \n")