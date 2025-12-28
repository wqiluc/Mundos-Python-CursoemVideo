#Desenvolva um programa que leia quatro valores pelo teclado 
# e guarde-os em uma tupla. No final, mostre:

#A) Quantas vezes apareceu o valor 9.

#B) Em que posição foi digitado o primeiro valor 3.

#C) Quais foram os números pares.

#Reslução:
numeros = (
    int(input("\n Digite o número: ")),
    int(input("\n Digite o número: ")),
    int(input("\n Digite o número: ")),
    int(input("\n Digite o número: ")))

print(f"\n Tupla digitada: {numeros}")

if 9 not in numeros:
    print("\n O valor 9 não foi digitado.")
else:
    print(f"\n O número 9 apareceu {numeros.count(9)} vezes.")


if 3 not in numeros:
    print("\n O valor 3 não foi digitado.")
else:
    print(f"\n O valor 3 apareceu pela primeira vez na posição {numeros.index(3)}.")

print("\n Valores pares digitados:")
for n in numeros:
    if n % 2 == 0:
        print(n, end=" ")
