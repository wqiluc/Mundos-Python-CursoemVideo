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
