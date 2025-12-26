#A Confederação Nacional de Natação precisa de um programa 
# que leia o ano de nascimento de um atleta e mostre 
# sua categoria, de acordo com a idade:#
#Até 9 anos: MIRIM;
#Até 14 anos: INFANTIL;
#Até 19 anos: JÚNIOR;
#Até 25 anos: SÊNIOR; e
#Acima de 25 anos: MASTER.

#Reslução:
from cores import(Negrito, Reset, Azul, CyanClaro)
from time import sleep
from datetime import datetime #datetime.today().year = ano atual do seu computador

ano = int(input(f"\n {Negrito} Digite o ano de nascimento do Atleta: {Reset}"))
idade = (datetime.today().year - ano)

print(f"\n {CyanClaro} Carregando ...{Reset} \n")
sleep(3)

if (ano==0):
    print(f"\n {Negrito} O Atleta tem meses de idade{Reset}")
    print(f"\n {Azul} Atleta = MIRIM {Reset} \n")
    exit()
if (idade!=0):
    if (idade<=9):
        print(f"\n {Negrito} O Atleta tem {idade} anos de idade{Reset} \n")
        print(f"\n {Azul} Atleta = MIRIM {Reset} \n")
    elif (idade>9 and idade<=14):
        print(f"\n {Negrito} O Atleta tem {idade} anos de idade{Reset} \n")
        print(f"\n {Azul} Atleta = INFANTIL {Reset} \n")
    elif (idade>14 and idade<=19):
        print(f"\n {Negrito} O Atleta tem {idade} anos de idade{Reset} \n")
        print(f"\n {Azul} Atleta = JUNIOR {Reset} \n")
    elif (idade>19 and idade<=25):
        print(f"\n {Negrito} O Atleta tem {idade} anos de idade{Reset} \n")
        print(f"\n {Azul} Atleta = SÊNIOR {Reset} \n")
    else:
        print(f"\n {Negrito} O Atleta tem {idade} anos de idade{Reset} \n")
        print(f"\n {Azul} Atleta = MASTER {Reset} \n")