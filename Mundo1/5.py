#Faça um programa que leia um número Inteiro e mostre na tela 
# o seu sucessor e seu antecessor.

#Resolução:

numero = int(input("\n Digite seu número inteiro: "))
antecessor = numero-1
sucessor = numero+1

print(f"""\n Análisando o número {numero}, seu antecessor é: {antecessor}, e seu sucessor é: {sucessor} \n """)