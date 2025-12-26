#Crie um programa que leia números inteiros pelo teclado. 
#O programa só vai parar quando o usuário digitar o valor 999, 
# que é a condição de parada. 
#No final, mostre quantos números foram digitados 
# e qual foi a soma entre elas (desconsiderando o flag).

#Reslução:
numero = 0
soma = 0
from cores import(Negrito,Reset, Amarelo)
while True:
    numero = int(input(f"\n {Negrito}Digite um número: {Reset}"))
    if (numero == 999):
        break
    soma+=numero
print(f"\n {Amarelo}A soma dos valores é = {soma}{Reset}")