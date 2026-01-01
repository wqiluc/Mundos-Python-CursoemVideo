#Modifique as funções que form criadas no desafio 107 
# para que elas aceitem um parâmetro a mais, 
# informando se o valor retornado por elas 
# vai ser ou não formatado pela função moeda(), 
# desenvolvida no desafio 108.

#Reslução:
from ..cores import Negrito, Reset, Verde, Magenta
from ..moeda import centoenovemoeda

valor = centoenovemoeda.leiadinheiro()

print(
    f"\n {Negrito}Aumento:{Reset} "
    f"O aumento de {Magenta}R${valor:.2f}{Reset} é = "
    f"{Verde}{centoenovemoeda.aumentar(valor, True)}{Reset}")

print(
    f"\n {Negrito}Diminuição:{Reset} "
    f"Uma diminuição de {Magenta}R${valor:.2f}{Reset} é = "
    f"{Verde}{centoenovemoeda.diminuir(valor, True)}{Reset}")

print(
    f"\n {Negrito}Metade:{Reset} "
    f"A metade de {Magenta}R${valor:.2f}{Reset} é = "
    f"{Verde}{centoenovemoeda.metade(valor, True)}{Reset}")

print(
    f"\n {Negrito}Dobro:{Reset} "
    f"O dobro de {Magenta}R${valor:.2f}{Reset} é = "
    f"{Verde}{centoenovemoeda.dobrar(valor, True)}{Reset}")