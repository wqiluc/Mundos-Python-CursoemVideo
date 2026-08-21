from rich.console import Console
from rich.panel import Panel

console = Console()

console.print(Panel
(
    "Crie a classe [bold #FFA500]Gamer[/bold #FFA500], onde podemos cadastrar "
    "[bold #3B82F6]nome[/bold #3B82F6], [bold #3B82F6]nick[/bold #3B82F6] e os "
    "[bold #3B82F6]jogos favoritos[/bold #3B82F6] de uma pessoa. Crie também um "
    "[bold #FFA500]método[/bold #FFA500] que permita mostrar a "
    "[bold #3B82F6]ficha[/bold #3B82F6] desse gamer.",
    title="[bold #FFA500]DESAFIO 020[/bold #FFA500]",
    border_style="#FFA500",
    style="on #111827",
    padding=(1, 2),
))
