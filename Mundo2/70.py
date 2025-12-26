#Crie um programa que leia o nome e o preço de vários produtos. 
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

#A) qual é o total gasto na compra.

#B) quantos produtos custam mais de R$1000.

#C) qual é o nome do produto mais barato.

#Reslução:
acumulador_total_compra = 0
acumulador_produtos_1000 = 0
lista_produtos = [ ]

from cores import(Negrito,Reset,VerdeClaro, Vermelho, MagentaClaro, Amarelo)

while True:
    opcao = str(input(f"\n {Negrito}Deseja continuar comprando? (S/N) {Reset}")).upper()
    if opcao=="N":
        break
    produtos = float(input(f"\n {MagentaClaro}Digite o preço dos produtos:{Reset} {VerdeClaro} R${Reset}"))
    acumulador_total_compra+=produtos
    lista_produtos.append(produtos)
    if produtos>1000:
        acumulador_produtos_1000+=1
    
print(f"\n {Negrito}O Total gasto dessa compra foi de:{Reset}{VerdeClaro} R${Reset} {acumulador_total_compra}{Reset} \n")
print(f"\n {Negrito}Os produtos que custaram mais de{Reset} {VerdeClaro}1000R$: {Reset}{VerdeClaro}R${Reset} {acumulador_produtos_1000} {Reset}\n")
print(f"\n{Amarelo}O produto de menor preço desta compra foi:{Reset} {VerdeClaro}R$ {min(lista_produtos):.2f}{Reset}")
print(f"\n {Vermelho}Encerrando o sistema 💻 ❌ . . . {Reset}")


