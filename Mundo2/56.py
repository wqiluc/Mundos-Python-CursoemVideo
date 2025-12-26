#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
#No final do programa, mostre: 
# a média de idade do grupo, qual é o nome do homem mais velho 
# e quantas mulheres têm menos de 20 anos.

#Reslução:

acumulador_mulheres_menosde20 = 0
soma_idades = 0
maior_idade_homem = 0
nome_homem_maisvelho = " "

from cores import (Negrito, Reset, Magenta)

for info_pessoas in range(1,5):
    nome = str(input(f"\n {Negrito}Digite o nome da {info_pessoas}º Pessoa: ")).strip().upper()
    idades = int(input(f"\n {Negrito}Digite a idade da {info_pessoas}º Pessoa: "))
    soma_idades += idades
    sexo = str(input(f"\n {Negrito}Digite o sexo da {info_pessoas}º Pessoa: (M/F) ")).upper()

    if idades < 20 and sexo == "F":
        acumulador_mulheres_menosde20 += 1
    if sexo == "M" and idades > maior_idade_homem:
        maior_idade_homem = idades
        nome_homem_maisvelho = nome

media_idade = soma_idades / 4

print(f"\n {Magenta}A média das idades é: {media_idade:.2f}{Reset}")
print(f"{Negrito}Há {acumulador_mulheres_menosde20} mulheres com menos de 20 anos{Reset}")
print(f"{Negrito}O homem mais velho é {nome_homem_maisvelho} com {maior_idade_homem} anos{Reset} \n")