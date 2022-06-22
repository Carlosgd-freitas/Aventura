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
            print(f"      por Carlos Gabriel de Freitas - Alpha v0.0.3\n")        

            print('[1] Novo Jogo')
            print(Fore.RED + '[2] Carregar Jogo' + Style.RESET_ALL)
            print('[3] Notas de Atualização')
            print('[4] Créditos')
            print('')
            print('[0] Sair')
            retorno = 0

        op = utils.LerNumero('> ')

        if op == 0:
            print('\nDeseja sair do jogo?')
            print('[0] Não, retornar ao jogo.')
            print('[1] Sim, fechar o jogo.')

            sair = utils.LerNumeroIntervalo('> ', 0, 1)

            if sair == 0:
                retorno = 1
            else:
                os._exit(0)
        
        if op == 1:
            NovoSaveFile()
            retorno = 1

        ########
        elif op == 2:
            # ContinuarJogo()
            print('Esta funcionalidade ainda não está presente.')
        ########

        elif op == 3:
            notas.menuNotas(notas)
            retorno = 1
        
        elif op == 4:
            creditos()
            retorno = 1

def NovoSaveFile():
    """
    Criando um novo Save File.
    """
    # nome = input('Digite o nome do Save File: ')
    # f = open(nome + '.bin', 'wb')



    # f.close()

    ##################################################################

    # Criação do Personagem
    nome = input('\nDigite o seu nome: ')

    print('\nEscolha o seu gênero: ')
    print('[1] Masculino')
    print('[2] Feminino\n')
    genero = utils.LerNumeroIntervalo('> ', 1, 2)

    print('\nEscolha a sua classe: ')
    if genero == 1:
        genero = "M"
        print('[1] Guerreiro')
        print('[2] Mago\n')
    
    else:
        genero = "F"
        print('[1] Guerreira')
        print('[2] Maga\n')
    classe = utils.LerNumeroIntervalo('> ', 1, 2)

    j = None

    if classe == 1:
        j = guerreiro.CriarNovoGuerreiro(nome, genero)

    elif classe == 2:
        j = mago.CriarNovoMago(nome, genero)

    menu_equipamentos.EquipadosGanhos(j)
    area = area_1.Area_1(j, 15)
    retorno = menu_explorar.MenuExplorar(j, area)

    if retorno == -1:
        return

def creditos():
    """
    Imprime os créditos do jogo.
    """
    print('|---------------------|')
    print('|      CRÉDITOS       |')
    print('|---------------------|')
    print('|     PROGRAMAÇÃO     |')
    print('|     OmegaDagger     |')
    print('|---------------------|')
    print('|       TESTERS       |')
    print('|        Hidan        |')
    print('|      Macenario      |')
    print('|     marcusvsf.77    |')
    print('|        Reis         |')
    print('|       vfalva        |')
    print('|       Wolfhar       |')
    print('|     Zé Pretinho     |')
    print('|---------------------|')
    print('| Obrigado por jogar! |')
    print('|---------------------|')
    
    input('Aperte [ENTER] para sair.')
    print('')
