from rich.console import Console
from rich.panel import Panel
from cores import CinzaClaro, Reset

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
class ControleRemoto:
    def __init__(self, volume: int, canal: int, ligado: bool) -> None:
        self.volume = volume
        self.canal = canal
        self.ligado = ligado

    def ligar(self):
        self.ligado = True
        console.print("[bold #10B981]O controle foi ligado.[/bold #10B981]")

    def desligar(self):
        self.ligado = False
        console.print("[bold #EF4444]O controle foi desligado.[/bold #EF4444]")

    def aumentar_volume(self):
        if (self.ligado and self.volume < 100):
            self.volume += 1
            console.print(f"[bold #3B82F6]Volume aumentado para {self.volume}[/bold #3B82F6]")

    def diminuir_volume(self):
        if (self.ligado and self.volume > 0):
            self.volume -= 1
            console.print(f"[bold #3B82F6]Volume diminuído para {self.volume}[/bold #3B82F6]")

    def mudar_canal(self, canal: int):
        if (self.ligado and canal > 0):
            self.canal = canal
            console.print(f"[bold #3B82F6]Canal alterado para {self.canal}[/bold #3B82F6]")


lista_controles = []

for indice_controle in range(3):
    controle = ControleRemoto(volume=50, canal=1, ligado=False)
    lista_controles.append(controle)

while True:
    def menu_controle():
        console.print("\n[bold #FFA500]Menu do Controle Remoto[/bold #FFA500]")
        console.print("[bold #3B82F6]1.[/bold #3B82F6] Ligar")
        console.print("[bold #3B82F6]2.[/bold #3B82F6] Desligar")
        console.print("[bold #3B82F6]3.[/bold #3B82F6] Aumentar Volume")
        console.print("[bold #3B82F6]4.[/bold #3B82F6] Diminuir Volume")
        console.print("[bold #3B82F6]5.[/bold #3B82F6] Mudar Canal")
        console.print("[bold #3B82F6]0.[/bold #3B82F6] Sair")

        opcao = str(input(f"{CinzaClaro}Escolha uma opção: {Reset}"))

        while (opcao.isdigit() == False):
            console.print("[bold #EF4444]Opção inválida. Digite um número.[/bold #EF4444]")
            opcao = console.input("[bold #3B82F6]Escolha uma opção: [/bold #3B82F6]")
        return int(opcao)
    
    if __name__ == "__main__":
        opcao = menu_controle()
        if (opcao == 0):
            console.print("\n[bold #10B981]Saindo do programa...[/bold #10B981]")
            break

        elif (opcao == 1):
            for indice_controle, controle in enumerate(lista_controles, start=1):
                print(f"\n{CinzaClaro}{indice_controle}º Controle:{Reset}")
                controle.ligar()

        elif (opcao == 2):
            for indice_controle, controle in enumerate(lista_controles, start=1):
                print(f"\n{CinzaClaro}{indice_controle}º Controle:{Reset}")
                controle.desligar()
    
        elif (opcao == 3):
            for indice_controle, controle in enumerate(lista_controles, start=1):
                print(f"\n{CinzaClaro}{indice_controle}º Controle:{Reset}")
                controle.aumentar_volume()
                
        elif (opcao == 4):
            for indice_controle, controle in enumerate(lista_controles, start=1):
                print(f"\n{CinzaClaro}{indice_controle}º Controle:{Reset}")
                controle.diminuir_volume()

        elif (opcao == 5):
            canal = console.input("[bold #3B82F6]Digite o novo canal: [/bold #3B82F6]")
            while (canal.isdigit() == False):
                console.print("\n[bold #EF4444]Canal inválido. Digite um número.[/bold #EF4444]")
                canal = console.input("[bold #3B82F6]Digite o novo canal: [/bold #3B82F6]")

            for indice_controle, controle in enumerate(lista_controles, start=1):
                print(f"\n{CinzaClaro}{indice_controle}º Controle:{Reset}")
                controle.mudar_canal(int(canal))
        else:
            console.print("\n[bold #EF4444]Opção inválida. Tente novamente.[/bold #EF4444]")