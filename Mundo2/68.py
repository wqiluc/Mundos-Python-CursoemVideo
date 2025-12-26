#Faça um programa que jogue par ou ímpar com o computador. 
# O jogo só será interrompido quando o jogador perder, 
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

#Reslução:
acumulador_tentativas = 0
from cores import(Negrito,Reset, Verde,Vermelho, Amarelo)
from random import choice

while True:
    numero_jogador = int(input(f"\n {Negrito} Digite um número: {Reset}"))
    numeros_computador = (1,2,3,4,5,6,7,8,9,10)
    numeros_computador = choice(numeros_computador)
    numero_analisado = numero_jogador + numeros_computador

    print(f"\n {Negrito}Número computador = {numeros_computador}{Reset}")
    print(f"\n {Negrito}Número Analisado = {numero_analisado}{Reset} \n")

    acumulador_tentativas+=1

    if numero_analisado % 2 == 0:
        print(f"{Verde} JOGADOR GANHOU !! 🥳✅{Reset}")
        break
    else:
       print(f"{Vermelho} COMPUTADOR GANHOU !! 💻❌{Reset}")
    
print(f"{Amarelo} O jogador precisou de {acumulador_tentativas} tentativas {Reset}")