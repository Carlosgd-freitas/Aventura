import math
import sys

from . import menu_paginado_generico

sys.path.append("..")
from base import imprimir, utils
from combate import usar_consumivel

def MenuInventario(jogador):
    """
    Menu de gerenciamento do inventário do jogador.
    """

    itens_por_pagina = 15
    ultima_pagina = len(jogador.inventario)
    ultima_pagina = math.ceil(ultima_pagina / itens_por_pagina)
    ultima_pagina -= 1
    item_indice_atual = 0
    pagina = 0

    while True:
        if pagina > 0:
            anterior = True
        else:
            anterior = False
        if pagina < ultima_pagina:
            proximo = True
        else:
            proximo = False
        item_indice_atual = (pagina * itens_por_pagina)

        # Imprimindo uma página de itens presentes no inventário do jogador
        print('|========================================> INVENTÁRIO <=========================================|')
        itens = menu_paginado_generico.ComporPagina(jogador.inventario, item_indice_atual, itens_por_pagina)
        tabela = imprimir.RetornarTabelaItens(itens, jogador, item_indice_atual + 1)
        print(tabela)
        print('')

        # Opções disponíveis no menu de inventário
        opcoes = ['Analisar Item', 'Usar Item', 'Jogar Item Fora']
        if anterior or proximo:
            opcoes.append('Anterior')
            opcoes.append('Próximo')
        opcoes.append('Retornar ao Menu Anterior')  
        op = menu_paginado_generico.ImprimirOpções(opcoes, pagina, ultima_pagina)
        if op != 0:
            print('')

        # Retornando ao menu anterior
        if op == 0:
            break
    
        # Imprimir até 'itens_por_pagina' itens anteriores
        elif op == 4 and anterior:
            pagina -= 1
        
        # Imprimir até 'itens_por_pagina' próximos itens
        elif op == 5 and proximo:
            pagina += 1

        # Analisar, usar ou jogar o item fora
        else:
            escolha = 1
            pergunta = 1

            menor_indice = (pagina * itens_por_pagina) + 1
            maior_indice = (pagina + 1) * itens_por_pagina
            if len(jogador.inventario) < maior_indice:
                maior_indice = len(jogador.inventario)

            while escolha != 0:

                if pergunta == 1:
                    if op == 1:
                        print('Qual item deseja analisar?')
                    elif op == 2:
                        print('Qual item deseja usar?')
                    elif op == 3:
                        print('Qual item deseja jogar fora?')
                    pergunta = 0

                escolha = utils.LerNumeroIntervalo('> ', menor_indice, maior_indice, permitido = [0])
                print('')

                # Saindo
                if escolha == 0:
                    break

                # Procedendo
                else:
                    item_escolhido = jogador.inventario[escolha - 1]

                    # Analisar item
                    if op == 1:
                        imprimir.ImprimirItemDetalhado(item_escolhido, jogador)
                        break

                    # Usar item
                    elif op == 2:
                        if item_escolhido.fora_batalha == True:
                            valido = usar_consumivel.ValidaUsoConsumivel(jogador, item_escolhido)

                            if valido:
                                usar_consumivel.UsarConsumivel(jogador, escolha-1, fora_combate = True)
                        else:
                            print('Este item não pode ser utilizado.\n')
                        break

                    # Jogar item fora
                    elif op == 3:
                        print('Quantos deste item deseja jogar fora?')
                    
                        while True:
                            escolha_quantidade = utils.LerNumeroIntervalo('> ', 0, item_escolhido.quantidade)
                            print('')

                            if escolha_quantidade == 0:
                                break
                            elif escolha_quantidade > 0:
                                item_escolhido.quantidade -= escolha_quantidade

                                if item_escolhido.quantidade <= 0:
                                    jogador.inventario.remove(item_escolhido)
                                break

                        # Operação foi cancelada
                        if escolha_quantidade == 0:
                            pergunta = 1
                        else:
                            break
        
            # Checando se a página tinha 1 item sobrando, e ele foi removido
            tentativa_ultima_pagina = len(jogador.inventario)
            tentativa_ultima_pagina = math.ceil(tentativa_ultima_pagina / itens_por_pagina)
            tentativa_ultima_pagina -= 1

            if escolha != 0 and ultima_pagina != tentativa_ultima_pagina:
                ultima_pagina -= 1
                if pagina > 0:
                    pagina -= 1

            # Se o jogador jogou todos os itens fora
            if len(jogador.inventario) == 0:
                print('Você não tem itens em seu inventário.')
                return
