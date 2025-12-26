#Escreva um programa que faça o computador "pensar" em um número inteiro 
# entre 0 e 5 e peça para o usuário tentar descobrir 
# qual foi o número escolhido pelo computador. 
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

#Resolução:

from random import choice
from time import sleep
from cores import (
Reset, Negrito, AmareloClaro, MagentaClaro, Verde, Vermelho, Azul)

print(f"{AmareloClaro}-=-{Reset}"*30)
print(f"{Azul}Vou pensar em um número de 0-5. Tente adivinhar{Reset}")
print(f"{AmareloClaro}-=-{Reset}"*30, "\n")

numerojogador = int(input(f"{Negrito}\n Em qual número eu pensei? {Reset}"))
numeromaquina = [0,1,2,3,4,5]
escolhamaquina = choice(numeromaquina)

print(f"{MagentaClaro}\n PROCESSANDO...{Reset} \n")
sleep(0.4)

if (numerojogador==escolhamaquina):
    print(f"{Verde}PARÁBENS!!🎉🥳✅ Você pensou no mesmo número que eu{Reset}\n")
else:
    print(f"{Vermelho}Droga😕❌ Não foi o mesmo número. eu pensei no {escolhamaquina}\n")