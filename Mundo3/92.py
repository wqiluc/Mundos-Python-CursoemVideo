#Crie um programa que leia nome, ano de nascimento 
# e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
#Se por acaso a CTPS for diferente de ZERO, 
# o dicionário receberá também o ano de contratação e o salário. 
#Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

#Reslução:
from cores import(Negrito,Reset,Verde,Amarelo,Vermelho)
from datetime import datetime
info_trabalhador = {
    "Nome": str(input(f"\n {Negrito}Digite o nome do trabalhador: {Reset}")).upper().strip(),
    "CTTPS": int(input(f"\n {Negrito}O cidadão tem CTTPS? [1 = S / 0 = N] {Reset}")),
    "Ano_Nascimento": int(input(f"\n {Negrito}Digite o ano de nascimento do cidadão: {Reset}")),
}

idade = datetime.today().year - info_trabalhador["Ano_Nascimento"]

if info_trabalhador["CTTPS"] == 0:
    print(f"\n{Amarelo} Nome = {info_trabalhador['Nome']} {Reset}")
    print(f"\n {Amarelo}Idade = {idade}\n {Reset}")
    print(f"{Vermelho} CTTP = INÁTIVO ❌ {Reset}")
else:
    info_trabalhador["ano_contratacao"] = int(input(f"{Negrito}Digite o ano de Contratação: {Reset}"))
    info_trabalhador["salario"] = int(input(f"{Negrito}Digite o ano salário do funcionário: {Reset}{Verde}R${Reset}"))
    print(f"\n{Amarelo} Nome = {info_trabalhador['Nome']} {Reset}")
    print(f"\n {Amarelo}Idade = {idade}\n {Reset}")
    print(f"{Verde} CTTP = ATIVO DESDE {info_trabalhador['ano_contratacao']} ✅ {Reset}")
    print(f"Salário {Verde}(R$){Reset} = {info_trabalhador['salario']}")
    aposentadoria = info_trabalhador["ano_contratacao"] + 35
    print(f"{Negrito}Tende a se aposentar em: {aposentadoria}{Reset} \n")