#Faça um programa que leia um ângulo qualquer e mostre na tela o valor de:
# seno, cosseno e tangente desse ângulo.

#Resolução:
from math import sin, cos, tan, radians


angulo = float(input("\nDigite o ângulo a ser análisado: "))
seno = sin(radians(angulo))
print(f"\n O seno de {angulo}° é {seno:.2f}")
cosseno = cos(radians(angulo))
print(f"\n O Cosseno de {angulo}° é {cosseno:.2f}")
tangente = tan(radians(angulo))
print(f"\n A Tangente de {angulo}° é {tangente:.2f} \n")