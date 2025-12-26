#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes 
# aparece a letra "A", em que posição ela aparece a primeira vez 
# e em que posição ela aparece a última vez.

#Resolução:
from time import sleep

nome = str(input("\nDigite seu nome: ")).strip().lower()
print("\nAnálisando o nome {}".format(nome))
sleep(0.43)

print(f"\n A letra 'a' aparece {nome.count("a")} vez(es) na frase")
print(f"\n pela 1ª vez na {nome.find("a")}ª posição")
print(f"\n pela última vez na {nome.rfind("a")}ª posição \n")