#!/usr/bin/env python

import random
from colorama import init

from menus.inicial import *

# Lembrete: Quando uma nova arma for criada e ela for de um tipo que não é "Normal", ela deve alterar o tipo
# do ataque normal do jogador em EquipadosGanhos()

# .py -> .exe : pyinstaller --onefile main.py

# Style.DIM ; Style.NORMAL ; Style.BRIGHT ; Style.RESET_ALL
# BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE
# Fore. ; Back.

# Inicialização
random.seed() # Inicialização de uma semente aleatória
init()        # Inicialização da biblioteca colorama

MenuInicial()
