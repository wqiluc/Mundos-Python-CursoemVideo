from ex115.lib import validacoes
from ex115.lib.cores import *

def linha(tamanho=42):
    return "-" * tamanho

def cabecalho(texto):
    print(f"{Negrito}{linha()}")
    print(texto.center(42))
    print(f"{linha()}{Reset}")

def menu():
    cabecalho(f"\t{MagentaClaro}MENU{Reset}")
    opcoes = ["Cadastrar cliente", "Ver clientes", "Atualizar cliente", "Apagar cliente", 
              "Sair"]
    cont = 0
    for indice_contador, contador in enumerate(opcoes):
        cont += 1
        print(f"[{indice_contador+1}] - {contador}")
    print(f"{Negrito}{linha()}{Reset}")
    return validacoes.leia_int(f"{CinzaClaro}Escolha uma opção: {Reset}")
