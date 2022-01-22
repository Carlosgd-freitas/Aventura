import math
import sys
from colorama import Fore, Back, Style

from . import imprimir
sys.path.append("..")
from classes_base import utils

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

    inventario = jogador.inventario
    indice_print = 1
    indice_item = 0
    relacao = [(0, -1)]

    print('\nEscolha qual consumível deseja usar:')
    for item in inventario:

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
        # Poções de cura com o hp cheio
        if jogador.hp == jogador.maxHp and inventario[escolha][1].nome == "Poção de Cura Pequena":
            print('Seu ' + Fore.RED + 'HP' + Style.RESET_ALL + ' já está maximizado.')
            escolha = -1
        
        # Poções de mana com a mana cheia
        elif jogador.mana == jogador.maxMana and inventario[escolha][1].nome == "Poção de Mana Pequena":
            print('Sua ' + Fore.BLUE + 'Mana' + Style.RESET_ALL + ' já está maximizada.')
            escolha = -1
        
        # Antídoto sem estar envenenado
        elif jogador.EfeitoPresente("debuff", "Veneno") == -1 and inventario[escolha][1].nome == "Antídoto":
            print('Você não está ' + Fore.GREEN + 'envenenado' + Style.RESET_ALL + '.')
            escolha = -1
    
    return escolha

def UsarConsumivel(jogador, indice, criaturas):
    """
    Utiliza uma item consumível do inventário do jogador.

    Parâmetros:
        - jogador: jogador que irá utilizar o item consumível;
        - indice: índice do item no inventário;
        - criaturas: lista de criaturas inimigas atualmente em combate;
    """

    item = jogador.inventario[indice][1]

    # Processando os buffs que o item concede
    for buff in item.buffs:

        sobrecura_hp = 0
        sobrecura_mana = 0

        # Cura o HP em um valor definido
        if buff.nome == "Cura HP":
            jogador.hp += buff.valor
            mensagem = f'A {item.nome} recuperou {valor} de ' + Fore.RED + 'HP' + Style.RESET_ALL + '.'
            sobrecura_hp = 1
        
        # Cura o HP com base no HP máximo
        elif buff.nome == "Cura HP %":
            valor = math.floor(jogador.maxHp * (buff.valor / 100))
            jogador.hp += valor
            mensagem = f'A {item.nome} recuperou {valor} de ' + Fore.RED + 'HP' + Style.RESET_ALL + '.'
            sobrecura_hp = 1
        
        # Cura o HP com base no HP máximo ou em um valor definido, o que for maior
        elif buff.nome == "Cura HP % ou valor":
            valor1 = math.floor(jogador.maxHp * (buff.valor[0] / 100))
            valor2 = buff.valor[1]

            if valor1 > valor2:
                valor = valor1
            else:
                valor = valor2

            jogador.hp += valor
            mensagem = f'A {item.nome} recuperou {valor} de ' + Fore.RED + 'HP' + Style.RESET_ALL + '.'
            sobrecura_hp = 1
        
        # Cura a Mana em um valor definido
        elif buff.nome == "Cura Mana":
            jogador.mana += buff.valor
            mensagem = f'A {item.nome} recuperou {valor} de ' + Fore.BLUE + 'Mana' + Style.RESET_ALL + '.'
            sobrecura_mana = 1
        
        # Cura a Mana com base na Mana máxima
        elif buff.nome == "Cura Mana %":
            valor = math.floor(jogador.maxMana * (buff.valor / 100))
            jogador.mana += valor
            mensagem = f'A {item.nome} recuperou {valor} de ' + Fore.BLUE + 'Mana' + Style.RESET_ALL + '.'
            sobrecura_mana = 1
        
        # Cura a Mana com base na Mana máxima ou em um valor definido, o que for maior
        elif buff.nome == "Cura Mana % ou valor":
            valor1 = math.floor(jogador.maxMana * (buff.valor[0] / 100))
            valor2 = buff.valor[1]

            if valor1 > valor2:
                valor = valor1
            else:
                valor = valor2

            jogador.mana += valor
            mensagem = f'A {item.nome} recuperou {valor} de ' + Fore.BLUE + 'Mana' + Style.RESET_ALL + '.'
            sobrecura_mana = 1
        
        # Cura debuff de envenenamento
        elif buff.nome == "Cura Veneno":
            debuff_indice = jogador.EfeitoPresente("debuff", "Veneno")
            jogador.debuffs.remove(jogador.debuffs[debuff_indice])
            mensagem = f'O {item.nome} curou seu ' + Fore.GREEN + 'envenenamento' + Style.RESET_ALL + '.'
        
        # Dá dano em todos os inimigos
        elif buff.nome == "Dano todos inimigos":
            for c in criaturas:
                dano = buff.valor - c.defesa

                # Checando se o alvo está defendendo
                if c.EfeitoPresente("buff", "Defendendo") != -1:
                    indice = c.EfeitoPresente("buff", "Defendendo")
                    valor = c.buffs[indice].valor
                    dano *= (valor / 100)
                
                dano = math.floor(dano)
                if dano < 0:
                    dano = 0

                c.hp -= dano
                mensagem = f'A {item.nome} infligiu {dano} de dano em {c.nome}.'

                if c.hp < 0:
                    c.hp = 0

        # Caso o HP ou Mana estrapole o valor máximo
        if sobrecura_hp == 1 and jogador.hp >= jogador.maxHp:
            jogador.hp = jogador.maxHp
            mensagem = f'A {item.nome} maximizou seu ' + Fore.RED + 'HP' + Style.RESET_ALL + '.'
            
        elif sobrecura_mana == 1 and jogador.mana >= jogador.maxMana:
            jogador.mana = jogador.maxMana
            mensagem = f'A {item.nome} maximizou sua ' + Fore.BLUE + 'Mana' + Style.RESET_ALL + '.'
        
        print(mensagem)

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
            utils.ImprimirTipo(h.tipo)

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
