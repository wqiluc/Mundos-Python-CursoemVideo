#Aprimore o desafio 93 para que ele funcione com vários jogadores, 
# incluindo um sistema de visualização de detalhes do aproveitamento 
# de cada jogador.

#Reslução:
from cores import (Negrito, Reset, Magenta, Vermelho, Amarelo, Azul)
time = []
jogador = {}
gols = []
total_gols = 0

while True:
    jogador["nome jogador"] = input(
        f"\n{Negrito}Digite o nome do jogador: {Reset}").upper().strip()
    partidas = int(input(
        f"{Negrito}Digite quantas partidas {jogador['nome jogador']} jogou: {Reset}"))

    for partida_contagem in range(partidas):
        gol_partida = int(input(
            f"{Magenta}Quantos gols {jogador['nome jogador']} fez na {partida_contagem+1}ª partida: {Reset}"))
        gols.append(gol_partida)
        total_gols += gol_partida

    jogador["gols"] = gols[:]
    jogador["Total Score"] = total_gols
    time.append(jogador.copy())

    opcao = input(f"\n{Azul}Deseja adicionar mais jogadores? [S / N] {Reset}").upper().strip()
    while opcao not in 'SN':
        print(f"{Vermelho}Termo INVÁLIDO!! ❌ Digite APENAS [S / N]{Reset}")
        opcao = input(f"{Azul}Deseja adicionar mais jogadores? [S / N] {Reset}").upper().strip()
    if opcao == "N":
        break

print(f"{Amarelo}=={Reset}" * 10)
print(f"{Magenta}Dados Jogadores:{Reset}")
print(f"{Amarelo}=={Reset}" * 10)

print(f"{Negrito}{'CÓDIGO':<9}{'NOME':<20}{'GOLS':<25}{'TOTAL SCORE'}{Reset}")
for posicao, j in enumerate(time):
    print(f"{posicao:<9}{j['nome jogador']:<20}{str(j['gols']):<25}{j['Total Score']}")

while True:
    codigo_jogador = int(input(f"\n{Azul}Digite o código do jogador (999 = parar): {Reset}"))
    if codigo_jogador == 999:
        print(f"\n{Magenta}Encerrando{Reset} . . . ⚽️\n")
        break
    elif codigo_jogador >= len(time):
        print(f"{Vermelho}Código inválido!! ❌ Digite um existente{Reset}")
    else:
        print(f"\n{Magenta}Levantamento do jogador: {time[codigo_jogador]['nome jogador']}{Reset}")
        for indice, g in enumerate(time[codigo_jogador]["gols"]):
            print(f"O jogador {time[codigo_jogador]['nome jogador']} "
                f"➜ Na {indice+1}ª partida fez {g} gol(s)")