#Faça um mini-sistema que utilize o 
# Interactive Help do Python. 
#O usuário vai digitar o comando 
#e o manual vai aparecer. 
#Quando o usuário digitar a palavra ‘FIM’,
#o programa se encerrará. 
#IMPORTANTE: use cores(from cores import ( . . . ) ).

#Reslução:
from cores import(Reset,Amarelo,Azul,Vermelho)

def interactive_help_Python():
    
    comandos = [
        "print", "input", "len", "type", "int", "float", "str", "bool",
        "list", "tuple", "set", "dict",
        "range", "enumerate", "zip",
        "sum", "max", "min", "sorted",
        "abs", "round", "pow",
        "open", "help", "dir",
        "map", "filter", "lambda",
        "any", "all",
        "isinstance", "id",
        "eval", "exec"]
    print(f"{Amarelo}Comandos Disponíveis: {Reset}")
    print(" .".join(comandos))
    comando = str(input(f"{Azul}Digite o Comando que quer análisar? 📊: {Reset}")).strip().lower()
    if comando == "fim":
        print(f"\n {Vermelho}FIM DO PROGRAMA!! ❌ {Reset} \n")
        return
    else:
        for comando in comandos:
            print(f"{Amarelo}=={Reset}"*15)
            help(eval(comando))
            print(f"{Amarelo}=={Reset}"*15)
            return interactive_help_Python()
interactive_help_Python()