#Faça um programa que leia o peso de cinco pessoas. 
#No final, mostre qual foi o maior e o menor peso lidos.

#Reslução:
from cores import(Negrito, Reset, Azul, AmareloClaro)

pesos_lista = []

for peso_pessoas in range(1, 6):
    peso = float(input(f"\n {Negrito}Digite o peso da {peso_pessoas}º pessoa: (Kg) "))
    pesos_lista.append(peso)

menorpessoa = min(pesos_lista)
maiorpessoa = max(pesos_lista)

print(f"\n {Azul}O menor peso lido foi: {menorpessoa} Kg{Reset}")
print(f"\n {AmareloClaro}O maior peso lido foi: {maiorpessoa} Kg{Reset}")
