# Declaração de Classe

class MinhaPrimeiraClasse:
    def __init__(self, nome, idade): 
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        self.idade += 1

    def mensagem(self, nome, idade):
        return f"Feliz aniversário!!, {nome}. Parabéns pelos {idade} de idade!"

usuario_a = MinhaPrimeiraClasse("Maria", 17)
usuario_b = MinhaPrimeiraClasse("Lucas", 21)
usuario_c = MinhaPrimeiraClasse("Ruan", 33)

lista_usuarios = [usuario_a, usuario_b, usuario_c]

for indice_usuario, usuario in enumerate(lista_usuarios):
    print(f"\n {indice_usuario+1}º Usuário: {usuario.mensagem(usuario.nome, usuario.idade)}")