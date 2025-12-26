#O mesmo professor do desafio 019 quer sortear a ordem de apresentação 
# de trabalhos dos alunos. 
# Faça um programa que leia o nome dos quatro alunos 
# e mostre a ordem sorteada.

#Resolução:
from random import shuffle

aluno1 = str(input("\n Digite o nome do primeiro aluno(a): "))
aluno2 = str(input("\n Digite o nome do segundo aluno(a): "))
aluno3 = str(input("\n Digite o nome do terceiro aluno(a): "))
aluno4 = str(input("\n Digite o nome do quarto aluno(a): "))
alunos = [aluno1, aluno2, aluno3, aluno4]
shuffle(alunos)

print(f"A ordem de apresentação será: {alunos} \n")