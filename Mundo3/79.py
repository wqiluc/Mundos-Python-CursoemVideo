#Crie um programa onde o usuário possa digitar vários valores numéricos 
# e cadastre-os em uma lista. 
#Caso o número já exista lá dentro, 
# ele não será adicionado. 
#No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

#Reslução:
from cores import(Negrito,Reset, Vermelho, Amarelo,Verde)
lista_valores = [ ]

while True:
    valor = int(input(f"\n {Negrito} Digite seu valor a ser acumulado aqui: {Reset}"))
    if valor not in lista_valores:
        print(f"\n {Verde} Valor adicionado! ✅ {Reset}")
        lista_valores.append(valor)
    else:
        print(f"\n {Vermelho} VALOR DUPLICADO!❌ Excluindo . . .")
        del valor
    opcao = str(input(f"\n {Negrito} Deseja continuar adicionando valores? [S/N] {Reset}")).upper()
    if opcao == "N":
        break


print(f"\n{Amarelo} Lista = {sorted(lista_valores)}{Negrito}")
