#Crie um algoritmo que leia um número e mostre:
#  o seu dobro, triplo e raiz quadrada.

#Resolução:



numero = int(input("\n Digite seu número: "))
dobro = numero*2
triplo = numero*3
raizquadrada = numero**0.5

print("\n O número análisado é: ",numero)
print(f"\n seu dobro é: {dobro}")
print(f"\n seu triplo é: {triplo}")
print(f"\n E, sua raiz quadrada é: {raizquadrada:.1f}\n \n")
