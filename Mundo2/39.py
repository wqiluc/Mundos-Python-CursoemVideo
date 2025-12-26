#Faça um programa que leia o ano de nascimento de um jovem e informe, 
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
# se é a hora exata de se alistar ou 
# se já passou do tempo do alistamento. 
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

#Reslução:
from cores import(Negrito, Reset, Verde, Vermelho, Magenta, Amarelo,CinzaClaro)
from datetime import datetime #datetime.today().year = ano atual do seu computador
from time import sleep

ano = int(input(f"\n {Negrito}Digite seu ano de nascimento: {Reset}"))
print(f"{Magenta}Análisando a situação do usuário...{Reset} \n")
sleep(2)
if (ano==0):
    datetime.today().year
    print(f"\n {Negrito}A pessoa que nasceu em: {Amarelo}{datetime.today().year}{Reset} fará seu alistamento em:{Reset} {Magenta}{datetime.today().year+18}{Reset} \n")
    print(f"\n {Vermelho}Menor de idade. Incapaz de se alistar.{Reset} \n {Vermelho}Situação: ❌{Reset} \n")
    exit()
if (ano!=0):
    print(f"\n {Negrito}A pessoa que nasceu em {ano}{Reset} tem {Verde}{datetime.today().year-ano} ano(s) de idade✅{Reset}")
    if(datetime.today().year-ano<18):
        print(f"\n {Vermelho}Menor de idade. Incapaz de se alistar. Situação: ❌{Reset} \n")
        exit()
    else:
        print(f"\n {Verde}Já possui os seus 18 anos ou mais!✅{Reset} {CinzaClaro}Alistamento:{Reset} {Verde}Já feito✅{Reset} {Amarelo}ou Pendente⚠️{Reset} \n")
opcao = int(input("Digite a situação do seu alistamento: ( 1 - Feito ✅/ 2 - Pendente ⚠️ ) "))
if (opcao==1):
    print(f"\n {Verde}Situação: ✅{Reset}\n ")
else:
    print(f"\n {Amarelo}Situação: ⚠️{Reset} \n")