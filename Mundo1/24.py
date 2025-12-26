#Crie um programa que leia o nome de uma cidade 
# e diga se ela começa ou não com o nome "SANTO".

#Resolução:
cidade = str(input("\n Digite o nome da sua cidade: ")).strip().upper()

print(f"Há a palavra 'SANTO' na sua cidade? {cidade[0:5].upper() == "SANTO"[0:5].upper()} \n")

