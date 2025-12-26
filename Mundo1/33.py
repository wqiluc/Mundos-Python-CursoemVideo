#Faça um programa que leia três números diferentes
# e mostre qual é o maior e qual é o menor.

#Resolução:
from cores import(Reset, Negrito, Amarelo, Azul, MagentaClaro)
from time import sleep

valor1 = int(input(f"{Negrito}\n Digite o primeiro valor: {Reset}"))
valor2 = int(input(f"{Negrito}\n Digite o segundo valor: {Reset}"))
valor3 = int(input(f"{Negrito}\n Digite o terceiro valor: {Reset}"))

print(f"\n {MagentaClaro}Análisando os três valores.... {Reset} \n")
sleep(0.91)

maior = valor1
if valor1>valor2>valor3:
    print(f"{Azul}O maior valor é o {valor1} {Reset} \n")
    print(f"{Amarelo}O menor valor é o {valor2} {Reset}\n")
elif valor1>valor3>valor2:
    print(f"{Azul}O maior valor é o {valor1} {Reset} \n")
    print(f"{Amarelo}O menor valor é o {valor2} {Reset}\n")

maior = valor2
if valor2>valor1>valor3:
    print(f"{Azul}O maior valor é o {valor2} {Reset} \n")
    print(f"{Amarelo}O menor valor é o {valor3} {Reset} \n")
elif valor2>valor3>valor1:
    print(f"{Azul}O maior valor é o {valor2} {Reset} \n")
    print(f"{Amarelo}O menor valor é o {valor1} {Reset} \n")

maior = valor3
if valor3>valor2>valor1:
    print(f"{Azul}O maior valor é o {valor3} {Reset} \n")
    print(f"{Amarelo}O menor valor é o {valor1} {Reset} \n")
elif valor3>valor1>valor2:
    print(f"{Azul}O maior valor é o {valor3} {Reset} \n")
    print(f"{Amarelo}O menor valor é o {valor2} {Reset} \n")