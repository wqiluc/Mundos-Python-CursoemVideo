#Crie um programa que leia o nome completo de uma pessoa e mostre: 
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.

#Resolução:
from time import sleep

nome = str(input("\n Digite seu nome: ")).strip().capitalize()
print("Análisando seu nome...")
sleep(0.9)
print(f"Seu nome em maíusculo é: {nome.upper()}")
print(f"Seu nome em mínusculo é: {nome.lower()}")
print(f"Ao todo, seu nome tem: {len(nome)} letras")
conta = nome.split()
print(f"Seu primeiro nome é: {conta[0]} e ele tem {len(conta[0])} letras") 
 