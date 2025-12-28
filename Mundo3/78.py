#Faça um programa que leia 5 valores numéricos 
# e guarde-os em uma lista. 
#No final, mostre qual foi 
# o maior e o menor valor digitado e as suas respectivas posições na lista.

#Reslução:
from cores import(Negrito, Reset, Azul, Amarelo)

numeros = [
    int(input(f"\n {Negrito}Digite o 1º valor: {Reset}")),
    int(input(f"\n {Negrito}Digite o 2º valor: {Reset}")),
    int(input(f"\n {Negrito}Digite o 3º valor: {Reset}")),
    int(input(f"\n {Negrito}Digite o 4º valor: {Reset}")),
    int(input(f"\n {Negrito}Digite o 5º valor: {Reset}"))]

print("\n",f"Lista = {numeros}", "\n")
print("\n", f"{Amarelo}" ,min(numeros), 
f"está na posição: {numeros.index(min(numeros))}{Reset}")
print("\n", f"{Azul}" ,max(numeros), 
f"está na posição: {numeros.index(max(numeros))}{Reset}")