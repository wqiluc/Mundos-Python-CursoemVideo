#Crie um programa que leia vários números inteiros pelo teclado. 
#O programa só vai parar quando o usuário digitar o valor 999, 
# que é a condição de parada. 
#No final, mostre quantos números foram digitados 
# e qual foi a soma entre eles (desconsiderando o flag).

#Reslução:
from cores import(Negrito, Reset, MagentaClaro)
acumulador_soma_numeros = acumulador_termos = 0


print(f"\n {Negrito} [ 9 9 9 ] pra parar {Reset}")
numero = int(input(f"\n {Negrito}Digite um número: {Reset}"))
acumulador_soma_numeros = numero
acumulador_termos = 1

while (numero!=999):
    print(f"\n {Negrito} [ 9 9 9 ] pra parar {Reset}") 
    numero = int(input(f"\n {Negrito}Digite um número: {Reset}"))
    acumulador_soma_numeros+=numero
    acumulador_termos+= 1
    continue

while(numero==999):
    if numero==999:
        acumulador_soma_numeros-=999
        acumulador_termos-=1
        print(f"\n {MagentaClaro}você somou {acumulador_termos} termos, e a sua soma é = {acumulador_soma_numeros}")
        break