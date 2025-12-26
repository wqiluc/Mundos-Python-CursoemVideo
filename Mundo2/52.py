#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

#Reslução:
from cores import(Negrito, Reset, VerdeClaro, VermelhoClaro)
numero = int(input(f"\n {Negrito}Digite o número a ser análisado: {Reset}"))
total = 0

for analise in range(1, numero+1):
    if numero % analise == 0:
        print(f"{VermelhoClaro}{Reset}", end=" ")
        total += 1
    else:
        print(f"{VerdeClaro}{Reset}", end=" ")
    print(f"\n {analise}\n ", end=" ")
print(f"\n O número {numero} foi divisível {total} vezes")
if total==2:
    print(f"\n {VerdeClaro}Por isso ele é primo! ✅{Reset}")
else:
    print(f"\n {VermelhoClaro}Por isso ele não é primo! ❌{Reset}")



