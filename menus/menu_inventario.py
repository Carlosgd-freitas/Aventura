import math
import sys
from tabulate import tabulate
from colorama import Fore, Back, Style

sys.path.append("..")
from base import imprimir, utils
from combate import jogador_acoes

def ImprimirInventario(jogador, item_indice, impressoes_por_pagina):
    """
    Imprime até <impressoes_por_pagina> primeiros itens presentes no inventário do jogador, incluindo e a
    partir do índice do item passado como parâmetro.
    """

    # Imprimindo os itens presentes no inventário do jogador
    print('|========================================> INVENTÁRIO <=========================================|')

    tabela = []
    cabecalho = ["Nome", "Quantidade", Fore.YELLOW + 'Preço' + Style.RESET_ALL, "Classificação"]
    alinhamento = ("left", "center", "center", "center")
        
    i = 0
    while i < impressoes_por_pagina:

        # Há menos que <impressoes_por_pagina> itens restantes
        if item_indice == len(jogador.inventario):
            break

        item = jogador.inventario[item_indice]
        
        t = []
        t.append(f'[{item_indice+1}] ' + item.nome) # Índice + Nome
        t.append(item.quantidade)                   # Quantidade
        t.append(item.preco)                        # Preço
        t.append(item.classificacao)                # Classificação
        tabela.append(t)

        item_indice += 1
        i += 1
    
    print(tabulate(tabela, headers = cabecalho, colalign = alinhamento, tablefmt="psql"))
    print('')

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

        # Imprimindo até 'itens_por_pagina' itens
        anterior = 0
        proximo = 0
        item_indice_atual = (pagina * itens_por_pagina)
        ImprimirInventario(jogador, item_indice_atual, itens_por_pagina)

        print('[1] Analisar item')
        print('[2] Usar item')
        print('[3] Jogar item fora')

        # É possível imprimir até 'itens_por_pagina' itens anteriores
        if pagina > 0:
            anterior = 1
            print('[4] Anterior')
        else:
            print(Fore.RED + '[4] Anterior' + Style.RESET_ALL)

        # É possível imprimir até 'itens_por_pagina' próximos itens
        if pagina < ultima_pagina:
            proximo = 1
            print('[5] Próximo')
        else:
            print(Fore.RED + '[5] Próximo' + Style.RESET_ALL)

        print('\n[0] Retornar ao menu anterior')

        while True:
            op = utils.LerNumeroIntervalo('> ', 0, 5)

            if (op == 4 and anterior == 0) or (op == 5 and proximo == 0):
                continue
            else:
                break
        
        # Retornando ao menu anterior
        if op == 0:
            break
    
        # Imprimir até 'itens_por_pagina' itens anteriores
        elif op == 4 and anterior == 1:
            pagina -= 1
        
        # Imprimir até 'itens_por_pagina' próximos itens
        elif op == 5 and proximo == 1:
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
                        print('\nQual item deseja analisar?')
                    elif op == 2:
                        print('\nQual item deseja usar?')
                    elif op == 3:
                        print('\nQual item deseja jogar fora?')
                    pergunta = 0

                escolha = utils.LerNumero('> ')
            
                # Saindo
                if escolha == 0:
                    break

                # Procedendo
                elif escolha >= menor_indice and escolha <= maior_indice:

                    item_escolhido = jogador.inventario[escolha - 1]

                    # Analisar item
                    if op == 1:
                        imprimir.ImprimirItemDetalhado(item_escolhido)
                        break

                    # Usar item
                    elif op == 2:
                        if item_escolhido.fora_batalha == True:
                            valido = jogador_acoes.ValidaUsoConsumivel(jogador, item_escolhido)

                            if valido:
                                jogador_acoes.UsarConsumivel(jogador, escolha-1, fora_combate = True)

                        else:
                            print('Este item não pode ser utilizado.')
                        
                        print('')
                        break

                    # Jogar item fora
                    elif op == 3:
                        print('\nQuantos deste item deseja jogar fora?')
                    
                        while True:
                            escolha_quantidade = utils.LerNumero('> ')

                            if escolha_quantidade == 0:
                                break

                            elif escolha_quantidade > 0 and escolha_quantidade <= item_escolhido.quantidade:
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
