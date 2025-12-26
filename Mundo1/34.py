#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

#Resolução:
from cores import(Reset, Negrito, Verde, AmareloClaro, Azul, Magenta)
from time import sleep

salario = float(input(f"{Negrito}\n Digite o salário do funcionário:{Reset} {Verde}R${Reset}"))

print(f"{Magenta}=={Reset}"*30)
print(f"\n {Negrito}Análisando Salário...{Reset} \n")
print(f"{Magenta}=={Reset}"*30)
sleep(0.9)

if salario<=1250.00:
    print(f"{AmareloClaro}\n O funcionário passará a ganhar:{Reset} {Verde}R${(salario)+(0.15*salario)}. {Reset}\n")
else:
    print(f"{Azul}\n O funcionário passará a ganhar:{Reset} {Verde}R${(salario)+(0.10*salario)}{Reset}\n")