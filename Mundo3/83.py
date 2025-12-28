#Crie um programa onde o usuário digite 
# uma expressão qualquer que use parênteses. 
# Seu aplicativo deverá analisar 
# se a expressão passada está com os parênteses 
# abertos e fechados na ordem correta.

#Reslução:
from cores import(Negrito,Reset,Vermelho,Verde)

expressao = str(input(f"\n {Negrito}Digite uma expressão: {Reset}"))
if not f"((({expressao})))":
    print(f"\n {Vermelho}Sua expressão está incorreta! ❌{Negrito}")
else:
    print(f"\n {Verde}Sua expressão está correta! ✅{Negrito} \n")