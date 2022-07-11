import sys
import pickle
from colorama import Fore, Back, Style

sys.path.append("..")
from classes_base import utils, configuracao

def MenuConfiguracoes(conf, caminhos):
    """
    Menu de gerenciamento das configurações preferenciais do jogador.

    Parâmetros:
    - conf: configurações do usuário relativas ao jogo;
    - caminhos: dicionário contendo o caminho de diversas pastas e arquivos.
    """

    retorno = 1
    op = -1

    # Visualizando e alterando configurações
    while op != 0:
        if retorno == 1:
            retorno = 0

            print('Digite o índice correspondente a uma configuração para alterá-la:\n')

            # Opção de ligar/desligar a confirmação ao fechar o jogo
            print('[1] Confirmação ao fechar o jogo: ', end = '')
            if conf.confirmacao_sair == True:
                print(Fore.GREEN + 'LIGADO' + Style.RESET_ALL)
            else:
                print(Fore.RED + 'DESLIGADO' + Style.RESET_ALL)
            
            # Velocidade da fala de narração e NPCs
            print(f'[2] Velocidade da fala de narração e NPCs: {conf.npc_fala_delay}')

            print('\n[0] Salvar configurações e voltar para o menu principal\n')

        # Jogador escolhendo uma opção
        op = utils.LerNumeroIntervalo('> ', 0, 2)

        if op == 1:
            conf.confirmacao_sair = not conf.confirmacao_sair
            print('Configuração [1] alterada!')
            retorno = 1
        
        elif op == 2:
            print('\nDigite um número real entre 0 e 0.5. Quanto mais baixo o número, mais rápida será as falas dos NPCs.')
            conf.npc_fala_delay = utils.LerNumeroIntervalo('> Nova Velocidade: ', 0, 0.5, 'float')

            utils.ImprimirComDelay('Este é um exemplo de como as falas de narração e NPCs serão impressas.\n', conf.npc_fala_delay)
            print('Configuração [2] alterada!')
            retorno = 1

        print('')

    # Salvando configurações
    caminho_conf = caminhos['conf']
    configuracao.SalvarConfiguracao(conf, caminho_conf)
