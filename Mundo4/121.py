from rich.console import Console
from rich.panel import Panel
from cores import CinzaClaro, Reset

console = Console()

console.print(Panel
(
    "Crie a classe [bold #FFA500]Churrasco[/bold #FFA500], onde seja possível informar "
    "[bold #3B82F6]quantas pessoas[/bold #3B82F6] vão participar e mostre "
    "[bold #3B82F6]quanto de carne[/bold #3B82F6] deve ser comprado, o "
    "[bold #3B82F6]custo total[/bold #3B82F6] do churrasco e o "
    "[bold #3B82F6]preço por pessoa[/bold #3B82F6].",
    title="[bold #FFA500]DESAFIO 018[/bold #FFA500]",
    border_style="#FFA500",
    style="on #111827",
    padding=(1, 2),
))

class ChurrascoPython:
    def __init__(self, pessoas: int, carne_por_pessoa: float, preco_kg_carne: float) -> None:
        self.pessoas = pessoas
        self.carne_por_pessoa = carne_por_pessoa
        self.preco_kg_carne = preco_kg_carne
        self.carnetotal = self.pessoas * self.carne_por_pessoa
        self.custototal = self.carnetotal * self.preco_kg_carne
        self.precoporpessoa = self.custototal / self.pessoas

    def convite_churrasco(self):
        console.print(Panel
        (
            "Olá, pessoal!! Estão convidados para o meu churrasco Python!\n\n"
            f"[bold #3B82F6]Data:[/bold #3B82F6] 01/09/2026\n"
            f"[bold #3B82F6]Máximo de Pessoas:[/bold #3B82F6] {self.pessoas}\n"
            f"[bold #3B82F6]Total de Carne necessário:[/bold #3B82F6] {self.carnetotal:.2f} kg\n"
            f"[bold #3B82F6]Custo Total do Churrasco:[/bold #3B82F6] R$ {self.custototal:.2f}\n"
            f"[bold #3B82F6]Custo por Pessoa:[/bold #3B82F6] R$ {self.precoporpessoa:.2f}\n\n"
            "Espero que gostem!! :) Vejo vocês lá!!",
            title="[bold #FFA500]CONVITE CHURRASCO[/bold #FFA500]",
            border_style="#FFA500",
            style="on #111827",
            padding=(1, 2),
        ))

dados_convidados = [
    ("Ana",),
    ("Bruno",),
    ("Carla",),
    ("Diego",),
    ("Elisa",),
]

lista_convidados_confirmados = [dados_convidados[indice_convidado][0] for indice_convidado in range(0, len(dados_convidados[0:]))]

churrasco = ChurrascoPython(
    pessoas=len(lista_convidados_confirmados[0:]),
    carne_por_pessoa=2.0,
    preco_kg_carne=90.00,
)

for indice_convidado, convidado in enumerate(lista_convidados_confirmados):
    print(f"\n{CinzaClaro}{indice_convidado+1}º Convidado(a) - {convidado}{Reset}")
churrasco.convite_churrasco()