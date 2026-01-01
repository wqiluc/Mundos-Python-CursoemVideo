#Faça um programa que tenha uma função chamada ficha(), 
# que receba dois parâmetros opcionais: 
# o nome de um jogador e quantos gols ele marcou. 
#O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

#Reslução:
from cores import(Negrito,Reset,Amarelo,Azul,Magenta)
print(f"""
    {Azul}DOCSTRINGS 💉 – FICHA DO JOGADOR ⚽️ \n{Reset}
{Magenta} Este exercício cria uma função chamada ficha_jogador(),
que recebe dois parâmetros opcionais:
    - nome → nome do jogador (string)
    - gols → número de gols marcados (inteiro)
Caso o nome não seja informado, ele será considerado
como "DESCONHECIDO".
A verificação de dados vazios pode ser feita utilizando a expressão lógica: {Reset}
    {Amarelo}
    not nome and not gols or gols == 0
    {Reset}
    {Magenta}
Onde:
    - not nome → verifica se o nome está vazio
    - gols == 0 → indica que o jogador não marcou gols {Reset}""")

def ficha_jogador(nome=" ",gols=0):
    nome = str(input(f"\n {Negrito}Digite o nome do jogador: {Reset}")).upper().strip()
    partida = str(input(f" \n {Negrito}Digite o número de partidas que esse jogador jogou: {Reset}"))
    if not partida.isnumeric():
        if not nome and gols or gols==0:
            nome == "Desconhecido"
            print(f"{Negrito}O jogador {nome} jogou {partida} partidas{Reset}")
    elif partida.isnumeric() and not nome:
        print(f"{Negrito}O jogador {nome} jogou {partida-partida} partidas{Reset}")
    else:
        partida = int(partida)
        print(f"{Negrito}O jogador {nome} jogou {partida} partidas{Reset}")
ficha_jogador(nome=" ", gols=0)