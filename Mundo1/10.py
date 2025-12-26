#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira 
# e mostre quantos dólares ela pode comprar.

#Resolução:

moedaRS = float(input("\n Quanto dinheiro você tem na carteira? R$")) #Real
moedaUSD = moedaRS/5.52 #Dólar

print(f"\n Com R${moedaRS} você consegue comprar: U$D{moedaUSD:.2f} \n")