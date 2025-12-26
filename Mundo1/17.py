#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente 
# de um triângulo retângulo.
#Calcule e mostre o comprimento da hipotenusa.

#Resolução:
from math import hypot

oposto = float(input("\n Digite o cateto oposto aqui: "))
adjacente = float(input("\n Digite o cateto adjacente aqui: "))
hipotenusa = hypot(oposto, adjacente)
print(f"\n O Triângulo Retângulo de catetos: {oposto} e {adjacente}, tem uma hipotenusa de: {hipotenusa:.2f} \n")