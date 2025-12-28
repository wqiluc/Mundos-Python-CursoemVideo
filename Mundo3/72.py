#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, 
# de zero até vinte. 
#Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

#Reslução:
from cores import(Vermelho, Reset, Amarelo)

extenso = ("Zero","Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", 
    "Nove", "Dez", "Onze", "Doze", "Treze", "Quatorze", "Quinze", 
    "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte") 


numero = str(input("\n Digite um número de 0 a 20: "))
while not numero.isdigit():
    print(f"\n {Vermelho}Termo Inválido. Digite um número (entre 0-20) {Reset}")
    numero = str(input("\n Digite um número de 0 a 20: "))

numero = int(numero)

while numero not in (0,1,2,3,4,5,6,7,8,9,10,11,12,12,13,14,15,16,17.18,19,20):
    print(f"\n {Vermelho}Número inválido. Digite um entre 0-20 {Reset}")
    numero = int(input("\n Digite um número de 0 a 20: "))

if numero>=0 and numero<=20:
    print(f"\n {Amarelo}O número {numero}, por extenso será: {(extenso[numero])}{Reset} \n")
exit()