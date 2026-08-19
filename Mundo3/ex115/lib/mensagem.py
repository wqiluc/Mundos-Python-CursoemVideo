from ex115.lib.cores import *

def sucesso(texto):
    print(f"{Verde}{texto}{Reset}")

def erro(texto):
    print(f"{Vermelho}{texto}{Reset}")

def alerta(texto):
    print(f"{Amarelo}{texto}{Reset}")

def info(texto):
    print(f"{MagentaClaro}{texto}{Reset}")