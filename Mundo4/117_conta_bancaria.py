from cores import *

class ContaBancaria:
    def __init__(self, id, titular, saldo=0):
        self.id = id
        self.titular = titular
        self.saldo = saldo

    def __str__(self):
        return f"""{CinzaClaro}O id da sua conta é: {self.id}, seu saldo é de: {Verde}R${Reset}{CinzaClaro}{self.saldo:.2f}\n
        Títular: {self.titular}{Reset}"""

    def depositar(self, valor):
        self.saldo+=valor
        print(f"{CinzaClaro}O Depósito no valor de: {Verde}R${Reset}{CinzaClaro}{valor:.2f} foi autorizado✅{Reset}")

    def sacar(self, valor):
        if(valor>self.saldo):
            print(f"{Vermelho}Voce está tentando sacar {Verde}R${Reset}{CinzaClaro}{valor:.2f}{Vermelho}, mas seu saldo NÃO É suficiente!❌{Reset}")
        else:
            self.saldo-=valor
            print(f"{CinzaClaro}O Saque no valor de: {Verde}R${Reset}{CinzaClaro}{valor:.2f} foi autorizado✅{Reset}")

conta1 = ContaBancaria(id=1, titular="Lucas Paguetti", saldo=3000)

print(f"\n {conta1} \n")
conta1.depositar(valor=500)

print(f"\n {CinzaClaro}Após o Depósito, o saldo é de: {Verde}R${Reset}{CinzaClaro}{conta1.saldo:.2f}{Reset} \n")
conta1.sacar(valor=2000)

print(f"\n {CinzaClaro}Após o Saque, o saldo é de: {Verde}R${Reset}{CinzaClaro}{conta1.saldo:.2f}{Reset} \n")