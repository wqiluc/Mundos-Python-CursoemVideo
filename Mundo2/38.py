#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#O primeiro valor é maior;
#O segundo valor é maior; ou
#Não existe valor maior, os dois são iguais.

#Reslução:
from cores import(Negrito,Reset,Azul,AmareloClaro, Magenta, VerdeClaro)
from time import sleep

numero1 = int(input(f"\n {Negrito}Digite o 1º número: {Reset}"))
numero2 = int(input(f"\n {Negrito}Digite o 2º número: {Reset}"))
print(f"\n {VerdeClaro} Análisando os dois números...{Reset} \n")
sleep(2)

if (numero1>numero2):
    print(f"\n {Azul}O 1º número é maior!: {numero1}{Reset}")
elif (numero2>numero1):
    print(f"\n {AmareloClaro}O 2º número é maior!: {numero2}{Reset}")
elif (numero1==numero2):
    print(f"\n {Magenta} Ambos os números são iguais!{Reset} \n")

