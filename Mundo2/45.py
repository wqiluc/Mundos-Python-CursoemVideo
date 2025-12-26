#Crie um programa que faça o computador jogar Jokenpô com você.

#Reslução:
from cores import (Negrito, Reset, Verde, Vermelho, MagentaClaro, Azul)
from random import choice
from time import sleep

print("\n", "="*20)
print(f"\n {MagentaClaro}JO-KEN-PÔ em Python 🐍{Reset}")
print("\n", "="*20)

print("""
    1 - Pedra 🪨
    2 - Papel 📄
    3 - Tesoura ✂️""")

opcaojogador = int(input(f"\n {Negrito}Escolha sua opção: {Reset}"))

pedra = 1
papel = 2
tesoura = 3

opcaomaquina = choice((pedra, papel, tesoura))

print(f"\n {Negrito} Análisando{Reset} {MagentaClaro}Jogo 🪨 📄 ✂️ {Reset} ... \n")
sleep(2)

if opcaojogador == opcaomaquina:
    print(f"{Azul}Empate!! Jogador = {opcaojogador}, Máquina = {opcaomaquina} \n")
elif opcaojogador!=opcaomaquina:
    if opcaojogador == 1 and opcaomaquina == 2:
        print(f"\n {Vermelho}Computador ganhou! 📄 {Reset} \n")
    elif opcaojogador == 1 and opcaomaquina == 3:
        print(f"\n {Verde}Jogador ganhou! 🪨 {Reset} \n")
    elif opcaojogador == 2 and opcaomaquina == 1:
        print(f"\n {Verde}Jogador ganhou! 📄 {Reset} \n")
    elif opcaojogador == 2 and opcaomaquina == 3:
        print(f"\n {Vermelho}Computador ganhou! ✂️ {Reset}\n")
    elif opcaojogador == 3 and opcaomaquina == 1:
        print(f"\n {Vermelho}Computador ganhou! 🪨 {Reset} \n")
    elif opcaojogador == 3 and opcaomaquina == 2:
        print(f"\n {Verde}Jogador ganhou! ✂️ {Reset} \n")