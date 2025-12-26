#Crie um programa que leia a idade e o sexo de várias pessoas. 
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
# No final, mostre:

#A) quantas pessoas tem mais de 18 anos;
#B) quantos homens foram cadastrados; e
#C) quantas mulheres tem menos de 20 anos.

#Reslução:
from cores import (Negrito,Reset, Vermelho, Amarelo, MagentaClaro)
acumulador_pessoas_maisde18=0
acumulador_mulheres_20_oumenos = 0
acumulador_homens = 0

while True:
    opcao = str(input(f"\n {Negrito}Deseja cadastrar um usuário novo? (S / N) {Reset}")).upper()
    if opcao=="N":
        break
    idade = int(input(f"\n {Negrito}Digite a idade do usuário: {Reset}"))
    sexo = str(input(f"\n {Negrito}Digite o sexo do usuário: [M / F]{Reset}")).upper()
    if idade>18 and sexo == "M" or sexo=="F":
        acumulador_pessoas_maisde18+=1
    if idade<20 and sexo=="F":
        acumulador_mulheres_20_oumenos+=1
    if sexo=="M":
        acumulador_homens+=1

print(f"\n {Amarelo}Você registrou {acumulador_homens} homens {Negrito}")

print(f"\n {Amarelo}Você registrou {acumulador_mulheres_20_oumenos} mulheres (com menos de 20 anos){Negrito}")

print(f"\n {MagentaClaro}Você registrou {acumulador_pessoas_maisde18} pessoas com +18 anos{Negrito}")

print(f"\n {Vermelho}Encerrando o Sistema ... 💻❌{Reset}")