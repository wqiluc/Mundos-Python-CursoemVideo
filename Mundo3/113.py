#Reescreva a função leiaInt() que fizemos no desafio 104, 
# incluindo agora a possibilidade 
# da digitação de um número de tipo inválido. 
# Aproveite e crie também uma função 
# leiaFloat();
# com a mesma funcionalidade.

#Reslução:
from cores import(Negrito,Reset,Vermelho,Magenta,Verde)
def leiaInt():
    valor = str(input(f"\n {Negrito}Digite um 1° valor: {Reset}")).strip()
    try:
        valor = int(valor)
    except:
        print(f"\n {Vermelho}Termo Inválido!! ❌ Digite APENAS um valor{Reset} {Magenta}(int){Reset}")
        return leiaInt()
    print(f"\n {Verde}DEFINIDO!!✅{Reset} {Negrito}O valor que você digitou:{Reset} {Verde}{valor}{Reset} {Negrito}É UM{Reset} {Verde}(int ✅){Reset}")
leiaInt()
def leiaFloat():
    valor2 = str(input(f"\n {Negrito}Digite um 2° valor: {Reset}")).strip()
    try:
        valor2 = float(valor2)
    except:
        print(f"\n {Vermelho}Termo Inválido!! ❌ Digite APENAS um valor{Reset} {Magenta}(float){Reset}")
        return leiaFloat()
    print(f"\n {Verde}DEFINIDO!!✅{Reset} {Negrito}O valor que você digitou:{Reset} {Verde}{valor2}{Reset} {Negrito}É UM{Reset} {Verde}(float ✅){Reset}")
leiaFloat()