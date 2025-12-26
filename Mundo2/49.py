#Refaça o DESAFIO 9.py, mostrando a tabuada de um número 
# que o usuário escolher, só que agora utilizando um laço for.

#Reslução:
from cores import(Negrito, Reset, MagentaClaro, Amarelo, Vermelho)
from time import sleep

numero = int(input(f"\n {Negrito}Digite o número a ser análisado: {Reset}"))

print(f"\n {Amarelo}TABUADA PYTHON 🐍 (loop for){Reset}")
print(f"{Vermelho} carregando. . . {Reset}")
sleep(2.3)
print(f"{Amarelo}==={Reset}"*10)
for tabuada in range(1,11):
    resultado = numero*tabuada
    print(f"{MagentaClaro}{numero} x {tabuada} = {resultado}{Reset}")
print(f"{Amarelo}==={Reset}"*10)