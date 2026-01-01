#Crie um programa que tenha uma função fatorial() 
# que receba dois parâmetros: 
# o primeiro que indique o número a calcular 
# e outro chamado show, que será um valor lógico (opcional);
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

#Reslução:
from cores import(Negrito,Reset,Magenta,Azul,Amarelo)
from math import factorial
print(f"""
    {Azul}DOCSTRINGS 102.PY {Reset} \n
{Magenta}O principal método utilizado neste exercício é o do fatorial,
representado e acessado por:{Reset}
    {Amarelo} from math import{Reset} {Azul}factorial.{Reset}
{Magenta}No qual, retorna n! de um número. Exemplo:
factorial(5) = 120; ou 5x4x3x2x1 = 120{Reset} \n""")

def fatorial(numero,show=False):
    numero = int(input(f"\n {Negrito}Digite o número que terá o fatorial análisado: {Reset}"))
    inicio = 1
    for contagem in range(numero, 0, -1):
        if (show==True):
            print(f"{contagem}", end=" x "
            if contagem > 1.
            else " = ")
        inicio *= contagem
    print(f"\n {Amarelo}O fatorial do número {numero} é = {factorial(numero)}{Reset}")
    return inicio
fatorial(numero=0, show=True)