#Faça um programa que leia algo pelo teclado 
# e mostre na tela o seu tipo primitivo e 
# todas as informações possíveis sobre ele.

#Resolução:

variavel1 = str(input("\n Digite algo: "))

print("\n É númerico inteiro ou texto?", variavel1.isalnum())
print("\n É texto?", variavel1.isalpha())
print("\n Está só em maíusculo?", variavel1.isupper())
print("\n Está só em mínusculo?", variavel1.islower())
print("\n Traduza p maíusculo: ", variavel1.capitalize())
print("\n É 'escrevivel' no terminal?", variavel1.isprintable())
print("\n É um número inreiro?", variavel1.isdigit())
