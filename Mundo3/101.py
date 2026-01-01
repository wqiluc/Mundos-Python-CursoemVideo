#Crie um programa que tenha uma função chamada voto() 
# que vai receber como parâmetro:
# o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto 
# NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

#Reslução:
from cores import(Negrito,Reset,Amarelo,Verde,Vermelho,Magenta,Azul)
from datetime import datetime

print(f""" 
{Azul}DOCSTRINGS - Utilizando pela 1º vez{Reset}
{Magenta}1 - como já utilizado inúmeras vezes nos 3 primeiros mundos,
'cores' é uma biblioteca externa que eu criei, usando os códigos ANSI
disponóveis no python3;{Reset} {Amarelo}from cores import (as cores que quer usar), já com o código
traduzido{Reset};
{Magenta}2 - datetime.today().year. {Reset}{Amarelo}Ele pega a data atual do seu computador.
{Reset}""")

def voto(ano_idade=0):
    ano_eleitor = int(input(f"\n {Negrito}Digite o seu ano de nascimento: {Reset}"))
    idade_eleitor = datetime.today().year - ano_eleitor
    if (idade_eleitor <=15):
        print(f"\n {Vermelho} Com {idade_eleitor} anos de idade, seu direito de voto está como: NEGADO!!❌ {Reset} \n",end=" ")
    elif idade_eleitor>=16 and idade_eleitor<18:
        print(f"\n {Amarelo}Com {idade_eleitor} anos de idade, seu direito de voto está como: OPCIONAL!! ⚠️{Reset} \n", end=" ")
    else:
        print(f"\n {Verde}Com {idade_eleitor} anos de idade, seu direito de voto está como: OBRIGATÓRIO!! ✅{Reset} \n", end=" ")
    return idade_eleitor
voto(ano_idade=0)