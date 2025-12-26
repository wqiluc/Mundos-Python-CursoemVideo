#Desenvolva um programa que pergunte a distância de uma viagem em Km. 
#Calcule o preço da passagem, cobrando:
# R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

#Resolução:
from cores import(Reset, Negrito, Azul, Magenta, Amarelo, Verde)


distancia = int(input(f"{Negrito}\n Digite a distância da sua viagem (em Km): {Reset}"))
print(f"{Magenta}\n Sua viagem terá uma distância de: {distancia}Km \n")
if distancia<=200:
    print(f"{Azul}O valor da sua viagem será de:{Reset} {Verde}R${(0.50)*distancia}{Reset} \n")
else:
    print(f"{Amarelo}O valor da sua viagem será de:{Reset} {Verde}R${(0.45)*distancia:.2f}{Reset} \n")