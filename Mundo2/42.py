#Refaça o DESAFIO 35.py dos triângulos, acrescentando o recurso de 
# mostrar que tipo de triângulo será formado:
#EQUILÁTERO: todos os lados iguais;
#ISÓSCELES: dois lados iguais, um diferente; ou
#ESCALENO: todos os lados diferentes.

#Reslução:
from cores import(Negrito, Reset, Amarelo, Verde, Vermelho)
from time import sleep

lado1 = int(input(f"\n {Negrito}Digite o 1º lado: {Reset}"))
lado2 = int(input(f"\n {Negrito}Digite o 2º lado: {Reset}"))
lado3 = int(input(f"\n {Negrito}Digite o 3º lado: {Reset}"))

print(f"\n {Amarelo} Análisando os lados desse Triângulo... {Reset}")
sleep(1.5)

if lado1<lado2+lado3 and lado2<lado1+lado3 and lado3<lado1+lado2:
    print(f"\n {Verde} Estes segmentos podem formar um triângulo ✅{Reset} \n")
else:
    print(f"\n {Vermelho} Estes segmentos não podem formar um triângulo ❌{Reset} \n")
    exit()

if (lado1==lado2==lado3):
    print(f"\n {Negrito} Esses segmentos podem formar um Triângulo EQUILÁTERO! (todos os lados iguais) {Reset} \n")
elif (lado1!=lado2!=lado3!=lado1):
    print(f"\n {Negrito} Esses segmentos podem formar um Triângulo ESCALENO! (todos os lados diferentes) {Reset} \n")
else:
    print(f"\n {Negrito} Esses segmentos podem formar um Triângulo ISÓSCELES! (dois lados iguais e um diferente){Reset} \n")