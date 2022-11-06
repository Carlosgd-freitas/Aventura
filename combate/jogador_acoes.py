import sys
from colorama import Fore, Back, Style

sys.path.append("..")
from base import imprimir, utils

def EscolherAlvo(criaturas):
    """
    Imprime as possíveis criaturas que o jogador pode atacar ou usar uma habilidade de alvo único e retorna
    o índice da lista de criaturas correspondente ao alvo escolhido.
    """

    print('\nEscolha quem deseja atacar:')
    i = 1
    for c in criaturas:
        imprimir.ImprimirCriatura(i, c)
        i += 1
    
    print('\n[0] Retornar e escolher outra ação.\n')

    while True:
        alvo = utils.LerNumero('> ')

        if alvo >= 0 and alvo <= len(criaturas):
            break
    
    return alvo-1

def EscolherConsumivel(jogador):
    """
    Imprime os possíveis consumíveis que o jogador pode usar e retorna o índice do inventário correspondente
    ao item escolhido.
    """

    indice_print = 1
    indice_item = 0
    relacao = [(0, -1)]

    print('\nEscolha qual consumível deseja usar:')
    for item in jogador.inventario:

        if item[0] == "Consumivel":
            print(f'[{indice_print}] {item[1].nome} - Quantidade: {item[1].quantidade}')
            relacao.append((indice_print, indice_item))
            indice_print += 1

        indice_item += 1
    
    print('\n[0] Retornar e escolher outra ação.\n')

    while True:
        escolha = utils.LerNumero('> ')

        if escolha >= 0 and escolha <= jogador.ContarItens("Consumivel"):
            break
    
    # Mapeando a escolha para um índice do inventario
    for r in relacao:
        if r[0] == escolha:
            escolha = r[1]
            break
    
    # Impedindo alguns itens de serem utilizados em algumas situações
    if escolha != -1:
        valido = ValidaUsoConsumivel(jogador, jogador.inventario[escolha])

        if valido == -1:
            escolha = -1

    return escolha

def ValidaUsoConsumivel(jogador, item):
    """
    Retorna 1 se o item consumível pode ser utilizado normalmente ou -1 caso contrário.
    """
    valido = 1

    # Usar itens com o hp cheio: Poções de cura, Poções de Regeneração, Erva Curativa ou Mel de Abelhóide
    if jogador.hp == jogador.maxHp and (item[1].nome == "Poção de Cura Pequena" or \
        item[1].nome == "Poção de Regeneração Pequena" or item[1].nome == "Erva Curativa" or \
        item[1].nome == "Mel de Abelhóide"):
        print('Seu ' + Fore.RED + 'HP' + Style.RESET_ALL + ' já está maximizado.')
        valido = -1
    
    # Poções de mana com a mana cheia
    elif jogador.mana == jogador.maxMana and item[1].nome == "Poção de Mana Pequena":
        print('Sua ' + Fore.BLUE + 'Mana' + Style.RESET_ALL + ' já está maximizada.')
        valido = -1
    
    # Antídoto sem estar envenenado
    elif jogador.EfeitoPresente("debuff", "Veneno") == -1 and item[1].nome == "Antídoto":

        if jogador.genero == "M":
            print('Você não está ' + Fore.GREEN + 'envenenado' + Style.RESET_ALL + '.')
        elif jogador.genero == "F":
            print('Você não está ' + Fore.GREEN + 'envenenada' + Style.RESET_ALL + '.')

        valido = -1
    
    return valido

def UsarConsumivel(jogador, indice, inimigos = None):
    """
    Utiliza uma item consumível do inventário do jogador.

    Parâmetros:
        - jogador: jogador que irá utilizar o item consumível;
        - indice: índice do item no inventário;
        - inimigos: lista de criaturas inimigas atualmente em combate.
    """

    item = jogador.inventario[indice][1]

    # Processando os buffs que o item concede
    for buff in item.buffs:
        utils.ProcessarEfeito(jogador, buff, jogador, item = item)
    
    # Processando dano e os debuffs que o item concede
    for debuff in item.debuffs:

        # Debuffs que afetam todos os inimigos
        if debuff.nome == "Dano todos inimigos" or debuff.nome == "Lentidão todos inimigos":
            for c in inimigos:
                utils.ProcessarEfeito(jogador, debuff, c, item = item)
                
    # Contabilizando a usagem do item
    item.quantidade -= 1
    if item.quantidade == 0:
        jogador.inventario.remove(jogador.inventario[indice])

def EscolherHabilidade(jogador):
    """
    Imprime as possíveis habilidades que o jogador pode usar e retorna o índice da lista de habilidades
    correspondente à habilidade escolhida.
    """

    print('\nEscolha qual habilidade deseja usar:')

    indice_atacar = jogador.HabilidadePresente("Atacar")
    indice_print = 1
    indice_item = 0
    relacao = [(0, -1)]

    for h in jogador.habilidades:

        # A habilidade de ataque normal, bem como habilidades passivas, não serão listadas
        if (indice_item != indice_atacar) and (h.passiva_ativa == "ativa"):
            mensagem = f'[{indice_print}] {h.nome} - Tipo: '
            print(mensagem, end = '')
            imprimir.ImprimirTipo(h.tipo)

            mensagem = ' - Custo: '

            # Imprimindo os custos de utilizar a habilidade
            i_2 = 0
            for c in h.custo:
                if i_2 > 0:
                    print(' e ')

                mensagem += f'{c[1]} '

                if c[0] == "Mana":
                    mensagem += Fore.BLUE + 'Mana' + Style.RESET_ALL
                elif c[0] == "HP":
                    mensagem += Fore.RED + 'HP' + Style.RESET_ALL
                
                i_2 += 1  
            
            # Imprimindo a recarga da habilidade
            mensagem += f' - Recarga: {h.recarga_atual}/{h.recarga}'

            print(mensagem)
            relacao.append((indice_print, indice_item))
            indice_print += 1

        indice_item += 1
    
    print('\n[0] Retornar e escolher outra ação.\n')

    while True:
        valido = 1
        escolha = utils.LerNumero('> ')

        if escolha >= 0 and escolha <= relacao[-1][0]:

            # Mapeando a escolha para um índice da lista de habilidades
            for r in relacao:
                if r[0] == escolha:
                    escolha = r[1]
                    break
            
            if escolha != -1:

                # Checando o custo de usar a habilidade
                for c in jogador.habilidades[escolha].custo:
                    if c[0] == "Mana" and c[1] > jogador.mana:
                        print('Você não tem ' + Fore.BLUE + 'Mana' + Style.RESET_ALL +
                            ' o suficiente para usar esta habilidade.')
                        valido = 0

                    elif c[0] == "HP" and c[1] > jogador.hp:
                        print('Você não tem ' + Fore.RED + 'HP' + Style.RESET_ALL +
                            ' o suficiente para usar esta habilidade.')
                        valido = 0

                # Checando a recarga da habilidade
                if jogador.habilidades[escolha].recarga_atual < jogador.habilidades[escolha].recarga:
                    print('Esta habilidade ainda está em recarga.')
                    valido = 0

            if valido == 1:
                break
    
    return escolha
