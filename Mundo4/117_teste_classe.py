# Documentação de Classes (docstrings e o atributo especial __doc__)

from cores import *

class Pessoa:
    """
    Classe Pessoa: representa uma pessoa com nome e idade.
    Atributos:
        nome (str): nome da pessoa.
        idade (int): idade da pessoa.
    Métodos:
        aniversario(): incrementa a idade em 1 ano.
    """

    def __init__(self, nome, idade):
        """Construtor: inicializa os atributos nome e idade."""
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        """Incrementa a idade da pessoa em 1 ano."""
        self.idade += 1


print(f"\n{CinzaClaro}A {Amarelo}docstring{CinzaClaro} é um texto de documentação escrito entre "
      f"{Magenta}três aspas{CinzaClaro} logo abaixo da declaração de uma {Amarelo}classe{CinzaClaro}, "
      f"{Amarelo}método{CinzaClaro} ou {Amarelo}função{CinzaClaro}.{Reset}")

print(f"\n{CinzaClaro}Ela fica guardada no atributo especial {Magenta}__doc__{CinzaClaro} "
      f"e pode ser consultada de duas formas:{Reset}")

print(f"{CinzaClaro}1) Direto pelo atributo: {Magenta}Pessoa.__doc__{Reset}")
print(f"{CinzaClaro}2) Usando a função nativa: {Magenta}help(Pessoa){Reset}")

print(f"\n{CinzaClaro}Documentação da {Amarelo}classe{CinzaClaro} Pessoa:{Reset}")
print(f"{CinzaClaro}{Pessoa.__doc__}{Reset}")

print(f"{CinzaClaro}Documentação do {Amarelo}método{CinzaClaro} __init__:{Reset}")
print(f"{CinzaClaro}{Pessoa.__init__.__doc__}{Reset}")

print(f"{CinzaClaro}Documentação do {Amarelo}método{CinzaClaro} aniversario:{Reset}")
print(f"{CinzaClaro}{Pessoa.aniversario.__doc__}{Reset}")

pessoa = Pessoa("Lucas", 22)
print(f"\n{CinzaClaro}Também dá pra consultar a partir do {Amarelo}objeto{CinzaClaro} já instanciado, "
      f"com {Magenta}pessoa.__doc__{CinzaClaro}:{Reset}")
print(f"{CinzaClaro}{pessoa.__doc__}{Reset}")


# ---------------------------------------------------------------------------
# __dict__: o "estado" de um objeto/classe é armazenado em um dicionário
# ---------------------------------------------------------------------------

print(f"\n{CinzaClaro}Todo {Amarelo}objeto{CinzaClaro} guarda seus atributos em um dicionário interno, "
      f"acessível por {Magenta}objeto.__dict__{CinzaClaro}. É esse dicionário que representa o "
      f"{Amarelo}estado{CinzaClaro} do objeto:{Reset}")
print(f"{CinzaClaro}pessoa.__dict__ = {Verde}{pessoa.__dict__}{Reset}")

pessoa.aniversario()
print(f"\n{CinzaClaro}Depois de {Magenta}pessoa.aniversario(){CinzaClaro}, o estado do objeto muda "
      f"(o valor de {Amarelo}idade{CinzaClaro} dentro do __dict__ é atualizado):{Reset}")
print(f"{CinzaClaro}pessoa.__dict__ = {Verde}{pessoa.__dict__}{Reset}")

print(f"\n{CinzaClaro}A {Amarelo}classe{CinzaClaro} também tem seu próprio {Magenta}__dict__{CinzaClaro}, "
      f"mas nele ficam os {Amarelo}métodos{CinzaClaro}, {Amarelo}docstring{CinzaClaro} e atributos de classe "
      f"(não os atributos de cada instância):{Reset}")
for chave in Pessoa.__dict__:
    print(f"{CinzaClaro} - {Amarelo}{chave}{Reset}")


# ---------------------------------------------------------------------------
# __str__: como o objeto se transforma em texto (print, str(), f-string)
# ---------------------------------------------------------------------------

print(f"\n{CinzaClaro}Sem um método {Magenta}__str__{CinzaClaro} definido, {Magenta}print(objeto){CinzaClaro} "
      f"mostra algo genérico, com o endereço em memória:{Reset}")
print(f"{CinzaClaro}print(pessoa) -> {Verde}{pessoa}{Reset}")


class PessoaComStr(Pessoa):
    """Mesma Pessoa, mas com __str__ sobrescrito para exibir o estado do objeto."""

    def __str__(self):
        return f"Pessoa(nome={self.nome!r}, idade={self.idade})"

pessoa_str = PessoaComStr("Ana", 30)
print(f"\n{CinzaClaro}Definindo {Magenta}__str__{CinzaClaro} na classe, {Magenta}print(objeto){CinzaClaro} "
      f"passa a mostrar o {Amarelo}estado{CinzaClaro} de forma legível:{Reset}")
print(f"{CinzaClaro}print(pessoa_str) -> {Verde}{pessoa_str}{Reset}")

pessoa_str.aniversario()
print(f"{CinzaClaro}Depois do aniversário, o {Amarelo}__str__{CinzaClaro} reflete o novo estado:{Reset}")
print(f"{CinzaClaro}print(pessoa_str) -> {Verde}{pessoa_str}{Reset}")

# ---------------------------------------------------------------------------
# Estados independentes: cada instância tem seu próprio __dict__
# ---------------------------------------------------------------------------

outra_pessoa = Pessoa("Maria", 40)
print(f"\n{CinzaClaro}Cada {Amarelo}instância{CinzaClaro} tem seu próprio {Magenta}__dict__{CinzaClaro}, "
      f"ou seja, seu próprio {Amarelo}estado{CinzaClaro}, independente das outras:{Reset}")
print(f"{CinzaClaro}pessoa.__dict__       = {Verde}{pessoa.__dict__}{Reset}")
print(f"{CinzaClaro}outra_pessoa.__dict__ = {Verde}{outra_pessoa.__dict__}{Reset}")