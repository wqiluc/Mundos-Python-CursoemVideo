import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from ex115.lib.interface import cabecalho, menu
from ex115.lib import clientes as cli
from ex115.lib.mensagem import erro
from ex115.lib.cores import *

def main():
    clientes = list()
    cabecalho(f"\t{CinzaClaro}CADASTRO DE CLIENTES 🏪 {Reset}")
    acoes = [cli.cadastrar, cli.ver, cli.atualizar, cli.apagar]
    while True:
        opcao = menu()
        if (opcao == 5):
            break
        valida = False
        for (indice_opcao), funcao in enumerate(acoes):
            if (opcao == indice_opcao + 1):
                funcao(clientes)
                valida = True
                break
        if not (valida):
            erro(f"{Vermelho}Opção inválida! Escolha um número de 1 a 5. ❌{Reset}")

if __name__ == "__main__":
    main()