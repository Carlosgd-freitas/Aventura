import random
from colorama import init

from classes_base.criatura import *
from classes_base.item import *
from menus.inicial import *

# Lembrete: Quando uma nova arma for criada e ela for de um tipo que não é "Normal", ela deve alterar o tipo
# do ataque normal do jogador em EquipadosGanhos()

# Lembrete: Quando um item equipável aumenta maxHp/maxMana, ele também deve aumentar hp/mana

# .py -> .exe : pyinstaller --onefile main.py

# Style.DIM ; Style.NORMAL ; Style.BRIGHT ; Style.RESET_ALL
# BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE
# Fore. ; Back.

# Inicialização do colorama
random.seed()
init()

MenuInicial()
