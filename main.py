import random
import os
import sys
import pickle
from colorama import init

from base import configuracao, imprimir
from menus import menu_inicial

def DefinirCaminhos():
    """
    Retorna um dicionário contendo os caminhos de diferentes arquivos e diretórios utilizados pelo
    jogo.
    """
    caminhos = {}

    if getattr(sys, 'frozen', False):
        caminho_main = os.path.dirname(sys.executable)
    elif __file__:
        caminho_main = os.path.dirname(os.path.abspath(__file__))
    caminhos['main'] = caminho_main

    caminho_bin = os.path.join(caminho_main, 'bin')
    caminhos['bin'] = caminho_bin

    caminho_conf = os.path.join(caminho_bin, 'conf')
    caminhos['conf'] = caminho_conf

    caminho_saves = os.path.join(caminho_main, 'saves')
    caminhos['saves'] = caminho_saves

    return caminhos

def DefinirConfiguracoes(caminhos):
    """
    Retorna as configurações preferenciais do usuário.

    Parâmetros:
    - caminhos: um dicionário contendo os caminhos de diferentes arquivos e diretórios utilizados pelo
    jogo.
    """
    caminho_conf = caminhos['conf']
    caminho_bin = caminhos['bin']

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
                imprimir.MensagemErro('As configurações não puderam ser carregadas corretamente.')
                os._exit(0)
        
        else:
            imprimir.MensagemErro('As configurações não puderam ser carregadas corretamente.')
            os._exit(0)
    
    return conf

if __name__ == "__main__":
    # Inicialização
    random.seed() # Inicialização de uma semente aleatória
    init()        # Inicialização da biblioteca colorama

    # Caminhos de arquivos e pastas
    caminhos = DefinirCaminhos()

    # Configurações do Usuário
    conf = DefinirConfiguracoes(caminhos)
    conf.Atualizar() # Atualizando o arquivo de configurações

    # Se o diretório "saves" ainda não foi criado
    caminho_saves = caminhos['saves']
    if(os.path.exists(caminho_saves) == False):
        os.mkdir(caminho_saves)

    # Menu inicial do jogo
    menu_inicial.MenuInicial(conf, caminhos)
