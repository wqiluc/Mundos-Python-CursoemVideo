from rich.console import Console
from rich.panel import Panel
from cores import *

console = Console()

console.print(Panel
(
    "Crie a classe [bold #FFA500]Funcionario[/bold #FFA500], onde podemos cadastrar "
    "[bold #3B82F6]nome[/bold #3B82F6], [bold #3B82F6]setor[/bold #3B82F6] e "
    "[bold #3B82F6]cargo[/bold #3B82F6]. Crie também um [bold #FFA500]método[/bold #FFA500] "
    "que permita ao funcionário se [bold #3B82F6]apresentar[/bold #3B82F6].",
    title="[bold #FFA500]DESAFIO 016[/bold #FFA500]",
    border_style="#FFA500",
    style="on #111827",
    padding=(1, 2),
))

class Funcionario:
    def __init__(self, id: int, nome: str, setor: str, cargo:str) -> None:
        self.id = id
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    @property
    def apresentacao(self):
        return f"""\n{CinzaClaro}Olá!! meu nome é {self.nome}, meu ID é {self.id}, 
        trabalho na área de {self.setor} e atuo como {self.cargo}{Reset}\n"""

lista_funcionarios = []
func1 = Funcionario(id=1, nome="Lucas Paguetti", setor="Tecnologia", cargo="Análista")
func2 = Funcionario(id=2, nome="Maria Silva", setor="Financeiro", cargo="Gerente")
func3 = Funcionario(id=3, nome="João Souza", setor="Recursos Humanos", cargo="Analista")
func4 = Funcionario(id=4, nome="Ana Costa", setor="Marketing", cargo="Coordenadora")

lista_funcionarios.extend([func1, func2, func3, func4])

for indice_funcionario, funcionario in enumerate(lista_funcionarios):
    print(f"{indice_funcionario+1} - {funcionario.apresentacao}")