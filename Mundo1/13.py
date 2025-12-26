#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, 
# com 15% de aumento.

#Resolução:

salárioantigo = float(input("\n Digite o salário atual do funcionário: R$"))
reajuste = (salárioantigo)+(0.15*salárioantigo)
print(f"\n O antigo salário de: R${salárioantigo}, passa agora a ser de: R${reajuste:.2f}\n ")
