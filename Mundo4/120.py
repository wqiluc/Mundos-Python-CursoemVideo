from rich.console import Console
from rich.panel import Panel

console = Console()

console.print(Panel
(
    "Crie a classe [bold #FFA500]Produto[/bold #FFA500], onde podemos cadastrar "
    "[bold #3B82F6]nome[/bold #3B82F6] e o [bold #3B82F6]preço[/bold #3B82F6]. Crie também um "
    "[bold #FFA500]método[/bold #FFA500] que mostre uma [bold #3B82F6]etiqueta de preço[/bold #3B82F6] "
    "do produto.",
    title="[bold #FFA500]DESAFIO 017[/bold #FFA500]",
    border_style="#FFA500",
    style="on #111827",
    padding=(1, 2),
))

class Produto:
    def __init__(self, nome: str, preco: float) -> None:
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        console.print(Panel
        (
            f"[bold #3B82F6]Produto:[/bold #3B82F6] {self.nome}\n"
            f"[bold #3B82F6]Preço:[/bold #3B82F6] R$ {self.preco:.2f}",
            title="[bold #FFA500]ETIQUETA[/bold #FFA500]",
            border_style="#FFA500",
            style="on #111827",
            padding=(1, 2),
        ))

dados_produtos = [
    ("Caneta", 15,00),
    ("Casaco", 150,00),
    ("Celular", 1500,00),
    ("Computador", 6700,00),
]

lista_produtos = []
lista_produtos.extend([Produto(nome=dados_produtos[indice_produto][0], preco=dados_produtos[indice_produto][1]) for indice_produto in range(0, 4)])

for indice_produto, produto in enumerate(lista_produtos):
    print(f"\n{indice_produto+1} - ")
    produto.etiqueta()