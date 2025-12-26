#Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar;
# [ 2 ] multiplicar;
# [ 3 ] maior;
# [ 4 ] novos números; ou
# [ 5 ] sair do programa.
#Seu programa deverá realizar a operação solicitada em cada caso.

#Reslução:
from cores import(Negrito, Reset, AzulClaro, Vermelho)

numero1 = int(input(f"\n {Negrito}Digite o 1º valor: {Reset}"))
numero2 = int(input(f"\n {Negrito}Digite o 2º valor: {Reset}"))
numeros = (numero1, numero2)
soma = numero1+numero2
multiplica = numero1*numero2

opcao_menu= int(input(f"\n {Negrito}Deseja acessar o menu? (1 - S/ 2 - N) {Reset}"))

while opcao_menu!=2:
    print("\n[ 1 ] Somar")
    print("\n [ 2 ] Multiplicar")
    print("\n [ 3 ] maior")
    print("\n [ 4 ] novos números")
    print("\n [ 0 ] sair do programa)")

    opcao_escolha= int(input(f"\n {Negrito}Escolha sua operação: {Reset}"))

    if opcao_escolha==1:
        print(f"{AzulClaro}A soma (+) entre: {numero1} e {numero2} é = {soma}{Reset}")
        break

    if opcao_escolha==2:
        print(f"\n {AzulClaro}A multiplicação (x) entre {numero1} e {numero2} é = {multiplica}{Reset}")
        break

    if opcao_escolha==3:
        print(f"\n {AzulClaro}O maior número é = {max(numeros)} {Reset}")
        break

    if opcao_escolha==4:
        numero_novo = int(input(f"\n {Negrito}Digite o um novo valor: {Reset}"))
        print(f"\n {AzulClaro} Valores Atualizados = {numero1}, {numero2} e {numero_novo}{Reset}")
        break

    if opcao_escolha==0:
        print(f"\n {Vermelho} Encerrando o Programa 💻 ... {Reset}\n")
        break
while opcao_menu==2:
    print(f"\n {Vermelho} Encerrando o Programa 💻 ... {Reset}\n")
    break