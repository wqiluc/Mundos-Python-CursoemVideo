#Desenvolva um programa que leia as duas notas de um aluno, 
# calcule e mostre a sua média.

#Resolução:

nota1 = float(input("\n Digite a primeira nota do aluno: "))
nota2 = float(input("\n Digite a segunda nota do aluno: "))
media = (nota1+nota2)/2

print(f"\n A média desse aluno foi: {media:.2f}\n")
