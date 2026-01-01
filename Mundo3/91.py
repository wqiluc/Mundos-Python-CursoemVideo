#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
#Guarde esses resultados em um dicionário em Python. 
# o final, coloque esse dicionário 
# em ordem, sabendo que o vencedor tirou o maior número no dado.

#Reslução:
from cores import (Negrito, Reset, Magenta, Amarelo,Azul)
from random import (choice)
jogo = { }
numeros = (1,2,3,4,5,6,7,8,9,10)

for jogadores in range(1, 5):
    numero_sorteado = choice(numeros)
    print(f"{Negrito}\n O jogador {jogadores} tirou o número: {numero_sorteado} {Reset}")
    jogo[f"Jogador {jogadores}"] = numero_sorteado

print("\n")
print(f"{Amarelo}=={Reset}"*20)
print(f"{Magenta}RANKING dos jogadores 🎲: {Reset}")
print(f"{Amarelo}=={Reset}"*20)

ranking_game = sorted(jogo.items(), key=lambda item:item[1], reverse=True)
for posicao, (jogador, numero) in enumerate(ranking_game, start=1):
    print(f"\n {Azul}{posicao}º lugar: {jogador} com {numero}{Reset}\n ")