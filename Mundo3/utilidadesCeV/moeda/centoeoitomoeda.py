from ..cores import(Negrito,Reset,Vermelho)


from cores import(Verde,Reset)
def aumentar(valor):
    return valor+valor
def diminuir(valor):
    return valor-valor
def dobrar(valor):
    return valor*2
def metade(valor):
    return valor/2
def moeda(valor):
    return {f"\n {Verde}R${valor}{Reset}"}
def leiadinheiro(msg="Digite o valor: R$"):
    while True:
        valor = str(input(f"\n{msg} ").replace(",", ".").strip())
        try:
            return float(valor)
        except ValueError:
            print(f"\n{Vermelho}Valor '{valor}' inválido! Digite um valor numérico.{Reset}\n")
