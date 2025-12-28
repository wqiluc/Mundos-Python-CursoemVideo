#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, 
# na ordem de colocação. Depois mostre:

#a) Os 5 primeiros times;
#b) Os últimos 4 colocados;
#c) Times em ordem alfabética; e
#d) Em que posição está o time da Chapecoense.

#Reslução:
from cores import (Vermelho, Verde, Reset, Amarelo)

times_brasileirao = (
    "Athletico Paranaense", "Bahia", "Botafogo", "Ceará", "Corinthians",
    "Cruzeiro", "Flamengo", "Fluminense", "Fortaleza", "Gremio",
    "Internacional", "Juventude", "Palmeiras", "Santos", "São Paulo",
    "Vasco da Gama", "América Mineiro", "Atlético Mineiro", "Goias", "Coritiba",
    "Red Bull Bragantino")


print(f"\n {Amarelo} Os Times são: {(times_brasileirao[::])}{Reset} \n")

print(f"\n {Amarelo} Os 5 primeiros times são: {(times_brasileirao[0:5])}{Reset} \n")

print(f"\n {Amarelo} Os 4 últimos colocados são: {(times_brasileirao[-4:])}{Reset} \n")

print(f"\n {Amarelo} Ordem Alfabética: {sorted(times_brasileirao)}{Reset} \n")

if "Chapecoense" not in (times_brasileirao):
    print(f"\n {Vermelho} o Chapecoense NÃO ESTÁ classificado. {Reset} \n")
else:
      print(f"\n {Verde} o Chapecoense ESTÁ classificado. {Reset} \n")