# Declaração de Classe

class MinhaPrimeiraClasse:
    def __init__(self):  # Método construtor
        self.nome = "Lucas Paguetti"
        self.idade = 22

    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"Feliz aniversário!!, {self.nome}. Parabéns pelos {self.idade} de idade!"

# Declaração de Objetos (instâncias da classe)

objeto_a = MinhaPrimeiraClasse()
objeto_b = MinhaPrimeiraClasse()
objeto_c = MinhaPrimeiraClasse()
objeto_d = MinhaPrimeiraClasse()

objeto_a.aniversario()

objeto_b.nome = "Ruan"
objeto_b.idade = 53

objeto_c.nome = "Maria"
objeto_c.idade = 30

objeto_d.nome = ""
objeto_d.idade = 0

print(f"\n {objeto_a.mensagem()}")
print(f"{objeto_b.mensagem()}")
print(f"{objeto_c.mensagem()}")
print(f"{objeto_d.mensagem()}")