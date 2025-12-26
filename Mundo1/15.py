#Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado 
# e a quantidade de dias pelos quais ele foi alugado. 
#Calcule o preço a pagar, sabendo que: 
# o carro custa R$60 por dia e R$0,15 por Km rodado.

#Resolução:

distanciaKM = float(input("Digite a distância(em KM) que o veículo ira percorrer: "))
diasalugados = int(input("E, por quantos dias esse veículo será alugado? "))

precoRS = (60*diasalugados)+(0.15*distanciaKM)

print(f"\n O total a pagar será de: R${precoRS}\n ")