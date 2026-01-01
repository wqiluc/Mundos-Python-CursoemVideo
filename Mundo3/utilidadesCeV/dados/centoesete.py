#Crie um módulo chamado "moeda.py",
# que tenha as funções incorporadas: aumentar(), diminuir(), dobro() e metade(). 
#Faça também um programa que importe esse módulo e use algumas dessas funções.

#Resluçuão:
from ..cores import Verde, Reset, Negrito
from ..moeda import centoesetemoeda

valor = centoesetemoeda.leiadinheiro()

print(f"Você digitou: R${valor:.2f}")

print(f"\n{Negrito}AUMENTO:{Reset} {Verde}R${centoesetemoeda.aumentar(valor):.2f}{Reset}")
print(f"\n{Negrito}DOBRAR:{Reset} {Verde}R${centoesetemoeda.dobrar(valor):.2f}{Reset}")
print(f"\n{Negrito}METADE:{Reset} {Verde}R${centoesetemoeda.metade(valor):.2f}{Reset}")
print(f"\n{Negrito}DIMINUIR:{Reset} {Verde}R${centoesetemoeda.diminuir(valor):.2f}{Reset}")

