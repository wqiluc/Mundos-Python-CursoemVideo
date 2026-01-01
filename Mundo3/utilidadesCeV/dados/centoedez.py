#Adicione o módulo moeda.py criado nos desafios anteriores, 
# uma função chamada resumo(), 
# que mostre na tela algumas informações geradas 
# pelas funções que já temos no módulo criado até aqui.

#Reslução:
from ..cores import Negrito, Reset, Vermelho
from ..moeda import centoedezmoeda

valor = centoedezmoeda.leiadinheiro()
centoedezmoeda.resumo(valor)
