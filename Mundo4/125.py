from rich.console import Console
from rich.panel import Panel

console = Console()

console.print(Panel
(
    "Crie a classe [bold #FFA500]ControleRemoto[/bold #FFA500], onde vamos simular o "
    "funcionamento de um controle simples ([bold #3B82F6]canal[/bold #3B82F6], "
    "[bold #3B82F6]volume[/bold #3B82F6] e [bold #3B82F6]liga/desliga[/bold #3B82F6])",
    title="[bold #FFA500]DESAFIO 022[/bold #FFA500]",
    border_style="#FFA500",
    style="on #111827",
    padding=(1, 2),
))