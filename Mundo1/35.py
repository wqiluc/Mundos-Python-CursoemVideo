#Desenvolva um programa que leia o comprimento de três retas 
# e diga ao usuário se elas podem ou não formar um triângulo.

#Resolução:
from cores import(Negrito, Reset, Vermelho, Verde, Amarelo)

segmento1 = float(input(f"\n {Negrito}Digite o Segmento 1: {Reset}"))
segmento2 = float(input(f"\n {Negrito}Digite o Segmento 2: {Reset}"))
segmento3 = float(input(f"\n {Negrito}Digite o Segmento 3: {Reset} "))

if segmento1<segmento2+segmento3 and segmento2<segmento1+segmento3 and segmento3<segmento1+segmento2:    
    print(f"\n {Verde}PODE formar um triângulo{Reset} \n")
else:    
    print(f"\n {Vermelho}NÃO PODE formar um  triângulo{Reset} \n")

