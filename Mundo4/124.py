from rich.console import Console
from rich.panel import Panel

console = Console()

console.print(Panel(
    "Crie a classe [bold #FFA500]Caneta[/bold #FFA500], que simule o funcionamento de uma "
    "[bold #3B82F6]caneta colorida[/bold #3B82F6], podendo "
    "[bold #3B82F6]escrever[/bold #3B82F6] frases na cor relativa.",
    title="[bold #FFA500]DESAFIO 021[/bold #FFA500]",
    border_style="#FFA500",
    style="on #111827",
    padding=(1, 2),
))
