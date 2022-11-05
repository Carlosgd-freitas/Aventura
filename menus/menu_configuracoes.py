import sys
import pickle
from colorama import Fore, Back, Style

sys.path.append("..")
from base import imprimir, configuracao, utils

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

            # Ligar/desligar a confirmação ao fechar o jogo
            print('[1] Confirmação ao fechar o jogo: ', end = '')
            configuracao.ImprimirConfiguracaoLigadoDesligado(conf.confirmacao_sair)

            # Ligar/desligar o salvamento automático ao fechar o jogo
            print('[2] Salvar automaticamente ao fechar o jogo: ', end = '')
            configuracao.ImprimirConfiguracaoLigadoDesligado(conf.salvar_sair)

            # Velocidade da fala de narração e NPCs
            print('[3] Velocidade da fala de narração e NPCs: ', end = '')
            configuracao.ImprimirConfiguracaoValor(conf.npc_fala_delay)

            # Tecla da ação de Status
            print('[4] Tecla da ação de Status no menu de exploração: ', end = '')
            configuracao.ImprimirConfiguracaoValor(conf.tecla_status)

            # Tecla da ação de Inventário
            print('[5] Tecla da ação de Inventário no menu de exploração: ', end = '')
            configuracao.ImprimirConfiguracaoValor(conf.tecla_inventario)

            # Tecla da ação de Habilidades
            print('[6] Tecla da ação de Habilidades no menu de exploração: ', end = '')
            configuracao.ImprimirConfiguracaoValor(conf.tecla_habilidades)

            # Tecla da ação de Equipamentos
            print('[7] Tecla da ação de Equipamentos no menu de exploração: ', end = '')
            configuracao.ImprimirConfiguracaoValor(conf.tecla_equipamentos)

            # Tecla da ação de Salvar o Jogo
            print('[8] Tecla da ação de Salvar o Jogo no menu de exploração: ', end = '')
            configuracao.ImprimirConfiguracaoValor(conf.tecla_salvar_jogo)

            print('\n[0] Salvar configurações e voltar para o menu principal\n')

        # Jogador escolhendo uma opção
        op = utils.LerNumeroIntervalo('> ', 0, 8)

        if op == 1:
            conf.confirmacao_sair = not conf.confirmacao_sair
        
        elif op == 2:
            conf.salvar_sair = not conf.salvar_sair
        
        elif op == 3:
            print('\nDigite um número real entre 0 e 0.5. Quanto mais baixo o número, mais rápida será as falas dos NPCs.')
            conf.npc_fala_delay = utils.LerNumeroIntervalo('> Nova Velocidade: ', 0, 0.5, 'float')
            imprimir.ImprimirComDelay('Este é um exemplo de como as falas de narração e NPCs serão impressas.\n', conf.npc_fala_delay)

        elif op == 4:
            configuracao.DefinirConfiguracaoValor(conf, conf.tecla_status)
        
        elif op == 5:
            configuracao.DefinirConfiguracaoValor(conf, conf.tecla_inventario)
        
        elif op == 6:
            configuracao.DefinirConfiguracaoValor(conf, conf.tecla_habilidades)
        
        elif op == 7:
            configuracao.DefinirConfiguracaoValor(conf, conf.tecla_equipamentos)
        
        elif op == 8:
            configuracao.DefinirConfiguracaoValor(conf, conf.tecla_salvar_jogo)

        if op >= 1 and op <= 8:
            imprimir.MensagemSistema(f'Configuração [{op}] foi alterada.', modo = 'print')
            retorno = 1

        print('')

    # Salvando configurações
    caminho_conf = caminhos['conf']
    configuracao.SalvarConfiguracao(conf, caminho_conf)
