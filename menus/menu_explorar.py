import os
import sys
import random
from colorama import Fore, Back, Style

from . import menu_equipamentos, menu_habilidades, menu_inventario

sys.path.append("..")

from classes_base import utils
from combate import batalha

def MenuExplorar(jogador, area):
    """
    Emula a exploração de uma área pelo jogador.
    """

    chance_loja = 0
    chance_descanso = 0
    explorar_flag = 0
    retorno = 1

    while True:

        if retorno == 1:
            print('\nEscolha sua Ação:')
            print('[1] Explorar')
            print('[2] Status')
            print('[3] Inventário')
            print('[4] Habilidades')
            print('[5] Equipamentos')
            print('\n[0] Sair\n')
            
            retorno = 0

        op = utils.LerNumero('> ')

        # Sair do Jogo
        if op == 0:
            os._exit(0)
        
        # Explorar a Área
        elif op == 1:

            explorar_flag = 0

            # Loja encontrada
            chance = random.randint(1, 100)
            if chance <= chance_loja and jogador.ouro > area.PrecoItemMaisBarato():
                area.Loja(jogador)
                chance_loja = 0
                explorar_flag = 1
            elif explorar_flag == 0:
                chance_loja += 10
            
            # Evento: Descanso
            chance = random.randint(1, 100)
            if explorar_flag == 0 and chance <= chance_descanso and \
            (jogador.hp < jogador.maxHp or jogador.mana < jogador.maxMana):
                area.EventoDescanso(jogador)
                chance_descanso = 0
                explorar_flag = 1
            elif explorar_flag == 0:
                chance_descanso += 10
            
            # Batalha
            if explorar_flag == 0:
                print('Uma batalha se iniciou!\n')

                encontro_numero = random.choice(area.encontros)
                inimigos = area.RetornarEncontro(jogador, encontro_numero)
                resultado = batalha.BatalhaPrinicipal(jogador, inimigos)

                # Resultado da Batalha
                if resultado == 1:

                    # Tentativa de subir de nível
                    subiu = 0
                    while True:
                        subiu = jogador.SubirNivel()

                        if subiu == 1:
                            area.DefinirEncontros(jogador) # Atualizando os encontros de inimigos possíveis
                        else:
                            break
                    
                    print('Você retoma seu fôlego e segue em sua Aventura.')

                elif resultado == -1:
                    print('\nO último ataque foi grave demais. Sua consciência vai se esvaindo e você colapsa no chão.')
                    print("     _____                                ____                         ")
                    print("    / ____|                              / __ \                        ")
                    print("   | |  __    __ _   _ __ ___     ___   | |  | | __   __  ___   _ __   ")
                    print("   | | |_ |  / _` | | '_ ` _ \   / _ \  | |  | | \ \ / / / _ \ | '__|  ")
                    print("   | |__| | | (_| | | | | | | | |  __/  | |__| |  \ V / |  __/ | |     ")
                    print("    \_____|  \__,_| |_| |_| |_|  \___|   \____/    \_/   \___| |_|     ")                                                            
                    input('\nPressione [ENTER] para fechar o jogo.')
                    os._exit(0)

            retorno = 1

        # Status do Jogador
        elif op == 2:
            jogador.ImprimirStatus()
            retorno = 1
        
        # Inventário do Jogador
        elif op == 3:
            print('')
            menu_inventario.MenuInventario(jogador)
            retorno = 1
        
        # Habilidades do Jogador
        elif op == 4:
            print('')
            menu_habilidades.MenuHabilidades(jogador)
            retorno = 1

        # Equipamentos do Jogador
        elif op == 5:
            print('')
            menu_equipamentos.MenuEquipamentos(jogador)
            retorno = 1