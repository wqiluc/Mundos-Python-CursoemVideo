#Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
#O programa vai ler o nome do jogador e quantas partidas ele jogou. 
#Depois vai ler a quantidade de gols feitos em cada partida. 
#No final, tudo isso será guardado 
# em um dicionário, incluindo o total de gols feitos durante o campeonato.

#Reslução:
from cores import(Negrito,Reset,Magenta)
jogador_dados = { }
total_gols = 0

jogador_dados["nome"] = str(input(f"\n {Negrito}Digite o nome do jogador: {Reset}")).upper().strip()
jogador_dados["partidas"] = int(input(f"\n {Negrito}Quantas paritdas {jogador_dados['nome']} já jogou? {Reset}"))
for partidas in range(jogador_dados["partidas"]):
    jogador_dados["gols"] = int(input(f"{Magenta }Quantos gols {jogador_dados['nome']} marcou na {partidas+1}cpartida? {Reset} "))
    total_gols+=jogador_dados['gols']
    print(f"{Negrito}Marcou {jogador_dados['gols']} gol(s) na {partidas+1}º partida {Reset}")
    
print(f"{Magenta}O jogador {jogador_dados['nome']} jogou {jogador_dados['partidas']} {Reset}")
print(f"{Negrito}O total de gols foi: {total_gols} {Reset}")