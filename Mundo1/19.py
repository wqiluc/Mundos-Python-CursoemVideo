#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo 
# na tela o nome do escolhido.

#Resolução:
from random import choice

aluno1 = str(input("\n Digite o nome do primeiro aluno(a): "))
aluno2 = str(input("\n Digite o nome do segundo aluno(a): "))
aluno3 = str(input("\n Digite o nome do terceiro aluno(a): "))
aluno4 = str(input("\n Digite o nome do quarto aluno(a): "))

alunos = aluno1, aluno2, aluno3, aluno4
escolhido = choice(alunos)

print(f"\n O aluno escolhido foi: {escolhido}")