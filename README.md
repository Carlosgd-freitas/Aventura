# Aventura

Um jogo de RPG baseado em texto feito do zero na linguagem Python.

<ins>Donwloads:<ins>
<div style="display: inline_block">
<a href="https://github.com/Carlosgd-freitas/Aventura/raw/main/Aventura.exe" download="Aventura.exe" title="Aventura.exe">
  <img align="center" alt="Windows" height="30" width="100" src="https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white"/>
</a>
<a href="https://github.com/Carlosgd-freitas/Aventura/raw/main/Aventura" download="Aventura" title="Aventura">
  <img align="center" alt="Linux" height="30" width="100" src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black"/>
</a>
</div>

***

### Organização do Repositório

A pasta _[areas](https://github.com/Carlosgd-freitas/Aventura/tree/main/areas)_ contém as áreas pelas quais o jogador se encontra, assim como os eventos que podem acontecer nelas.

A pasta _[base](https://github.com/Carlosgd-freitas/Aventura/tree/main/base)_ contém classes e funções básicas, utilizadas no sistema de configurações do jogo e para criar itens, por exemplo.

A pasta _[combate](https://github.com/Carlosgd-freitas/Aventura/tree/main/combate)_ contém funções relacionadas ao sistema de combate.

A pasta _[criaturas](https://github.com/Carlosgd-freitas/Aventura/tree/main/criaturas)_ contém as criaturas presentes no jogo, tais como Slimes e Cobras Venenosas.

A pasta _[habilidades](https://github.com/Carlosgd-freitas/Aventura/tree/main/habilidades)_ contém habilidades, sejam elas passivas ou ativas, como Envenenamento ou Projétil de Mana.

A pasta _[itens](https://github.com/Carlosgd-freitas/Aventura/tree/main/itens)_ contém os itens consumíveis, equipamentos, e espólios de inimigos derrotados.

A pasta _[menus](https://github.com/Carlosgd-freitas/Aventura/tree/main/menus)_ contém os menus relacionados a habilidades, inventário, equipamentos, etc.

A pasta _[sistemas](https://github.com/Carlosgd-freitas/Aventura/tree/main/sistemas)_ contém funções relacionadas aos demais sistemas do jogo, como o sistema de fabricação.

***

### Executando o Jogo

No Windows, dê um clique duplo no executável **Aventura.exe**. O Windows pode alertar que o jogo é um malware já que ele não contém um certificado de segurança. Apenas ignore ou desabilite esse alerta para executar o jogo.

No Linux, execute o comando ```chmod +x Aventura``` para tornar o arquivo executável, e então, o comando ```./Aventura``` para executar o jogo.

Ao executar o jogo pela primeira vez, os diretórios ```bin``` e ```saves``` serão criados. O diretório ```bin``` conterá arquivos binários utilizados por alguns sistemas do jogo (como o de configuração). Já o diretório ```saves``` conterá os arquivos dos jogos salvos pelo jogador.

***

### Compilando o Código

Para compilar e executar o código, siga os passos descritos a seguir:

1. Instale o Python 3, cujo download, processo de instalação e demais informações podem ser vistas em https://www.python.org.
2. Instale um gerenciador de pacotes, como o pip, cujas informações podem ser vistas em https://pypi.org/project/pip/.
3. Instale os pacotes necessários através do arquivo de requerimentos: ```pip install -r requirements.txt```.
    - Alternativamente, certifique-se de que os pacotes `colorama`, `tabulate` e `Unidecode` já estejam instalados em sua máquina.
4. Execute o comando ```python main.py``` (ou ```python3 main.py```).

**Obs.:** Caso você não modifique o código do jogo, não renomeie as pastas ou os arquivos para que o código compile e o jogo execute corretamente.

