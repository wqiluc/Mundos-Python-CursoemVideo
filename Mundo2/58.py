#Melhore o jogo do DESAFIO 28.py,
# onde o computador vai “pensar” em um número entre 0 e 10. 
#Só que agora, o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

#Reslução:
acumulador_tentativas = 1
numero_inicial = 1
from cores import(Negrito, Reset, Vermelho, Verde)
from random import choice 

numerojogador = int(input(f"\n {Negrito}Adivinhe o número que o computador está pensando: {Reset}"))
numeroscomputador = (1,2,3,4,5,6,7,8,9,10)
choice(numeroscomputador)

while numerojogador!=choice(numeroscomputador):
    print(f"\n {Vermelho}Droga. Você errou o número. eu pensei em: {choice(numeroscomputador)} e você escreveu {numerojogador}")
    acumulador_tentativas+=1
    numerojogador = int(input(f"\n {Negrito}Tente novamente adivinhar o número que o computador está pensando: {Reset}"))
    if numerojogador==choice(numeroscomputador):
        print(f"\n {Verde} BOAA!! ✅ pensamos no mesmo número < {numerojogador} > Você precisou de {acumulador_tentativas} tentativa(as) pra acertar 🤣{Reset} \n")
        break