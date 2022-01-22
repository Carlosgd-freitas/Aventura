import os
import sys
from colorama import Fore, Back, Style

from . import notas_atualizacao, menu_explorar, menu_equipamentos

sys.path.append("..")

from classes_base import guerreiro, mago, utils
from areas import area_1

def MenuInicial():
    """
    Primeiro menu visto ao inicializar o jogo.
    """

    notas = notas_atualizacao.NotasAtualizacao
    retorno = 1

    while True:
        if retorno == 1:
            
            print(f"    _                          _                         ")
            print(f"   / \  __   __  ___   _ __   | |_   _   _   _ __   __ _ ")
            print(f"  / _ \ \ \ / / / _ \ | '_ \  | __| | | | | | '__| / _` |")
            print(f" / ___ \ \ V / |  __/ | | | | | |_  | |_| | | |   | (_| |")
            print(f"/_/   \_\ \_/   \___| |_| |_|  \__|  \__,_| |_|    \__,_|\n")
            print(f"      por Carlos Gabriel de Freitas - Alpha v0.0.2\n")        

            print('[1] Novo Jogo')
            print(Fore.RED + '[2] Carregar Jogo' + Style.RESET_ALL)
            print('[3] Notas de Atualização\n')
            print('[0] Sair')
            retorno = 0

        op = utils.LerNumero('> ')

        if op == 0:
            os._exit(0)
        
        ########
        elif op == 2:
            print('Esta funcionalidade ainda não está presente.')
        ########

        elif op == 3:
            notas.exibir(notas)
            retorno = 1

        ######## if op >= 1 or op == 2:
        if op == 1:
            break
    
    if op == 1:
        NovoSaveFile()
    # elif op == 2:
    #     ContinuarJogo()

def NovoSaveFile():
    """
    Criando um novo Save File.
    """
    # nome = input('Digite o nome do Save File: ')
    # f = open(nome + '.bin', 'wb')



    # f.close()

    ##################################################################

    nome = input('\nDigite o seu nome: ')

    print('\nEscolha a sua classe: ')
    print('[1] Guerreiro')
    print('[2] Mago\n')

    j = None
    while True:
        op = utils.LerNumero('> ')

        if op == 1:
            j = guerreiro.CriarNovoGuerreiro(nome)
            break
    
        elif op == 2:
            j = mago.CriarNovoMago(nome)
            break

    menu_equipamentos.EquipadosGanhos(j)
    area = area_1.Area_1(j, 15)
    menu_explorar.MenuExplorar(j, area)
