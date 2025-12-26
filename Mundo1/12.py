#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, 
# com 5% de desconto.

#Resolução:

produto = float(input("\n Digite o preço do produto: R$"))

#5% de desconto:
desconto = (produto)-(produto*0.05)
print(f"\n O produto de preço R${produto}, com 5% de desconto fica: R${desconto:.2f} \n")