#Crie um programa que declare uma matriz de dimensão 3×3 
# e preencha com valores lidos pelo teclado. 
#No final, mostre a matriz na tela, com a formatação correta.

#Reslução:
from cores import(Negrito,Reset, Verde)

matriz_3x3 = [ ]

for horizontal in range(1,4):
    for vertical in range(1,4):
            numero = int(input(f"\n {Negrito}Digite os números da matriz (horizontal): {Reset}"))
            if numero not in matriz_3x3:
                print(f"\n {Verde} número {numero} adicionado! ✅{Reset}")
            else:
                 print(f"\n {Verde} número {numero} adicionado! ✅ pode ser repetido! {Reset}")
            matriz_3x3.append(numero)
print(f"\n {sorted(matriz_3x3[0:3])}", end=" ")
print(f"\n {sorted(matriz_3x3[3:6])}", end=" ")
print(f"\n {sorted(matriz_3x3[6:9])}", end=" ")