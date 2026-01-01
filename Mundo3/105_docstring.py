from cores import(Azul,Amarelo,Magenta,Reset,Vermelho,Verde)

print(f"""
{Azul}DOCSTRINGS 💉 – FUNÇÃO notas(📚){Reset}

{Magenta}Este programa tem como objetivo criar uma função chamada{Reset}
{Amarelo}notas(){Reset}{Magenta}, responsável por receber várias notas de alunos
e realizar a análise do desempenho da turma.{Reset}

{Magenta}A função executa as seguintes tarefas:{Reset}
{Magenta}• Validação dos dados de entrada do aluno;{Reset}
{Magenta}• Cálculo da média individual;{Reset}
{Magenta}• Identificação da situação do aluno;{Reset}
{Magenta}• Armazenamento das informações coletadas.{Reset}

{Magenta}A função{Reset} {Amarelo}notas(){Reset} {Magenta}pode receber múltiplos alunos
até que o usuário decida encerrar a inserção de dados.{Reset}

{Magenta}Situação do aluno baseada na média:{Reset}
{Magenta}→ Média menor ou igual a 5:{Reset} {Vermelho}REPROVADO{Reset}
{Magenta}→ Média maior que 5 e menor ou igual a 6:{Reset} {Amarelo}RECUPERAÇÃO{Reset}
{Magenta}→ Média acima de 6:{Reset} {Verde}APROVADO{Reset}

{Magenta}Bibliotecas utilizadas:{Reset}
{Magenta}• Módulo{Reset} {Amarelo}cores{Reset}{Magenta} para estilização do terminal.{Reset}""")