#Faça um programa que tenha uma função chamada área(), 
# que receba as dimensões de um terreno retangular (largura e comprimento) 
# e mostre a área do terreno.

#Reslução:
from cores import(Negrito,Reset,Amarelo,Azul,Magenta)

def area(largura,comprimento):
    print(f"{Azul}=={Reset}"*20)
    print(f"{Negrito}A Área de um tereno de largura = {largura}m x comprimento = {comprimento}m é ={Reset} {Magenta}{largura*comprimento}m²{Reset}")
    print(f"{Amarelo}=={Reset}"*20)

largura = float(input(f"\n {Negrito}Largura (m): {Reset}"))
comprimento = float(input(f"{Negrito}Comprimento (m): {Reset}"))
area(largura,comprimento)