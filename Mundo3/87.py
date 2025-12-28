#Aprimore o desafio anterior, mostrando no final:    
#A) A soma de todos os valores pares digitados; 
#B) A soma dos valores da terceira coluna; e      
#C) O maior valor da segunda linha.

#Reslução:
from cores import (Negrito, Reset, Verde)

matriz_3x3 = []
pares = []

for horizontal in range(1, 4):
    for vertical in range(1, 4):
        numero = int(input(f"\n {Negrito}Digite os números da matriz (horizontal): {Reset}"))

        if numero not in matriz_3x3:
            print(f"\n {Verde} número {numero} adicionado! ✅{Reset}")
        else:
            print(f"\n {Verde} número {numero} adicionado! ✅ pode ser repetido! {Reset}")
        
        matriz_3x3.append(numero)

        if numero % 2 == 0:
            pares.append(numero)

print(f"\n {sorted(matriz_3x3[0:3])}", end=" ")
print(f"\n {sorted(matriz_3x3[3:6])}", end=" ")
print(f"\n {sorted(matriz_3x3[6:9])}", end=" ")
print(f"\n A soma dos valores pares é = {sum(pares)}")
print(f"A soma dos valores da terceira coluna = {matriz_3x3[6] + matriz_3x3[7] + matriz_3x3[8]}")
print(f"O maior valor da segunda coluna é: {max(matriz_3x3[3:6])}")