#Crie um programa que tenha uma tupla única com nomes de produtos 
# e seus respectivos preços, na sequência. 
#No final, mostre uma listagem de preços, 
# organizando os dados em forma tabular.

#Reslução:
contador = 0
numeros = (
    str(input("\n Digite o nome do produto: ")).strip().upper(),
    float(input("\n Digite seu preço: R$")),
    str(input("\n Digite o nome do produto: ")).strip().upper(),
    float(input("\n Digite seu preço: R$")),
    str(input("\n Digite o nome do produto: ")).strip().upper(),
    float(input("\n Digite seu preço: R$")))

tupla = (numeros)
print("\n" + "=" * 40)
print(f'{"PRODUTO"}{"PREÇO"}')
print("=" * 40)

for item in numeros:
    if contador % 2 == 0: ## se for par, mostra o nome do produto
        print(f"{item:<30}", end="")
    else: ## se for ímpar; seu preço
        print(f"R$ {item:>7.2f}")
    contador += 1
print("=" * 40)