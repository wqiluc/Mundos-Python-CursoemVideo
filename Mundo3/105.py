#Faça um programa que tenha uma função notas() 
# que pode receber várias notas de alunos 
# e vai retornar um dicionário com as seguintes informações: Quantidade de notas;   
# A maior nota; # A menor nota; # A média da turma; e a situação (opcional)

#Reslução:
from cores import (Negrito,Reset,Vermelho,Amarelo,Verde,MagentaClaro,Azul)
info_alunos = dict( )
info_aluno = list( )

def notas():
    while True:
        nome = str(input(f"\n {Negrito}Digite o nome do aluno: {Reset}")).upper().strip()
        while not nome.replace(" ", "",10).isalpha():
            print(f"\n {Vermelho}Digite um NOME (string){Reset}")
            nome = str(input(f"{Negrito}Digite o nome do aluno: {Reset}")).upper().strip()
        nome = str(nome)
        nota1 = str(input(f"\n {Negrito}Digite a 1ª nota do aluno: {Reset}"))
        while not nota1.replace(".", "",1).isdigit():
            print(f"{Vermelho}\n Termo Inválido!!❌ Digite uma nota (float) {Reset}")
            nota1 = str(input(f"\n {Negrito}Digite a 1ª nota do aluno: {Reset}"))
        nota2 = str(input(f"\n {Negrito}Digite a nota 2 do aluno: {Reset}"))
        while not nota2.replace(".", "",1).isdigit():
            print(f"{Vermelho}T\n ermo Inválido!!❌ Digite uma nota (float) {Reset}")
            nota2 = str(input(f"\n {Negrito}Digite a 2ª nota  o aluno: {Reset}"))
        nota1 = float(nota1)
        nota2 = float(nota2)
        media = (nota1+nota2) / 2
        print(f"\n {Negrito}As notas do aluno: {nome:<5}; foram{Reset}: {Amarelo}{nota1}{Reset} e {Azul}{nota2}{Reset}, tendo sua média = {MagentaClaro}{media:.2f} {Reset}")
        if media <=5:
            print(f"\n {Vermelho}Situação do aluno = REPROVADO!! ❌{Reset} \n")
            info_aluno.append([f"Nome do aluno = {nome} ; 1ª nota = {nota1}, 1ª = {nota2} & média final = {media:.2f}"])
        elif media>5 and media<=6:
            print(f"\n {Amarelo}Situação do aluno = DE RECUPERAÇÃO !! ⚠️{Reset}")
            info_aluno.append([f"Nome do aluno = {nome} ; 1ª nota = {nota1}, 1ª nota = {nota2} & média = {media:.2f}"])
        else:
            print(f"\n {Verde}Situação do aluno = APROVADO!! ✅{Reset}")
            info_aluno.append([f"Nome do aluno = {nome} ; 1ª nota = {nota1}, 2ª nota = {nota2} & média final = {media:.2f}"])
            info_aluno.copy()
            info_alunos.copy()
        opcao = str(input(f"\n {Negrito}Deseja adicionar mais notas?{Reset}" 
                          f"[{Verde}S{Reset} / {Vermelho}N{Reset}] {Reset}")).upper().strip()
        while not opcao in 'SN':
            print(f"\n {Vermelho}Termo INVÁLIDO! Digite um valor: {Reset}" 
            f"[{Verde}S{Reset} / {Vermelho}N{Reset}]")
            opcao = str(input(f"{Negrito}Deseja adicionar mais notas?" 
            f"[{Verde}S{Reset} / {Vermelho}N{Reset}]")).upper().strip()
        if opcao=="N":
            break
notas()
print(info_aluno)