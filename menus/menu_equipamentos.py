import sys
from colorama import Fore, Back, Style

sys.path.append("..")
from classes_base import utils
from itens import equipamentos

def ImprimirEquipamento(item):
    """
    Recebe um item e o imprime.
    """

    if item[0] != "Item Vazio":
        mensagem = f'{item[1].nome}'.ljust(45, ' ')
        mensagem += ' | Nível: {:2d} | Tipo: '.format(item[1].nivel)
        print(mensagem, end = '')
        utils.ImprimirTipo(item[1].tipo)
        print('')
    else:
        print('----------')

def ImprimirEquipados(jogador):
    """
    Imprime os equipamentos atualmente equipados no jogador.
    """

    print('|========================================> EQUIPAMENTOS <========================================|')

    mao_1 = jogador.equipados[0]
    mao_2 = jogador.equipados[1]
    cabeca = jogador.equipados[2]
    peitoral = jogador.equipados[3]
    pes = jogador.equipados[4]
    acessorio = jogador.equipados[5]

    print('[1]       Mão: ', end = '')
    ImprimirEquipamento(mao_1)

    print('[2]       Mão: ', end = '')
    ImprimirEquipamento(mao_2)

    print('[3]    Cabeça: ', end = '')
    ImprimirEquipamento(cabeca)

    print('[4]  Peitoral: ', end = '')
    ImprimirEquipamento(peitoral)

    print('[5]       Pés: ', end = '')
    ImprimirEquipamento(pes)

    print('[6] Acessório: ', end = '')
    ImprimirEquipamento(acessorio)
    
    print('')

def EquipadosGanhos(jogador):
    """
    Aumenta os atributos do jogador e concede efeitos baseados nos itens equipados.
    """

    # Aumentando os atributos do jogador
    equipado_indice = 0
    for e in jogador.equipados:
        if equipado_indice == 1 and e[0] == "Duas Mãos":
            pass

        else:
            jogador.maxHp += e[1].maxHp
            jogador.hp += e[1].hp
            jogador.maxMana += e[1].maxMana
            jogador.mana += e[1].mana

            jogador.ataque += e[1].ataque
            jogador.defesa += e[1].defesa
            jogador.magia += e[1].magia
            jogador.velocidade += e[1].velocidade

        equipado_indice += 1

def EquipadosPerdas(jogador):
    """
    Diminui os atributos do jogador e retira efeitos baseados nos itens equipados.
    """

    # Diminuindo os atributos do jogador
    equipado_indice = 0
    for e in jogador.equipados:
        if equipado_indice == 1 and e[0] == "Duas Mãos":
            pass

        else:
            jogador.maxHp -= e[1].maxHp
            jogador.hp -= e[1].hp
            jogador.maxMana -= e[1].maxMana
            jogador.mana -= e[1].mana

            jogador.ataque -= e[1].ataque
            jogador.defesa -= e[1].defesa
            jogador.magia -= e[1].magia
            jogador.velocidade -= e[1].velocidade

        equipado_indice += 1
    
    # Voltando o tipo do Ataque Normal para "Normal"
    ataque_indice = jogador.HabilidadePresente("Atacar")
    jogador.habilidades[ataque_indice].tipo = "Normal"

def MenuDesequipar(jogador, lugar, verbose = 1):
    """
    Menu que gerencia a ação de desequipar do jogador. Retorna:
    * 1 e o nome do equipamento desequipado, se foi possível desequipar um item;
    * 0 e "Item Vazio", caso contrário.

    <lugar> é um número inteiro que tem a seguinte equivalência:
    * 1 = Mão
    * 2 = Mão
    * 3 = Cabeça
    * 4 = Peitoral
    * 5 = Pés
    * 6 = Acessório

    Se verbose for igual à 0, a função não imprimirá nenhuma mensagem.
    """

    item = jogador.equipados[lugar - 1]

    if item[0] == "Item Vazio":
        return 0, "Item Vazio"

    # Mãos
    if lugar == 1 or lugar == 2:
        if item[0] == "Item Vazio" and verbose == 1:
            print('Não há nada equipado nesta mão para você desequipar.\n')

        # Desequipando Item
        else:
            vazio = equipamentos.Vazio()
            jogador.AdicionarAoInventario(item)

            if item[0] == "Uma Mão":
                jogador.equipados[lugar - 1] = vazio
            
            else:
                jogador.equipados[0] = vazio
                vazio_2 = equipamentos.Vazio()
                jogador.equipados[1] = vazio_2

            return 1, item[1].nome

    # Cabeça
    elif lugar == 3 and item[0] == "Item Vazio" and verbose == 1:
        print('Não há nada equipado na cabeça para você desequipar.\n')
    
    # Peitoral
    elif lugar == 4 and item[0] == "Item Vazio" and verbose == 1:
        print('Não há nada equipado no peitoral para você desequipar.\n')

    # Pés
    elif lugar == 5 and item[0] == "Item Vazio" and verbose == 1:
        print('Não há nada equipado nos pés para você desequipar.\n')

    # Acessório
    elif lugar == 6 and item[0] == "Item Vazio" and verbose == 1:
        print('Não há acessório equipado para você desequipar.\n')

    # Desequipando Item
    else:
        vazio = equipamentos.Vazio()
        jogador.AdicionarAoInventario(item)
        jogador.equipados[lugar - 1] = vazio

        return 1, item[1].nome
    
    return 0, "Item Vazio"

def ClonarEquipar(jogador, lugar, item, lugar_adicional = None, verbose = 0):
    """
    Esta função é chamada ao:
    * Cancelar a operação de equipar um item;
    * Equipar um item.

    Se verbose for igual à 0, a função não imprimirá nenhuma mensagem.
    """

    # Criando um clone do item
    item_clone = (item[0], item[1].ClonarItem())
    item_clone[1].quantidade = 1

    # Equipando o clone
    jogador.equipados[lugar - 1] = item_clone
    
    if lugar_adicional is not None:
        jogador.equipados[lugar_adicional - 1] = item_clone

    # Imprimindo a mensagem se a verbose for igual à 1
    if verbose == 1:
        print(f'{item_clone[1].nome} foi equipado.\n')

    # Reduzindo a quantidade e possivelmente removendo o item do inventário
    item[1].quantidade -= 1
    if item[1].quantidade <= 0:
        jogador.inventario.remove(item)

def MenuEquipar(jogador, lugar):
    """
    Menu que gerencia a ação de equipar do jogador. Retorna:
    * 1 e o nome do equipamento equipado, se foi possível equipar um item;
    * 0 e "Item Vazio", caso contrário.
    
    <lugar> é um número inteiro que tem a seguinte equivalência:
    * 1 = Mão
    * 2 = Mão
    * 3 = Cabeça
    * 4 = Peitoral
    * 5 = Pés
    * 6 = Acessório
    """

    # Estados do inventário e equipados antes de qualquer modificação
    inventario_antigo = jogador.ClonarLista(jogador.inventario)
    equipados_antigo = jogador.ClonarLista(jogador.equipados)

    # Classificação do item
    if lugar == 1 or lugar == 2:
        classificacao = "Uma Mão"
    elif lugar == 3:
        classificacao = "Cabeça"
    elif lugar == 4:
        classificacao = "Peitoral"
    elif lugar == 5:
        classificacao = "Pés"
    elif lugar == 6:
        classificacao = "Acessório"
        
    print('Qual item você deseja equipar?')

    # Imprimindo os itens que podem ser equipados
    print_indice = 1
    item_indice = 0
    relacao = [(0, -1)]

    for item in jogador.inventario:

        if (classificacao == "Uma Mão") and (item[0] == "Uma Mão" or item[0] == "Duas Mãos") and \
            (item[1].nivel <= jogador.nivel):

            print(f'[{print_indice}] {item[1].nome} - Nível: {item[1].nivel} - Tipo: ', end = '')
            utils.ImprimirTipo(item[1].tipo)
            print('')
            relacao.append((print_indice, item_indice))
            print_indice += 1
        
        elif (item[0] == classificacao) and (item[1].nivel <= jogador.nivel):
            
            print(f'[{print_indice}] {item[1].nome} - Nível: {item[1].nivel} - Tipo: ', end = '')
            utils.ImprimirTipo(item[1].tipo)
            print('')
            relacao.append((print_indice, item_indice))
            print_indice += 1

        item_indice += 1
    
    print('\n[0] Cancelar e retornar ao menu anterior.\n')

    # Jogador escolhe qual item quer equipar ou se quer cancelar a operação
    while True:
        escolha = utils.LerNumero('> ')

        if escolha >= 0 and escolha <= relacao[-1][0]:
            break
    
    # Mapeando a escolha para um índice do inventario
    for r in relacao:
        if r[0] == escolha:
            escolha = r[1]
            break
    
    # Jogador procedeu com a operação
    if escolha != -1:

        item_equipado = jogador.inventario[escolha]

        if ((lugar == 1 or lugar == 2) and item_equipado[0] == "Uma Mão") or (lugar >= 3 and lugar <= 6):
            MenuDesequipar(jogador, lugar, verbose = 0)
            ClonarEquipar(jogador, lugar, item_equipado, verbose = 1)

        elif (lugar == 1 or lugar == 2) and item_equipado[0] == "Duas Mãos":
            MenuDesequipar(jogador, 1, verbose = 0)
            MenuDesequipar(jogador, 2, verbose = 0)
            ClonarEquipar(jogador, 1, item_equipado, 2, verbose = 1)

        return 1, item_equipado[1].nome

    # Jogador cancelou a operação
    else:
        
        # Retornando aos estados do inventário e equipados antes de qualquer modificação
        jogador.inventario = inventario_antigo
        jogador.equipados = equipados_antigo

        return 0, "Item Vazio"

def MenuEquipamentos(jogador):
    """
    Menu de gerenciamento dos equipamentos do jogador. Retorna 1 se o jogador realizou alguma troca de equipamentos
    e retorna 0 caso contrário.
    """

    EquipadosPerdas(jogador)

    flag = 0
    troca_realizada = 0
    retorno = 1

    while True:

        # Jogador realizou alguma troca de equipamentos
        if flag == 1:
            troca_realizada = 1

        if retorno == 1:
            ImprimirEquipados(jogador)
            print('[1] Equipar')
            print('[2] Desequipar\n')
            print('[0] Retornar ao menu anterior')
            retorno = 0

        op = utils.LerNumero('> ')

        # Voltar ao Menu Anterior
        if op == 0:
            break

        # Equipar
        elif op == 1:
            print("\nEm qual lugar deseja equipar?")

            # Jogador escolhe um lugar para equipar (Mão, Peitoral, etc.)
            while True:
                lugar = utils.LerNumero('> ')

                if lugar >= 0 and lugar <= 6:
                    print('')
                    break
            
            # Jogador procede em equipar
            if lugar > 0:
                flag, inutilizado = MenuEquipar(jogador, lugar)

            retorno = 1

        # Desequipar
        elif op == 2:
            print("\nEm qual lugar deseja desequipar?")

            # Jogador escolhe um lugar para desequipar (Mão, Peitoral, etc.)
            while True:
                lugar = utils.LerNumero('> ')

                if lugar >= 0 and lugar <= 6:
                    print('')
                    break
            
            # Jogador procede em desequipar
            if lugar > 0:
                flag, inutilizado = MenuDesequipar(jogador, lugar)

            retorno = 1
    
    EquipadosGanhos(jogador)
    
    return troca_realizada
    