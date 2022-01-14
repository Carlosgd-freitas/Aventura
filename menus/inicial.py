import os
from colorama import Fore, Back, Style

import sys
sys.path.append("..")

from classes_base import jogador
from criaturas import slime
from combate import batalha

def MenuInicial():
    """
    Primeiro menu visto ao inicializar o jogo.
    """

    notas = NotasAtualizacao
    retorno = 1

    while True:
        if retorno == 1:
            
            print(f"    _                          _                         ")
            print(f"   / \  __   __  ___   _ __   | |_   _   _   _ __   __ _ ")
            print(f"  / _ \ \ \ / / / _ \ | '_ \  | __| | | | | | '__| / _` |")
            print(f" / ___ \ \ V / |  __/ | | | | | |_  | |_| | | |   | (_| |")
            print(f"/_/   \_\ \_/   \___| |_| |_|  \__|  \__,_| |_|    \__,_|\n")
            print(f"   por Carlos Gabriel de Freitas - Alpha v0.0.1\n")        

            print('[1] Novo Save File')
            print(Fore.RED + '[2] Carregar Save File' + Style.RESET_ALL)
            print('[3] Notas de Atualização\n')
            print('[0] Sair')
            retorno = 0

        op = int(input('> '))

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

    print('Escolha a sua classe: ')
    print('[1] Guerreiro')
    print('[2] Mago')

    while True:
        op = int(input('> '))

        if op == 1:
            op = "Guerreiro"
            break
    
        elif op == 2:
            op = "Mago"
            break

    j = jogador.Jogador(op, nome)

    # Aumentando os atributos do jogador com base em seus equipamentos
    for equip in j.equipados:
        j.ataque += equip[1].ataque
        j.defesa += equip[1].defesa
        j.magia += equip[1].magia
        j.velocidade += equip[1].velocidade

    slime_1 = slime.Slime(3)

    inimigos = [slime_1]

    resultado = batalha.BatalhaPrinicipal(j, inimigos)
    if resultado == 1:
        print('ganhei')
    elif resultado == -1:
        print('AFF')
    else:
        print('escapei')
    ##################################################################

class NotasAtualizacao():
    """
    Exibe o que foi adicionado, removido ou balanceado nas versões lançadas do jogo.
    """
    def exibir(self):
        """
        Exibe as notas de atualização.
        """

        self.titulo('\n----------------------------------- Alpha Versão 0.0.1 -----------------------------------')
        print('\nJogabilidade')
        self.positivo('Ações de Atacar, Defender, Usar Consumível, Usar Habilidade e Correr de uma Batalha adicionadas.\n')
        print('Jogador')
        self.positivo('Classes Guerreiro e Mago adicionadas.\n')
        print('Inimigos')
        self.positivo('Slime adicionado.\n')
        print('Habilidades')
        self.positivo('Projétil de Mana, Regeneração e Cuspe Ácido adicionados.\n')
        print('Itens')
        self.positivo('Espada Enferrujada, Cajado de Iniciante, Poção de Cura Pequena e Poção de Mana Pequena adicionados.\n')

        input('Aperte [ENTER] para sair.')
        return

    def titulo(string):
        """
        Utilizado para imprimir o título de uma versão. Impime a string em preto com fundo branco.
        """
        print(Fore.BLACK + Back.WHITE + string + Style.RESET_ALL)

    def positivo(string):
        """
        Imprime um '+' verde e uma string em branco, ambos com fundo preto.
        """
        print(Back.BLACK + Fore.GREEN + '+ ' + Fore.WHITE + string + Style.RESET_ALL)
    
    def negativo(string):
        """
        Imprime um '-' vermelho e uma string em branco, ambos com fundo preto.
        """
        print(Back.BLACK + Fore.RED + '- ' + Fore.WHITE + string + Style.RESET_ALL)
    
    def neutro(string):
        """
        Imprime um '*' amarelo e uma string em branco, ambos com fundo preto.
        """
        print(Back.BLACK + Fore.YELLOW + '- ' + Fore.WHITE + string + Style.RESET_ALL)
        