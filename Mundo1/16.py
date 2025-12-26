#Crie um programa que leia um número Real qualquer pelo teclado 
# e mostre na tela a sua porção Inteira.

#Resolução 1:

numero = float(input("\n Digite o número: "))
print(f"\n A porção inteira de {numero} é {numero:.0f} \n")

#Resolução 2:

numero2 = float(input("\n Digite o número 2: "))
inteiro = int(numero2)

print(f"\n A porção inteira de {numero} é {inteiro} \n")