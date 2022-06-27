import os
import sys
import random

from . import menu_equipamentos, menu_habilidades, menu_inventario

sys.path.append("..")

from classes_base import utils
from combate import batalha

def MenuExplorar(jogador, area, conf):
    """
    Emula a exploração de uma área pelo jogador. Retorna -1 quando o jogador perde o jogo.
    """

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

            if area.nome == "Planície de Slimes":
                if area.conhece_vila == False:
                    print('[6] Encontrar a vila mais próxima')
                elif area.conhece_vila == True:
                    print('[6] Ir até a Vila Pwikutt')
            
                print('[7] Ir em direção à Floresta')

            print('\n[0] Sair\n')
            
            retorno = 0

        op = utils.LerNumero('> ')

        # Sair do Jogo
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
        
        # Explorar a Área
        elif op == 1:

            explorar_flag = 0
            
            # Evento: Descanso
            chance = random.randint(1, 100)
            if explorar_flag == 0 and chance <= chance_descanso and \
                (jogador.hp < jogador.maxHp or jogador.mana < jogador.maxMana):

                resultado = area.EventoDescanso(jogador)
                chance_descanso = 0
                explorar_flag = 1

            elif explorar_flag == 0:
                chance_descanso += 15
            
            # Batalha
            if explorar_flag == 0:
                print('Uma batalha se iniciou!')

                inimigos = area.RetornarEncontro(jogador)
                aliados = [jogador]
                resultado = batalha.BatalhaPrinicipal(aliados, inimigos)

            # Resultado de uma Batalha
            if resultado == 1:

                # Tentativa de subir de nível
                subiu = jogador.SubirNivel()
                
                print('Você retoma seu fôlego e segue em sua Aventura.')

            elif resultado == -1:
                print('\nO último ataque foi grave demais. Sua consciência vai se esvaindo e você colapsa no chão.')
                print("     _____                                ____                         ")
                print("    / ____|                              / __ \                        ")
                print("   | |  __    __ _   _ __ ___     ___   | |  | | __   __  ___   _ __   ")
                print("   | | |_ |  / _` | | '_ ` _ \   / _ \  | |  | | \ \ / / / _ \ | '__|  ")
                print("   | |__| | | (_| | | | | | | | |  __/  | |__| |  \ V / |  __/ | |     ")
                print("    \_____|  \__,_| |_| |_| |_|  \___|   \____/    \_/   \___| |_|     ")                                                            
                input('\nPressione [ENTER] para retornar ao menu principal.')
                return -1

            retorno = 1

        # Status do Jogador
        elif op == 2:
            jogador.ImprimirStatus()
            retorno = 1
        
        # Inventário do Jogador
        elif op == 3:
            print('')

            if not jogador.inventario:
                print('Você não tem itens em seu inventário.')
            else:
                menu_inventario.MenuInventario(jogador)

            retorno = 1
        
        # Habilidades do Jogador
        elif op == 4:
            print('')

            if len(jogador.habilidades) == 1: # Jogador só possui a habilidade "Atacar"
                print('Você não tem habilidades.')
            else:
                menu_habilidades.MenuHabilidades(jogador)

            retorno = 1

        # Equipamentos do Jogador
        elif op == 5:
            print('')
            menu_equipamentos.MenuEquipamentos(jogador)
            retorno = 1
        
        # Ir até a Vila/Cidade
        elif op == 6:
            print('')
            area.MenuVila(jogador, conf)
            retorno = 1

        # Ir em direção à Floresta
        elif op == 7:
            print('')
            resultado = area.EncontroChefe(jogador, conf)

            if area.chefao_derrotado == True:
                utils.ImprimirComDelay('Você chegou ao final desta versão do jogo, parabéns! Você agora será '+
                'retornado ao menu de exploração, com sua vida e mana maximizadas,\ne pode continuar jogando. O ' +
                'chefão também estará vivo novamente, se quiser enfrentá-lo. Obrigado por jogar!\n', conf.npc_fala_delay)
            
                jogador.hp = jogador.maxHp
                jogador.mana = jogador.maxMana

                retorno = 1
            
            elif resultado == -1:
                return -1
