# Aula extra - Rich: erros bonitos (traceback) + inspect em uma @property
# Complementa 118.py mostrando o "Bônus" da BIBLIOTECA_RICH.md (seção 9):
# - rich.traceback.install(): deixa exceções não tratadas mais legíveis no terminal
# - rich.inspect(): explora atributos/métodos de um objeto de forma formatada

from rich import print
from rich import inspect
from rich.traceback import install

install()  # a partir daqui, qualquer exceção não tratada aparece formatada pela Rich


class ContaBancaria:
    def __init__(self, id, titular, saldo):
        self.id = id
        self.titular = titular
        self._saldo = saldo  
        # "privado": só muda pelo setter da property, que valida o valor

    @property  # transforma o método abaixo em getter: permite ler "conta.saldo" como atributo, sem usar ()
    def saldo(self):
        return self._saldo

    @saldo.setter  # associa este método como o setter de "saldo": roda quando se faz "conta.saldo = valor"
    def saldo(self, valor):
        if (valor < 0):
            raise ValueError(f"Saldo não pode ser negativo (tentou definir {valor})")
        self._saldo = valor

    def __str__(self):
        return f"Id: {self.id} - Conta de {self.titular}: R$ {self.saldo:.2f}"


conta1 = ContaBancaria(111,"Lucas", 150.0)
print(f"[bold cyan]{conta1}[/bold cyan]")

# inspect: mostra atributos, métodos e a própria @property "saldo", tudo formatado
inspect(conta1, methods=True)

# Erro proposital: definir um saldo negativo passa pelo setter da property, que levanta ValueError.
# Como não há try/except aqui, a Rich intercepta a exceção e imprime o traceback formatado
# (graças ao install() lá em cima), em vez do traceback cru do Python.
conta1.saldo = -500