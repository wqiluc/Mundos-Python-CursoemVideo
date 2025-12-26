#Faça um programa que leia o sexo de uma pessoa, m
# as só aceite os valores ‘M’ ou ‘F’. 
#Caso esteja errado, peça a digitação novamente até ter um valor correto.

#Reslução:
from cores import(Negrito, Reset, Vermelho, Magenta, Amarelo)
from time import sleep

sexo = str(input(f"\n {Negrito}Digite o seu sexo: (M/F) {Reset}")).upper()
print(f"\n {Amarelo} carregando{Reset} {Vermelho} . . . {Reset}\n ")
sleep(0.8)
if sexo=="M" or sexo=="F":
        print(f"\n{Magenta} Sexo do usuário = {sexo}")
        exit()
while sexo not in ("MF"):
    print(f"\n {Vermelho} Sexo inválido. Digite novamente. (APENAS M/F)")
    sexo = str(input(f"\n {Negrito}Digite o seu sexo: (M/F) {Reset}")).upper()
    print(f"\n {Amarelo} carregando{Reset} {Vermelho} . . . {Reset}\n ")
    sleep(0.8)
    if sexo=="M" or sexo=="F":
        print(f"\n{Magenta} Sexo do usuário = {sexo}")
        break