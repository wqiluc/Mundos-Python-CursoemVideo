#Crie um programa que leia duas notas de um aluno e calcule sua média, 
# mostrando uma mensagem no final, de acordo com a média atingida:
#a)Média abaixo de 5.0: REPROVADO;
#b)Média entre 5.0 e 6.9: RECUPERAÇÃO; ou
#c)Média 7.0 ou superior: APROVADO.

#Reslução:
from cores import(Negrito, Reset,  Verde, Vermelho, Amarelo, MagentaClaro)
from time import sleep

nota1 = float(input(f"\n {Negrito}Digite a 1º nota do aluno: {Reset}"))
nota2 = float(input(f"\n {Negrito}Digite a 2º nota do aluno: {Reset}"))
media = (nota1+nota2)/2

print(f"\n {MagentaClaro} Análisando a Situação do aluno... {Reset} \n")
sleep(2)

if (media>=7.0):
    print(f"\n {Verde} Média do aluno = {media:.1f}{Reset} \n")
elif (media>5.0 and media<=6.9):
    print(f"\n {Amarelo} Média do aluno = {media:.1f}{Reset} \n")
else:
    print(f"\n {Vermelho} Média do aluno = {media:.1f}{Reset} \n")

if (media>=7.0):
    print(f"{Verde}Situação do aluno: APROVADO por Média ✅🎓{Reset} \n")
elif (media>5.0 and media<=6.9):
    print(f"{Amarelo}Situação do aluno: RECUPERAÇÃO ⚠️{Reset} \n")
else:
    print(f"{Vermelho}Situação do aluno: REPROVADO ❌{Reset} \n")