from rich.console import Console
from rich.panel import Panel
from rich.text import Text

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

class Gamer:
    def __init__(self, nome: str, nick: str, jogos_favoritos: list) -> None:
        self.nome = nome
        self.nick = nick
        self.jogos = jogos_favoritos

    def ficha_gamer(self):
        jogos_formatados = "\n".join(f"  • {jogo}" for indice_jogo, jogo in enumerate(self.jogos))
        console.print(Panel
        (
            f"[bold #3B82F6]Nome:[/bold #3B82F6] {self.nome}\n"
            f"[bold #3B82F6]Nick:[/bold #3B82F6] {self.nick}\n"
            f"[bold #3B82F6]Jogos Favoritos:[/bold #3B82F6]\n{jogos_formatados}",
            title="[bold #FFA500]FICHA DO GAMER[/bold #FFA500]",
            border_style="#FFA500",
            style="on #111827",
            padding=(1, 2),
        ))

    def etiqueta(self):
        conteudo = Text(justify="center")
        conteudo.append(f"{self.nick}\n", style="bold #FFA500")
        conteudo.append(self.nome, style="#3B82F6")
        console.print(Panel.fit
        (
            conteudo,
            border_style="#3B82F6",
            style="on #111827",
            padding=(1, 4),
        ))

gamers = [
    Gamer("Ana Souza", "AnaFire", ["Valorant", "League of Legends", "Overwatch 2"]),
    Gamer("Bruno Lima", "BrunoBlade", ["Elden Ring", "Dark Souls III"]),
    Gamer("Carla Nunes", "CarlaNova", ["Minecraft", "Stardew Valley", "Terraria"]),
]

for indice_gamer, gamer in enumerate(gamers):
    print(f"{indice_gamer+1} - ")
    gamer.ficha_gamer()