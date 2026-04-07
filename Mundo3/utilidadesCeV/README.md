<h1 align="center">
UtilidadesCeV - Pacote de Exercícios 107 a 110; <br>
Mundo3 🐍🌍
</h1>

<p align="center">
 <img src="../../img/cursoemvideo1.jpeg" alt="Curso em video Logo">
 <br> <br>
 <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" width="60" style="vertical-align: middle;">
 <br>
</p>

Este pacote contém os módulos desenvolvidos durante os exercícios: ```.py```: <br> 
107 a 110; do Curso em Vídeo de ```Python3```, organizados para estudo e execução prática.📂🔗

<h1 align="center">
1. Estrutura do pacote: 📂
</h1>

```
Mundo3/
├── utilidadesCeV/
│   ├── __init__.py
│   ├── README_utilidadesCeV.md
│   ├── cores.py
│   ├── dados/
│   │   ├── __init__.py
│   │   ├── centoesete.py
│   │   ├── centoeoito.py
│   │   ├── centonove.py
│   │   ├── centodez.py
│   └── moeda/
│       ├── __init__.py
│       ├── centoesetemoeda.py
│       ├── centoeoitomoeda.py
│       ├── centoenovemoeda.py
│       ├── centoedezmoeda.py
```

<h1 align="center">
2. Como rodar os arquivos: ⚙️
</h1>

### Passo 1: Abrir o terminal e acessar a pasta `Mundo3`

Abra o terminal e navegue até a pasta `Mundo3`:

```bash
cd "/Users/seu_usuario/Library/Mobile Documents/Sua Pasta usual/Mundos Python - Guanabara/Mundo3"
```

Verifique se o pacote está presente:

```bash
ls (ou list) (listar) -  ele verifica o que tem na sua pasta
```

**Deve mostrar🔍👁️‍🗨️**:


utilidadesCeV 📂 <br>
cores.py<img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" width="20" height="20" style="vertical-align: middle; margin-left: 5px;"> <br>
72.py até o 114.py<img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" width="20" height="20" style="vertical-align: middle; margin-left: 5px;"> <br>
(e seus ```Docstrings 💉```)


> 💡 **Dica:** Sempre acesse `Mundo3` com `cd Mundo3` **antes** de rodar os módulos.

### Passo 2: Executar arquivos com Python usando `-m` ⚡

Para rodar qualquer arquivo dentro da pasta `dados`:

```bash
python3 -m utilidadesCeV.dados.centoesete
python3 -m utilidadesCeV.dados.centoeoito
python3 -m utilidadesCeV.dados.centoenove
python3 -m utilidadesCeV.dados.centoedez
```

**⚠️Observações importantes:**

* `-m` permite que o Python trate o arquivo como módulo do pacote, garantindo que imports relativos (`..`) funcionem.
* Nunca execute diretamente (`python3 arquivo.py`) arquivos com imports relativos.

<br>

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" width="100">
</p>