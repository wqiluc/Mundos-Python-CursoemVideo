from ..cores import (Verde, Reset,Negrito,Vermelho)

def moeda(valor=0):
    return f"{Verde}R${valor:.2f}{Reset}"
def aumentar(valor=0, resposta=False,formato=False):
    resposta = valor + valor
    return moeda(resposta) if formato else resposta
def diminuir(valor=0, formato=False):
    resposta = valor - valor
    return moeda(resposta) if formato else resposta
def dobrar(valor=0, formato=False):
    resposta = valor * 2
    return moeda(resposta) if formato else resposta
def metade(valor=0, formato=False):
    resposta = valor /2
    return moeda(resposta) if formato else resposta

def resumo(valor=0, resposta=False, formato=False):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: ====\t{moeda(valor)}')
    print(f'Dobro do preço: ====\t{dobrar(valor, True)}')
    print(f'Metade do preço: ====\t{metade(valor, True)}')
    print('-' * 30)
    
def leiadinheiro(msg="Digite o valor: R$"):
    while True:
        valor = str(input(f"\n{msg} ").strip().replace(",", "."))
        try:
            valor_float = float(valor)
            return valor_float
        except ValueError:
            print(f"\n{Vermelho} Valor '{valor}' inválido! Digite um valor numérico.{Reset}\n")