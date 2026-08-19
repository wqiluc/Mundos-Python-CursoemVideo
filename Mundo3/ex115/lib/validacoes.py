from ex115.lib import mensagem
from ex115.lib.cores import *

def leia_int(msg):
    valor = str(input(msg).strip())
    while not (valor.lstrip("-").isdigit()):
        mensagem.erro(f"{Vermelho}ERRO!❌ Digite um número inteiro válido. {Reset}")
        valor = str(input(msg).strip())
    return int(valor)

def leia_nome(msg):
    nome = str(input(msg).strip())
    while not (nome.replace(" ", "").isalpha()):
        mensagem.erro(f"{Vermelho}ERRO!❌ Digite um nome válido (somente letras).{Reset}")
        nome = str(input(msg).strip())
    return nome.title()