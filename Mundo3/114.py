#Crie um código em Python que teste se o site: https://www.pudim.com.br ; 
# está acessível pelo computador usado.

#Reslução:
import urllib.request
import urllib.error
from cores import(Verde,Vermelho,Reset)

site = "https://www.pudim.com.br"
try:
    urllib.request.urlopen(site)
    print(f"\n {Verde}✅ O site pudim.com.br está acessível! {Reset} \n")
except urllib.error.URLError:
    print(f"\n ❌ {Vermelho}O site pudim.com.br NÃO está acessível! {Reset} \n")