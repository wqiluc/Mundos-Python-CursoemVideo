#Faça um programa que tenha uma lista chamada números e duas funções chamadas 
# sorteia() e somaPar(). 
#A primeira função vai sortear 5 números e vai colocá-los dentro da lista 
# e a segunda função vai mostrar a soma entre todos os valores 
# pares sorteados pela função anterior.

#Reslução:
from random import randint
from cores import Negrito, Reset
numeros = []
soma_valores = 0

def sorteia():
    print(f"{Negrito}Escolhendo 5 valores aleatórios: {Reset}")
    for indice in range(5):
        ordem = randint(1,10)
        numeros.append(ordem)
        print(ordem, end=" ==> ")
    print(indice)
def soma():
    for valores in numeros:
        if valores % 2 == 0:
            valores+=soma_valores
    print(f"{Negrito}Da lista {numeros}, a soma dos valores pares é = {soma_valores} {Reset}")
sorteia()
soma()