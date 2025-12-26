#Faça um programa que leia o nome completo de uma pessoa, 
# mostrando em seguida o primeiro e o último nome, separadamente.

#Resolução:

nome = str(input("Digite seu nome: ")).strip().upper().capitalize()
print(f"É um prazer te conhecer {nome.strip().lower()}")
print(f"Seu primeiro nome é: {nome.split()[0]}")
print(f"Seu último nome é: {nome.split()[-1]}")