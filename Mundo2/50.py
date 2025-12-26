#Desenvolva um programa que leia seis números inteiros 
# e mostre a soma apenas daqueles que forem pares. 
# Se o valor digitado for ímpar, desconsidere-o.

#Reslução:
soma = 0
cont = 0
from cores import(Negrito, Reset, MagentaClaro)


for analise in range(1,7):
    numero = int(input(f"\n {Negrito} Digite o número: {Reset}"))
    if numero%2 == 0:
        soma+=numero
        cont+=1
print(f"\n {MagentaClaro}A soma dos valores PARES é = {soma}{Reset}")