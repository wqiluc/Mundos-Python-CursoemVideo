from ex115.lib import mensagem, validacoes
from ex115.lib.cores import *

def cadastrar(clientes):
    nome = validacoes.leia_nome(f"{CinzaClaro}Nome: {Reset}")
    idade = validacoes.leia_int(f"{CinzaClaro}Idade: {Reset}")
    clientes.append({"nome": nome.title(), "idade": idade})
    mensagem.sucesso(f"{VerdeClaro}Cliente {nome} cadastrado com sucesso! ✅{Reset}")

def ver(clientes):
    if (not clientes):
        mensagem.alerta(f"{Vermelho}Não há clientes cadastrados. ❌{Reset}")
        return
    else:
        for (indice_cliente), cliente in enumerate(clientes):
            print(f"{CinzaClaro}[{indice_cliente+1}] {cliente['nome']}, {cliente['idade']} anos{Reset}")

def _selecionar(clientes):
    if (not clientes):
        return None # vazio
    else:
        while True:
            valor = str(input(f"{CinzaClaro}Número do cliente (ESC para voltar): {Reset}").strip())
            if (valor.upper() == "ESC"):
                return None
            if not (valor.lstrip("-").isdigit()):
                mensagem.erro(f"{Vermelho}ERRO!❌ Digite um número inteiro válido ou ESC para voltar.{Reset}")
                continue
            indice = int(valor) - 1
            if (indice >= 0 and indice < len(clientes)):
                return indice
            else:
                mensagem.erro(f"{Vermelho}Cliente inválido. ❌{Reset}")

def atualizar(clientes):
    if (not clientes):
        mensagem.alerta(f"{Vermelho}Não há clientes cadastrados. ❌{Reset}")
        return
    else:
        mensagem.info(f"{CinzaClaro}{Reset}")
        indice = _selecionar(clientes)
    if (indice is None):
        return

    print(f"""\n{CinzaClaro}Nome antigo:{Reset} {Vermelho}{clientes[indice]['nome']}{Reset} 
    {CinzaClaro}Idade Antiga:{Reset} {Vermelho}{clientes[indice]['idade']}{Reset}\n""")

    nome = validacoes.leia_nome(f"{CinzaClaro}Novo nome: {Reset}")
    idade = validacoes.leia_int(f"{CinzaClaro}Nova idade: {Reset}")
    clientes[indice] = {"nome": nome.title(), "idade": idade}
    mensagem.sucesso(f"{VerdeClaro}Cliente atualizado com sucesso! ✅{Reset}")

def apagar(clientes):
    if (not clientes):
        mensagem.alerta(f"{Vermelho}Não há clientes cadastrados. ❌{Reset}")
        return
    
    else:
        indice = _selecionar(clientes)
    if (indice is None):
        return
    
    removido = clientes.pop(indice)
    mensagem.sucesso(f"""{VerdeClaro}Cliente {removido['nome']} removido com sucesso! ✅{Reset}""")