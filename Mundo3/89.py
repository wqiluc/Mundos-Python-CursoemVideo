#Crie um programa que leia nome e duas notas 
# de vários alunos e guarde tudo em uma lista composta. 
#No final, mostre um boletim contendo:
# a média de cada um e 
# permita que o usuário possa mostrar as notas de cada aluno individualmente.

#Reslução:
from cores import(Negrito,Reset,Amarelo,Vermelho)

info_alunos = [ ]

while True:
    nome = str(input(f"\n {Negrito} Digite o nome do aluno: {Reset}")).upper().strip()
    while not nome.isalpha():
        print(f"{Vermelho}TERMO INVÁLIDO! Digite um NOME (string){Reset}")
        nome = str(input(f"\n {Negrito} Digite o nome do aluno: {Reset}")).upper().strip()
    nota1 = str(input(f"\n {Negrito} Digita a 1º nota do aluno: {Reset}"))
    while not nota1.replace(".", "").isnumeric():
        print(f"{Vermelho}TERMO INVÁLIDO! Digite um NÚMERO (float){Reset}")
        nota1 = str(input(f"\n {Negrito} Digita a 1º nota do aluno: {Reset}"))
    nota2 = str(input(f" \n {Negrito} Digita a 2º nota do aluno: {Reset}"))
    while not nota2.replace(".", "").isnumeric():
        print(f"{Vermelho}TERMO INVÁLIDO! Digite um NÚMERO (float){Reset}")
        nota2 = str(input(f" \n {Negrito} Digita a 2º nota do aluno: {Reset}"))
    nota1 = float(nota1)
    nota2 = float(nota2)
    media = (nota1+nota2)/2
    info_alunos.append([nome, media][:])
    opcao = str(input(f"\n {Amarelo}Deseja computar outro aluno? [S / N] ")).upper().strip()
    if opcao=="N":
        break

print(f"\n{Negrito}{'-'*35}")
print(f"{'ALUNO':<20}{'MÉDIA'}")
print(f"{'-'*35}{Reset}")
for aluno, media in info_alunos:
    print(f"{aluno:<10}{media:<.2f}")
print(f"{Negrito}{'-'*35}{Reset}")