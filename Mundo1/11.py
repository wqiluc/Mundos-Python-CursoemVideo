#Faça um programa que leia a largura e a altura de uma parede em metros, 
# calcule a sua área e a quantidade de tinta necessária para pintá-la, 
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

#Resolução:

largura_parede = float(input("\nDigite a largura da parede: "))
altura_parede =  float(input("\nDigite a altura da parede: "))
area = largura_parede*altura_parede
litrostinta = area/2
print(f"\n As dimensões da sua parede são: \n Largura = {largura_parede}m x Altura = {altura_parede}m, o que dá um resultado de {area:.2f}m²")
print(f"\n Tendo esse resultado, você precisaria de {litrostinta:.0f} L de Tinta")