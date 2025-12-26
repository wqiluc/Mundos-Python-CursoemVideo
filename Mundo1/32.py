#Faça um programa que leia um ano qualquer 
# e mostre se ele é bissexto ou não.

#Resolução:

from time import sleep
from cores import (Negrito, Reset, Vermelho, Verde, Magenta)
from datetime import date

ano = int(input(f"\n {Negrito} Que ano você quer análisar? {Reset}"))
if ano == 0:
   ano = date.today().year

print(f"\n {Magenta} Análisando o ano de {ano}...{Reset} \n")

sleep(0.8)

if ano%4==0 and ano%100!=0 or ano%400==0:
    print(f"\n {Verde}É UM ANO BISSEXTO ✅📅{Reset} \n")
else:
    print(f"\n {Vermelho}NÃO É BISSEXTO❌📅{Reset} \n")

   