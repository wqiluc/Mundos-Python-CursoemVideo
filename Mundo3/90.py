#Faça um programa que leia nome e média de um aluno, 
# guardando também a situação em um dicionário. 
#No final, mostre o conteúdo da estrutura na tela.

#Reslução:
from cores import(Negrito,Reset,Amarelo,Verde,Vermelho)

situacao = {
    "nome" : str(input(f"\n {Negrito}Digite o nome do aluno: {Reset}")).upper().strip(),
    "media": float(input(f"\n {Negrito}Digite a média final desse aluno: {Reset}"))
    }

if situacao['media'] < 5:
    print(f"\n {Vermelho}O aluno: {situacao['nome']} com a média final de: {situacao['media']} está REPROVADO! ❌ {Reset} \n")
elif situacao['media'] >= 5 and situacao['media'] < 7:
    print(f"\n {Amarelo} O aluno: {situacao['nome']} com a média final de: {situacao['media']} está de Recuperação! ⚠️{Reset} \n")
else:
    print(f"\n {Verde}O aluno: {situacao['nome']} com a média final de: {situacao['media']} está APROVADO! ✅ {Reset} \n")