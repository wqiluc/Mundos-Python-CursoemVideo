#Faça um programa que mostre a tabuada de vários números, um de cada vez, 
# para cada valor digitado pelo usuário. 
#O programa será interrompido quando o número digitar "N".

#Reslução:
tabuada = 1
from cores import(Negrito,Reset, Vermelho)

while True:
      numero = int(input(f"\n {Negrito}Digite um número pra analisar sua tabuada: {Reset}"))
      if numero<0:
            break
      for tabuada in range(1,11):
            print(f"\n {Negrito} {numero} x {tabuada} = {numero*tabuada} {Reset}")
      opcao = str(input(f"\n {Negrito} Deseja mostrar outro número? (S / N){Reset} ")).upper()
      if opcao=="N":
            break
print(f"\n {Vermelho}Encerrando . . . 💻 ❌{Reset}")