#Crie um programa que leia uma frase qualquer e diga 
# se ela é um palíndromo, desconsiderando os espaços.


#Reslução:
from cores import(Negrito, Reset,Verde,Vermelho)
frase = input(f"\n {Negrito}Digite algo: {Reset}").strip().upper()
palavras = frase.split()
junto = "".join(palavras)
inverso = ""

print(f"\n {Negrito}{junto}{Reset}")
print(f"{Negrito}{inverso}{Reset}")

for letras in range(len(junto)-1, -1, -1):
    inverso+=junto[letras]
print(inverso, "\n")
if junto==inverso:
        print(f"\n{Verde}É um palíndromo! ✅{Reset} \n")
else:
       print(f"\n{Vermelho}Não é um palíndromo! ❌{Reset} \n")