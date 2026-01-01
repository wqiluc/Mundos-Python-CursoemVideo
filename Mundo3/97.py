#Faça um programa que tenha uma função chamada: "escreva()", 
# que receba um texto qualquer como parâmetro 
# e mostre uma mensagem com tamanho adaptável.

#Reslução:  
from cores import(Negrito,Reset,Azul,Amarelo,Magenta)

def escreva(texto):
    print(f"{Azul}=={Reset}"*5, " \n", texto)
    print("          ",  f"{Azul}=={Reset}"*5)

texto = str(input(f"\n {Negrito}Digite algo: {Reset}")).lower().strip()
escreva(texto)