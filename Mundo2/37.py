#Escreva um programa em Python que leia um número inteiro qualquer 
# e peça para o usuário escolher qual será a base de conversão: 
# 1 para binário, 2 para octal e 3 para hexadecimal.

#Resolução:
from cores import(Negrito, Reset, Azul, MagentaClaro, AmareloClaro)


numerointeiro = int(input(f"\n{Negrito}Digite o número inteiro: {Reset}"))
print("""\n Para qual base você quer converter? \n
      1 - Binário; \n
      2 - Octal; e \n 
      3 - Hexadecimal.""")
opcao_escolha = int(input(f"\n {Negrito}Digite a base de conversão escolhida: {Reset}"))

if opcao_escolha == 1:
    print(f"\n {Azul}O número {numerointeiro} em Binário é = {bin(numerointeiro)}{Reset} \n")
if opcao_escolha == 2:
     print(f"{MagentaClaro}O número {numerointeiro} em Octal é = {oct(numerointeiro)}{Reset}")
if opcao_escolha == 3:
     print(f"{AmareloClaro}O número {numerointeiro} em Hexadecimal é = {hex(numerointeiro)}{Reset}")