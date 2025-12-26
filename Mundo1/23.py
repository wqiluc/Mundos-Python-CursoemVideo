#Faça um programa que leia um número de 0 a 9999 
# e mostre na tela cada um dos dígitos separados.

#Resolução:
from time import sleep

numero = int(input("\nDigite o número aqui: "))
string = str(numero)
print(" \nAnálisando o Número acima... \n")
sleep(0.5)

print(f"Unidade = {string[3]}")
print(f"Dezena = {string[2]}")
print(f"Centena = {string[1]}")
print(f"Milhar = {string[0]} \n")

# 1, 2, 3, 4, 5... = normal
#[0],[1],[2],[3],[4].. = Python
# 1 = [0], 2 = [1], 3 = [2], 4 = [3], 5 = [4]
