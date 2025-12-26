#Elabore um programa que calcule o valor a ser pago por um produto, 
# considerando o seu preço normal e condição de pagamento:
#a)à vista dinheiro/cheque: 10% de desconto;
#b)à vista no cartão: 5% de desconto;
#c)em até 2x no cartão: preço formal; ou
#d)3x ou mais no cartão: 20% de juros.

#Reslução:
from cores import(Negrito, Reset, Verde, Azul, AmareloClaro, Vermelho, MagentaClaro, Cyan)
from time import sleep
print("\n")
print(f"\n {MagentaClaro}========= Lojinha Python 🛍️🐍 ========={Reset}")
preco = float(input(f"\n {Negrito}Digite o preço do Produto:{Reset} {Verde}R${Reset}"))
print(f"\n {Negrito} Métodos de Pagamento 💸💳{Reset} \n")
print(""" 
    1 - À vista dinheiro/cheque;
    2 - À vista no cartão;
    3 - em até 2x no cartão; ou
    4 - 3x ou mais no cartão.""")

opcao = int(input(f"\n {Negrito}Digite o método de pagamento: {Reset}"))
print(f"\n {Cyan} Carregando... {Reset}")
sleep(2)

match opcao:
    case 1:
        print(f"\n {Verde} Pagamento À vista no Dinheiro/Cheque realizado com sucesso✅ de: R${preco:.2f},\n"
              f"você obteve um desconto de 10% off, retornando o valor de: R${(preco)-(preco*0.10)} \n")
    case 2:
        print(f"\n {Verde} Pagamento À vista no Cartão realizado com sucesso✅ de: R${preco}\n, "
              f"você obteve um desconto de 5% off, retornando o valor de: R${(preco)-(preco*0.05):.2f}\n")
    case 3:
        print(f"\n {Azul} Pagamento de 2x no Cartão realizado com sucesso✅ preço base: R${preco:.2f}\n ")
    case 4:
        parcelascartao = int(input(f"\n {AmareloClaro}Quantas parcelas no cartão?{Reset}"))
        print(f"\n {AmareloClaro} Pagamento de 3x ou mais no Cartão realizado com sucesso✅ de: R${preco},\n"
              f"adicionamos um acrescimo de 20% , retornando o valor de: R${(preco)+(preco*0.20):.2f}")
    case __:
        print(f"\n {Vermelho} Método de pagamento inválido! Tente novamente{Reset} \n")
        exit()