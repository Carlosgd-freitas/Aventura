import os
import sys
from colorama import Fore, Back, Style

from . import notas_atualizacao, menu_explorar, menu_equipamentos, menu_configuracoes

sys.path.append("..")

from classes_base import guerreiro, mago, utils, configuracao
from areas import area_1

def MenuInicial():
    """
    Primeiro menu visto ao inicializar o jogo.
    """

    notas = notas_atualizacao.NotasAtualizacao
    conf = configuracao.Configuracao()

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
            print('[5] Configurações')
            print('')
            print('[0] Sair')
            retorno = 0

        op = utils.LerNumero('> ')

        if op == 0:
            if conf.confirmacao_sair:
                print('\nDeseja sair do jogo?')
                print('[0] Não, retornar ao jogo.')
                print('[1] Sim, fechar o jogo.')

                sair = utils.LerNumeroIntervalo('> ', 0, 1)

                if sair == 0:
                    retorno = 1
                else:
                    os._exit(0)
            
            else:
                os._exit(0)
        
        if op == 1:
            NovoSaveFile(conf)
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
        
        elif op == 5:
            print('')
            menu_configuracoes.MenuConfiguracoes(conf)
            retorno = 1

def NovoSaveFile(conf):
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
    area = area_1.Area_1(15)

    utils.ImprimirComDelay('\nOlha. Na falta de um começo pra um enredo revolucionário, nunca antes visto em um RPG ' +
        'com tema medieval, vamos com um genérico mesmo. Ou vários. Você pode ter o\nsonho de se tornar o maior ' +
        'aventureiro do mundo ou está com uma sede de sangue e busca matar monstros para se saciar. Talvez você ' +
        'planeje juntar todo o ouro que\nconseguir e investir em uma franquia de estalagens e bares, ou ainda você ' +
        'queira explorar cada floresta e caverna que este mundo tem a oferecer. Talvez ainda,\nvocê acabe sua jornada ' +
        'enfrentando seres de poder que você sequer consegue imaginar. Escolha o começo de história que mais te '+
        'agrada.\n', conf.npc_fala_delay)
    utils.ImprimirComDelay('Mas o que está consolidado mesmo.\n',conf.npc_fala_delay)
    utils.ImprimirComDelay('É que você partiu em uma Aventura.\n',conf.npc_fala_delay)

    retorno = menu_explorar.MenuExplorar(j, area, conf)

    if retorno == -1:
        return

def creditos():
    """
    Imprime os créditos do jogo.
    """
    utils.ImprimirComDelay('|---------------------|\n', 0.01)
    utils.ImprimirComDelay('|      ', 0.01)
    utils.ImprimirComDelay('CRÉDITOS', 0.03)
    utils.ImprimirComDelay('       |\n', 0.01)
    utils.ImprimirComDelay('|---------------------|\n', 0.01)

    utils.ImprimirComDelay('|     ', 0.01)
    utils.ImprimirComDelay('PROGRAMAÇÃO', 0.03)
    utils.ImprimirComDelay('     |\n', 0.01)

    utils.ImprimirComDelay('|        ', 0.01)
    utils.ImprimirComDelay('Omega', 0.1)
    utils.ImprimirComDelay('        |\n', 0.01)

    utils.ImprimirComDelay('|---------------------|\n', 0.01)

    utils.ImprimirComDelay('|       ', 0.01)
    utils.ImprimirComDelay('TESTERS', 0.03)
    utils.ImprimirComDelay('       |\n', 0.01)

    utils.ImprimirComDelay('|        ', 0.01)
    utils.ImprimirComDelay('Hidan', 0.03)
    utils.ImprimirComDelay('        |\n', 0.01)

    utils.ImprimirComDelay('|      ', 0.01)
    utils.ImprimirComDelay('Macenario', 0.03)
    utils.ImprimirComDelay('      |\n', 0.01)

    utils.ImprimirComDelay('|     ', 0.01)
    utils.ImprimirComDelay('marcusvsf.77', 0.03)
    utils.ImprimirComDelay('    |\n', 0.01)

    utils.ImprimirComDelay('|       ', 0.01)
    utils.ImprimirComDelay('vfalva', 0.03)
    utils.ImprimirComDelay('        |\n', 0.01)

    utils.ImprimirComDelay('|       ', 0.01)
    utils.ImprimirComDelay('Wolfhar', 0.03)
    utils.ImprimirComDelay('       |\n', 0.01)

    utils.ImprimirComDelay('|     ', 0.01)
    utils.ImprimirComDelay('Zé Pretinho', 0.03)
    utils.ImprimirComDelay('     |\n', 0.01)

    utils.ImprimirComDelay('|---------------------|\n', 0.01)
    utils.ImprimirComDelay('| ', 0.01)
    utils.ImprimirComDelay('Obrigado por jogar!', 0.03)
    utils.ImprimirComDelay(' |\n', 0.01)
    utils.ImprimirComDelay('|---------------------|\n', 0.01)
    
    input('Aperte [ENTER] para sair.')
    print('')
