#Crie um programa onde o usuário possa digitar cinco valores numéricos 
# e cadastre-os em uma lista, 
# já na posição correta de inserção (sem usar o sort()). 
# No final, mostre a lista ordenada na tela.

#Reslução:
lista = [ ]
for contagem in range(1,6):
    numero = int(input(f"\n Digite o {contagem}º número: "))
    if len(lista) == 0 or numero > lista[-1]:
        lista.append(numero)
    else:
        posicao = 0
        while posicao == 0:
            if posicao<=0:
                lista.insert(posicao, numero)
                break
            posicao+=1

print(f"Lista = {lista} \n")