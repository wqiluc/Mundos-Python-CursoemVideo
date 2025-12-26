#Crie um programa que leia o nome de uma pessoa 
# e diga se ela tem "SILVA" no nome.

#Resolução:

nome = str(input("\n Digite seu nome: ")).strip().upper()

print(f"\n Há 'SILVA' no seu nome? {"SILVA" in nome} \n")