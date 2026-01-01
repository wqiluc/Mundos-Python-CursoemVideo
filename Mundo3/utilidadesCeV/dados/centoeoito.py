#Adapte o código do desafio 107.py, 
# criando uma função adicional chamada 
# moeda() que consiga mostrar os números como um valor monetário formatado.

#Reslução:
from ..cores import Negrito, Reset, Verde, Magenta
from ..moeda import centoeoitomoeda


valor = centoeoitomoeda.leiadinheiro()

print(
    f"\n {Negrito}Aumento: {Reset}"
    f"O aumento de: {Magenta}R${valor:.2f}{Reset} é = "
    f"{Verde}R${centoeoitomoeda.aumentar(valor):.2f}{Reset}: "
    f"{Magenta}{valor}{Reset} + {Verde}{valor}{Reset}")
print(
    f"\n {Negrito}Diminuição: {Reset}"
    f"uma Diminuição de: {Magenta}R${valor:.2f}{Reset} é = "
    f"{Verde}R${centoeoitomoeda.diminuir(valor):.2f}{Reset}: "
    f"{Magenta}{valor}{Reset} - {Verde}{valor}{Reset}")
print(
    f"\n {Negrito}Metade: {Reset}"
    f"a Metade de: {Magenta}R${valor:.2f}{Reset} é = "
    f"{Verde}R${centoeoitomoeda.metade(valor):.2f}{Reset}: "
    f"{Magenta}{valor}{Reset} / {Verde}2{Reset}")
print(
    f"\n {Negrito}Dobro: {Reset}"
    f"o Dobro de: {Magenta}R${valor:.2f}{Reset} é = "
    f"{Verde}R${centoeoitomoeda.dobrar(valor):.2f}{Reset}: "
    f"{Magenta}{valor}{Reset} * {Verde}2{Reset}")