#Escreva um programa que leia um valor em metros e o exiba convertido em:
# centímetros e milímetros.

#Resolução:

medida = int(input("\n Digite sua medida (em m): "))

#Conversões:

km = medida/1000
hm = medida/100
dam = medida/10
print(f"\n {medida}m equivalem a {km}km")
print(f"\n {medida}m equivalem a {hm}hm")
print(f"\n {medida}m equivalem a {dam}dam")

print("\n ============== \n")

dm = medida*10
cm = medida*100
mm = medida*1000
print(f"\n {medida}m equivalem a {dm}dm")
print(f"\n {medida}m equivalem a {cm}cm")
print(f"\n {medida}m equivalem a {mm}mm\n \n")
