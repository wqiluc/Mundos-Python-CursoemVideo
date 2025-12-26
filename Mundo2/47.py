#Crie um programa que mostre na tela todos os números pares 
# que estão no intervalo entre 1 e 50.

#Reslução:
from cores import(Reset,Amarelo)

for numeros in range(2,52,2):
    print(f"\n {Amarelo}{numeros}{Reset}", end=' ')
print("ACCABOU")