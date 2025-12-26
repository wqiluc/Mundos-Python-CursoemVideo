#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
#A prestação mensal não pode exceder 30% do salário,
# ou então o empréstimo será negado.

#Resolução:
from cores import(Negrito, Reset, VerdeClaro, VermelhoClaro, AmareloClaro)
from time import sleep

RScasa = int(input(f"\n {Negrito} Digite o valor da casa:{Reset} {VerdeClaro}R${Reset}"))
RSsalario = int(input(f"\n {Negrito} Digite o salário do comprador:{Reset} {VerdeClaro}R${Reset}"))
tempo = int(input(f"\n {Negrito}Digite o tempo de financiamento (em anos): {Reset}"))  

prestacaocasa = (RScasa / (tempo*12))
valorlimite = (RSsalario*0.30)

print(f"{AmareloClaro}Análisando caso... {Reset}\n")
sleep(1)

print(f"{Negrito} Para adquirir um imóvel de:{Reset} {VerdeClaro}R${RScasa}{Reset}{Negrito}em {tempo} anos "
      f"A prestação será de:{Reset} {VerdeClaro}R${(prestacaocasa):.2f}{Reset} mensais {Negrito}e você só pode pagar:{Reset} {VerdeClaro}R${valorlimite}{Reset}")

if prestacaocasa<=valorlimite:
    print(f"\n {VerdeClaro} EMPRÉSTIMO ACEITO!✅🎉{Reset}")
else:
     print(f"\n {VermelhoClaro} EMPRÉSTIMO NEGADO❌{Reset}")
