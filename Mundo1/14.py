#Escreva um programa que converta uma temperatura digitando em graus Celsius 
# e converta para graus Fahrenheit.

#Resolução:

celcius = float(input("\n Digite a temperatura em °C: "))
fahrenheit = (celcius*1.8)+32
print(f"\n A temperatura de {celcius}°C é convertida em {fahrenheit}°F \n")