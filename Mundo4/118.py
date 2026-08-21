# Aula extra - Biblioteca Rich
# Rich é uma biblioteca para deixar a saída no terminal mais bonita e legível:
# textos coloridos/formatados, tabelas, progresso, painéis, tracebacks, etc.
# Instalação: pip install rich

from rich import print
from rich import inspect
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import track
from time import sleep

console = Console()

# print() do rich aceita marcações de estilo dentro da própria string
print("[bold green]Sucesso![/bold green] Biblioteca [italic cyan]Rich[/italic cyan] instalada e funcionando. ✅")

# console.print() é equivalente ao print(), mas pelo objeto Console
console.print("Texto com fundo colorido", style="white on blue")

# Panel: emoldura um texto/conteúdo com título e borda
console.print(Panel("Painel de destaque com borda e título", title="Aviso", border_style="magenta"))

# Table: monta tabelas formatadas no terminal
tabela = Table(title="Usuários cadastrados")
tabela.add_column("Nome", style="cyan", justify="left")
tabela.add_column("Idade", style="green", justify="center")

tabela.add_row("Lucas", "22")
tabela.add_row("Maria", "30")
tabela.add_row("Ruan", "53")

console.print(tabela)

# track: gera uma barra de progresso automática ao iterar
for indice_, _ in enumerate(track(range(5), description="Processando...")):
    sleep(0.2)

console.print("\n[bold yellow]Fim da demonstração da Rich![/bold yellow]")

# inspect: mostra de forma formatada os atributos, métodos e docstring de um objeto/classe
# all=True exibe também os métodos e atributos "privados" (que começam com _)
inspect(int, all=True)