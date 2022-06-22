import math
import sys
from colorama import Fore, Back, Style

sys.path.append("..")
from classes_base import utils
from combate import jogador_acoes

def ImprimirInventario(jogador, item_indice, impressoes_por_pagina):
    """
    Imprime até <impressoes_por_pagina> primeiros itens presentes no inventário do jogador, incluindo e a
    partir do índice da habilidade passada como parâmetro.
    """

    # Imprimindo os itens presentes no inventário do jogador
    print('|========================================> INVENTÁRIO <=========================================|')

    i = 0
    while i < impressoes_por_pagina:

        flag_consumivel = 0

        # Há menos que <impressoes_por_pagina> itens restantes
        if item_indice == len(jogador.inventario):
            break

        item = jogador.inventario[item_indice]

        # Nome do item
        mensagem = f'[{item_indice+1}] {item[1].nome} - '
        
        # Classificação do item
        if item[0] == "Consumivel":
            mensagem += 'Consumível - '
            flag_consumivel = 1
        elif item[0] == "Duas maos":
            mensagem += 'Duas mãos - '
        elif item[0] == "Uma mao":
            mensagem += 'Uma mão - '
        elif item[0] == "Peitoral":
            mensagem += 'Peitoral - '
        elif item[0] == "Pes":
            mensagem += 'Pés - '
        elif item[0] == "Acessorio":
            mensagem += 'Acessório - '

        # Quantidade e preço do item
        mensagem += f'Quantidade: {item[1].quantidade} - '
        mensagem += Fore.YELLOW + 'Preço' + Style.RESET_ALL + f': {item[1].preco}'

        # Nível e tipo do item, caso ele não for um consumível
        if flag_consumivel == 0:
            mensagem += f' - Nível: {item[1].nivel} - Tipo: '
            print(mensagem, end = '')
            utils.ImprimirTipo(item[1].tipo)
            print('')

        else:
            print(mensagem)

        # Descrição do Item
        print(f'Descrição: {item[1].descricao}\n')

        item_indice += 1
        i += 1

def MenuInventario(jogador):
    """
    Menu de gerenciamento do inventário do jogador.
    """

    ultima_pagina = len(jogador.inventario)
    ultima_pagina = math.ceil(ultima_pagina / 10)
    ultima_pagina -= 1
    item_indice_atual = 0
    pagina = 0

    while True:

        # Imprimindo até 10 itens
        anterior = 0
        proximo = 0
        item_indice_atual = (pagina * 10)
        ImprimirInventario(jogador, item_indice_atual, 10)

        # É possível imprimir até 10 itens anteriores
        if pagina > 0:
            anterior = 1
            print('[1] Anterior')
        
        else:
            print(Fore.RED + '[1] Anterior' + Style.RESET_ALL + '')

        # É possível imprimir até 10 próximos itens
        if pagina < ultima_pagina:
            proximo = 1
            print('[2] Próximo')
        
        else:
            print(Fore.RED + '[2] Próximo' + Style.RESET_ALL)

        print('[3] Usar item')
        print('[4] Jogar item fora\n')
        print('[0] Retornar ao menu anterior')

        while True:
            op = utils.LerNumero('> ')

            if (op == 0) or (op == 1 and anterior == 1) or (op == 2 and proximo == 1) or (op == 3) or (op == 4):
                break
        
        # Retornando ao menu anterior
        if op == 0:
            break
    
        # Imprimir até 10 itens anteriores
        elif op == 1 and anterior == 1:
            pagina -= 1
        
        # Imprimir até 10 próximos itens
        elif op == 2 and proximo == 1:
            pagina += 1

        # Usar item ou jogar item fora
        elif op == 3 or op == 4:
            
            escolha = 1
            pergunta = 1

            menor_indice = (pagina * 10) + 1
            maior_indice = len(jogador.inventario)

            while escolha != 0:

                if pergunta == 1:
                    if op == 3:
                        print('\nQual item deseja usar?')
                    if op == 4:
                        print('\nQual item deseja jogar fora?')
                    pergunta = 0

                escolha = utils.LerNumero('> ')
            
                # Saindo
                if escolha == 0:
                    break

                # Procedendo
                elif escolha >= menor_indice and escolha <= maior_indice:

                    item_escolhido = jogador.inventario[escolha-1]

                    if op == 3:
                        if item_escolhido[1].nome == "Erva Curativa" or \
                            item_escolhido[1].nome == "Poção de Cura Pequena" or \
                            item_escolhido[1].nome == "Poção de Mana Pequena" or \
                            item_escolhido[1].nome == "Antídoto":
                            valido = jogador_acoes.ValidaUsoConsumivel(jogador, item_escolhido)

                            if valido != -1:
                                jogador_acoes.UsarConsumivel(jogador, escolha-1)

                        else:
                            print('Este item não pode ser utilizado.')
                        
                        print('')
                        break

                    if op == 4:

                        print('\nQuantos deste item deseja jogar fora?')
                    
                        while True:

                            escolha_quantidade = utils.LerNumero('> ')

                            if escolha_quantidade == 0:
                                break

                            elif escolha_quantidade > 0 and escolha_quantidade <= item_escolhido[1].quantidade:
                                item_escolhido[1].quantidade -= escolha_quantidade

                                if item_escolhido[1].quantidade <= 0:
                                    jogador.inventario.remove(item_escolhido)

                                break

                        # Operação foi cancelada
                        if escolha_quantidade == 0:
                            pergunta = 1

                        else:
                            break
        
            # Checando se a página tinha 1 item sobrando, e ele foi removido
            tentativa_ultima_pagina = len(jogador.inventario)
            tentativa_ultima_pagina = math.ceil(tentativa_ultima_pagina / 10)
            tentativa_ultima_pagina -= 1

            if escolha != 0 and ultima_pagina != tentativa_ultima_pagina:
                ultima_pagina -= 1
                if pagina > 0:
                    pagina -= 1

            # Se o jogador jogou todos os itens fora
            if len(jogador.inventario) == 0:
                print('Você não tem itens em seu inventário.')
                return
