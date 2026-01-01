#Crie um programa que tenha a função leiaInt(), 
# que vai funcionar de forma semelhante a função input() do Python, 
# só que fazendo a validação para aceitar apenas um valor numérico. 
# x: n = leiaInt(‘Digite um n: ‘)

#Reslução:

from cores import(Negrito,Reset,Amarelo,Azul,Magenta,Vermelho,Verde)
from time import sleep

print(f"""
        {Azul}DOCSTRINGS 104.PY{Reset}

{Magenta}Este exercício propõe a criação de uma função chamada{Reset}
{Amarelo}leiaInt(){Reset}, {Magenta}que funciona de forma semelhante à função nativa{Reset}
{Amarelo}input(){Reset} {Magenta}do Python, porém realizando validação de dados.{Reset}

{Magenta}Objetivo:{Reset}
{Magenta}Garantir que o valor digitado pelo usuário seja obrigatoriamente
um número inteiro válido, evitando erros causados por entradas inválidas,
como letras, símbolos ou valores vazios.{Reset}

{Magenta}Funcionamento:{Reset}
{Magenta}• A função recebe uma mensagem como parâmetro.{Reset}
{Magenta}• Solicita a entrada do usuário.{Reset}
{Magenta}• Verifica se o valor digitado pode ser convertido em inteiro.{Reset}
{Magenta}• Caso não seja válido, exibe uma mensagem de erro.{Reset}
{Magenta}• Repete o processo até que um valor inteiro seja informado.{Reset}

{Magenta}Retorno:{Reset}
{Magenta}• Retorna um valor do tipo{Reset} {Amarelo}int{Reset}

{Magenta}Exemplo de uso:{Reset}
    {Amarelo}n = leiaInt("Digite um número: "){Reset}
    {Amarelo}print(f"Você digitou o número n"){Reset}""")

def leiaint():
    numero = str(input(f"\n {Negrito}Digite o seu número: {Reset}"))
    print(f"{Amarelo}Análisando o seu input . . .{Magenta}")
    sleep(1)
    while not numero.isnumeric():
        print(f"\n {Vermelho}Termo Inválido!! Digite APENAS um número inteiro (int){Reset}")
        numero = str(input(f"\n {Negrito}Digite o seu número: {Reset}"))
        print(f"{Amarelo}Análisando o seu input . . .{Magenta}")
        sleep(1)
    numero = int(numero)
    print(f"\n {Negrito}Você digitou o número: {numero}{Reset}, {Verde}e ele é inteiro! ✅{Reset}")
leiaint()