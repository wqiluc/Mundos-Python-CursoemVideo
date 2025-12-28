#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
#Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

#Reslução:

palavras = (
    "aprender",
    "progrmar",
    "linguagem",
    "python",
    "futuro")

print("\n",palavras)

print(f"\n Na palavra: {palavras[0]}, temos: {palavras[0].count("a")} a",  
      {palavras[0].count("e")}, "e", {palavras[0].count("i")}, "i",  
    {palavras[0].count("o")}, "o",  {palavras[0].count("u")}, "u")

print(f"\n Na palavra: {palavras[1]}, temos: temos: {palavras[1].count("a")} a",  
      {palavras[1].count("e")}, "e", {palavras[1].count("i")}, "i",  
    {palavras[1].count("o")}, "o",  {palavras[1].count("u")}, "u")

print(f"\n Na palavra: {palavras[2]}, temos: temos: {palavras[2].count("a")} a",  
      {palavras[2].count("e")}, "e", {palavras[2].count("i")}, "i",  
    {palavras[2].count("o")}, "o",  {palavras[2].count("u")}, "u")
print(f"\n Na palavra: {palavras[3]}, temos: temos: {palavras[3].count("a")} a",  
      {palavras[3].count("e")}, "e", {palavras[3].count("i")}, "i",  
    {palavras[3].count("o")}, "o",  {palavras[3].count("u")}, "u")

print(f"\n Na palavra: {palavras[4]}, temos: temos: {palavras[4].count("a")} a",  
      {palavras[4].count("e")}, "e", {palavras[4].count("i")}, "i",  
    {palavras[4].count("o")}, "o",  {palavras[4].count("u")}, "u", "\n")