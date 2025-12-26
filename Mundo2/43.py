#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#IMC abaixo de 18,5: Abaixo do Peso;
#Entre 18,5 e 25: Peso Ideal;
#25 até 30: Sobrepes
#30 até 40: Obesidade; ou
#Acima de 40: Obesidade Mórbida.

#Reslução:
from cores import(Negrito, Reset, Azul, Amarelo, Vermelho, MagentaClaro)
from time import sleep

peso = int(input(f"\n {Negrito}Digite seu peso - (Kg): {Reset}"))
altura = float(input(f"{Negrito}Digite a sua altura - (m): {Reset}"))
IMC = (peso) / (altura*altura)

print(f"\n {Negrito}IMC = {IMC:.1f}{Reset} \n")
print(f"\n {MagentaClaro} Análisando o seu IMC... {Reset} \n")
sleep(2)

if IMC<18.5:
    print(f"\n {Vermelho}IMC = Abaixo do Peso ideal {Reset} \n")
elif IMC>=18.5 and IMC<25:
     print(f"\n {Azul}IMC = Peso ideal {Reset} \n")
elif IMC>=25 and IMC<30:
      print(f"\n {Amarelo}IMC = Sobrepeso {Reset} \n")
elif IMC>=30 and IMC<=40:
      print(f"\n {Vermelho}IMC = Obesisade {Reset} \n")
else:
      print(f"\n {Vermelho}IMC = OBESIDADE MORBIDA {Reset} \n")