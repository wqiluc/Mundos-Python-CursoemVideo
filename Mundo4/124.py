from rich.console import Console
from rich.panel import Panel
from time import sleep

console = Console()

console.print(Panel
(
    "Crie a classe [bold #FFA500]Caneta[/bold #FFA500], que simule o funcionamento de uma "
    "[bold #3B82F6]caneta colorida[/bold #3B82F6], podendo "
    "[bold #3B82F6]escrever[/bold #3B82F6] frases na cor relativa.",
    title="[bold #FFA500]DESAFIO 021[/bold #FFA500]",
    border_style="#FFA500",
    style="on #111827",
    padding=(1, 2),
))

class Canetascoloridas:
    def __init__(self, texto: str, cor: str) -> None:
        self.texto = texto
        self.cor = cor

    def colir_texto(self) -> str:
        return f"Texto {self.texto} colorido com a cor: {self.cor}"

cores_textos = [
    ("Vermelho", "red", "Escrevendo com a caneta vermelha!"),
    ("Azul", "blue", "Escrevendo com a caneta azul!"),
    ("Verde", "green", "Escrevendo com a caneta verde!"),
    ("Amarelo", "yellow", "Escrevendo com a caneta amarela!"),
    ("Roxo", "magenta", "Escrevendo com a caneta roxa!"),
]

for indice, (cor, estilo, texto) in enumerate(cores_textos, start=1):
    caneta = Canetascoloridas(texto=texto, cor=cor)
    console.print(f"{indice}. {caneta.colir_texto()}", style=estilo)
    sleep(1.1)