#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados 
# e vai sortear 6 números entre 1 e 60 para cada jogo, 
# cadastrando tudo em uma lista composta.

#Reslução:
from cores import (Negrito, Reset)
from random import sample

mega_sena = []
jogos = int(input(f"\n {Negrito}Digite quantos jogos quer jogar? {Reset}"))

for megasena in range(jogos):
    numeros = sample(range(1,61),6)
    numeros.sort
    mega_sena.append(numeros)
    
print(f"\n {Negrito}Jogos gerados: {Reset}")
for tentativas,jogo in enumerate(mega_sena, start=1):
    print(f"\n Jogo {tentativas} = {jogo} ")