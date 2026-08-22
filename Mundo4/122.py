from rich.console import Console
from rich.panel import Panel

console = Console()

console.print(Panel
(
    "Crie a classe [bold #FFA500]Livro[/bold #FFA500], que vai simular a "
    "[bold #3B82F6]passagem de páginas[/bold #3B82F6] de um livro, considerando também se o "
    "usuário [bold #3B82F6]chegou ao fim[/bold #3B82F6] da leitura.",
    title="[bold #FFA500]DESAFIO 019[/bold #FFA500]",
    border_style="#FFA500",
    style="on #111827",
    padding=(1, 2),
))

class Livro:
    def __init__(self, titulolivro: str, paginaatual: int, totalpaginas: int, pularpagina: int) -> None:
        self.titulolivro = titulolivro
        self.totalpaginas = totalpaginas
        self.paginaatual = paginaatual
        self.pularpagina = pularpagina

    def pular_pagina(self):
        self.paginaatual += self.pularpagina
        self.pularpagina = self.paginaatual+1
        if (self.paginaatual >= self.totalpaginas):
            self.paginaatual = self.totalpaginas
            return (
                f"Você chegou ao fim do livro [bold #3B82F6]'{self.titulolivro}'[/bold #3B82F6]! "
                f"([bold #3B82F6]{self.paginaatual}/{self.totalpaginas}[/bold #3B82F6] páginas)"
            )
        else:
            return (
                f"Você está lendo o livro [bold #3B82F6]'{self.titulolivro}'[/bold #3B82F6] e está na "
                f"página [bold #3B82F6]{self.paginaatual}[/bold #3B82F6] de [bold #3B82F6]{self.totalpaginas}[/bold #3B82F6]"
            )

livros = [
    Livro("Dom Casmurro", 0, 120, 30),
    Livro("O Hobbit", 0, 310, 80),
    Livro("1984", 0, 260, 90),
    Livro("O Pequeno Príncipe", 0, 96, 40),
    Livro("Harry Potter e a Pedra Filosofal", 0, 223, 60),
]


for indice_livro, livro in enumerate(livros):
    while (livro.paginaatual < livro.totalpaginas):
        console.print(Panel
        (
            livro.pular_pagina(),
            title=f"[bold #FFA500]LIVRO {indice_livro+1}[/bold #FFA500]",
            border_style="#FFA500",
            style="on #111827",
            padding=(1, 2),
        ))