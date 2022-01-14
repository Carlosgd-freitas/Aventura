from classes_base.criatura import *
from classes_base.item import *
from menus.inicial import *

from colorama import init

# .py -> .exe : pyinstaller --onefile main.py

# Style.DIM ; Style.NORMAL ; Style.BRIGHT ; Style.RESET_ALL
# BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE
# Fore. ; Back.

# Inicialização do colorama
init()

MenuInicial()
