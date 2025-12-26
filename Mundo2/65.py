#Crie um programa que leia vários números inteiros pelo teclado. 
#No final da execução, mostre a média entre todos os valores e qual foi o maior 
# e o menor valores lidos. 
# O programa deve perguntar ao usuário se ele quer 
# ou não continuar a digitar valores.

#Reslução:
from cores import(Negrito,Reset)
soma_valores = add_valores = 0 

numero_incial = int(input(f"\n {Negrito}Digite um número: {Reset}"))
soma_valores = numero_incial
add_valores+=1

opcao = int(input(f"\n {Negrito}Deseja continuar? (1 - S / 2 - N)"))
while opcao!=2:
    numero_opcao = int(input(f"\n {Negrito}Digite um número: {Reset}"))
    soma_valores+=numero_opcao
    add_valores+=1
    opcao = int(input(f"\n {Negrito}Deseja continuar? (1 - S / 2 - N)"))
    continue

while opcao==2:
    numerosloop = (numero_incial, numero_opcao)
    media = (soma_valores / add_valores)

    print(f"\n {Negrito}Você adicionou {add_valores} valores{Reset}")
    print(f"{Negrito}A média entre esses {add_valores} valores é = {media}{Reset}")
    print(f"{Negrito} Menor valor = {min(numerosloop)}{Reset}")
    print(f"{Negrito} Maior valor = {max(numerosloop)}{Reset}")
    break