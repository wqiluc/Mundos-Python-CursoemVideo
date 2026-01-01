#Faça um programa que tenha uma função chamada contador(), 
# que receba três parâmetros: início, fim e passo. 
# Seu programa tem que realizar três contagens através da função criada:                                                                                                        a) de 1 até 10, de 1 em 1✅;
# b) de 10 até 0, de 2 em 2✅; e  
# c) uma contagem personalizada.

#Reslução:
from cores import Negrito,Reset

def contador(início, fim, ordem):
    print(f"\n {Negrito}contando de {início} até {fim}, pulando de {ordem} em {ordem} {Reset}")

print(" \n")
for contador1 in range(1,11,1):
    print(contador1, end=" ")
print(" \n")
contador(início=1, fim=10,ordem=1)
print(" \n")
for contador2 in range(10,-1,-2):
    print(contador2, end=" ")
print(" \n")
contador(início=10, fim=-1+1,ordem=-2+4)
print(" \n")

sua_ordem1 = int(input(f"{Negrito}Qual será o início da sua contagem? {Reset}"))
sua_ordem2 = int(input(f"{Negrito}Qual será o fim da sua contagem? {Reset}"))
sua_ordem3 = int(input(f"{Negrito}Qual será a ordem da sua contagem? {Reset}"))

for contagem_propria in range(sua_ordem1,sua_ordem2,sua_ordem3):
    print(contagem_propria, end=" ")
contador(início=sua_ordem1, fim=sua_ordem2,ordem=sua_ordem3)