#!/usr/bin/env python

import random
import os
import pickle
from colorama import init

from classes_base import configuracao
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

# Caminhos de arquivos e pastas
caminhos = {}

caminho_main = os.path.dirname(os.path.abspath(__file__))
caminhos['main'] = caminho_main

caminho_bin = os.path.join(caminho_main, 'bin')
caminhos['bin'] = caminho_bin

caminho_conf = os.path.join(caminho_bin, 'conf')
caminhos['conf'] = caminho_conf

# Configurações do Usuário
conf = None

# Se ainda não foi criado um arquivo contendo as configurações
if(os.path.exists(caminho_conf) == False):

    # Se o diretório "bin" ainda não foi criado
    if(os.path.exists(caminho_bin) == False):
        os.mkdir(caminho_bin)

    conf = configuracao.Configuracao()
    configuracao.SalvarConfiguracao(conf, caminho_conf)

# Carregando as configurações do usuário
else:
    dados = pickle.loads(open(caminho_conf, "rb").read())

    # Campo de validação do arquivo binário
    if 'valido' in dados:
        valido = dados['valido']

        if valido == 'Arquivo de configuração do Aventura':
            conf = dados['conf']
        
        else:
            input('ERRO: As configurações não puderam ser carregadas corretamente.')
            os._exit(0)
    
    else:
        input('ERRO: As configurações não puderam ser carregadas corretamente.')
        os._exit(0)

# Menu inicial do jogo
MenuInicial(conf, caminhos)
