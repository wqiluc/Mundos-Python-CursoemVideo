#Escreva um programa que leia um número N inteiro qualquer 
# e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 

#Reslução:
from cores import(Negrito, Reset)

quantidade_termos = int(input(f"\n {Negrito}Digite quantos termos da Sequência de Fibonacci deseja ver: {Reset}"))

termo_atual = 0
proximo_termo = 1
contador = 0

while contador < quantidade_termos:
    print(termo_atual, end=" ")
    termo_atual, proximo_termo = proximo_termo, termo_atual + proximo_termo
    contador += 1